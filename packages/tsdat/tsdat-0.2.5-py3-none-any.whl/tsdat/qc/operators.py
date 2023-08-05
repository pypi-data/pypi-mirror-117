import abc
from typing import Dict, List, Optional

import numpy as np
import xarray as xr

from tsdat.config import QualityTestDefinition
from tsdat.constants import ATTS
from tsdat.utils import DSUtil


class QualityOperator(abc.ABC):
    """-------------------------------------------------------------------
    Class containing the code to perform a single QC test on a Dataset
    variable.
    -------------------------------------------------------------------"""
    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters={}):
        """-------------------------------------------------------------------
        Args:
            ds (xr.Dataset): The dataset the operator will be applied to
            previous_data (xr.Dataset): Data from the previous processing interval
            test (QCTestDefinition)  : The test definition
            params(Dict)   : A dictionary of operator-specific parameters
        -------------------------------------------------------------------"""
        self.ds = ds
        self.previous_data = previous_data
        self.test = test
        self.params = parameters

    @abc.abstractmethod
    def run(self, variable_name: str) -> Optional[np.ndarray]:
        """-------------------------------------------------------------------
        Test a dataset's variable to see if it passes a quality check.
        These tests can be performed on the entire variable at one time by
        using xarray vectorized numerical operators.

        Args:
            variable_name (str):  The name of the variable to check

        Returns:
            np.ndarray | None: If the test was performed, return a
            ndarray of the same shape as the variable. Each value in the
            data array will be either True or False, depending upon the
            results of the test.  True means the test failed.  False means
            it succeeded.

            Note that we are using an np.ndarray instead of an xr.DataArray
            because the DataArray contains coordinate indexes which can
            sometimes get out of sync when performing np arithmectic vector
            operations.  So it's easier to just use numpy arrays.

            If the test was skipped for some reason (i.e., it was not
            relevant given the current attributes defined for this dataset),
            then the run method should return None.
        -------------------------------------------------------------------"""
        pass


class CheckMissing(QualityOperator):

    def run(self, variable_name: str) -> Optional[np.ndarray]:
        """-------------------------------------------------------------------
        Checks if any values are assigned to _FillValue or 'NaN' (for non-time
        variables) or checks if values are assigned to 'NaT' (for time variables).
        Also, for non-time variables, checks if values are above or below
        valid_range, as this is considered missing as well.
        -------------------------------------------------------------------"""

        # If this is a time variable, we check for 'NaT'
        if self.ds[variable_name].values.dtype.type == np.datetime64:
            results_array = np.isnat(self.ds[variable_name].values)

        else:
            fill_value = DSUtil.get_fill_value(self.ds, variable_name)

            # If the variable has no _FillValue attribute, then
            # we select a default value to use
            if fill_value is None:
                fill_value = -9999

            # Make sure fill value has same data type as the variable
            fill_value = np.array(fill_value, dtype=self.ds[variable_name].values.dtype.type)

            # First replace any values that are outside valid_range to be fill_value so
            # it will get flagged as missing
            self._replace_invalid_values(fill_value, variable_name)

            # First check if any values are assigned to _FillValue
            results_array = np.equal(self.ds[variable_name].values, fill_value)

            # Then, if the value is numeric, we should also check if any values are assigned to
            # NaN
            if self.ds[variable_name].values.dtype.type in (type(0.0), np.float16, np.float32, np.float64):
                results_array |= np.isnan(self.ds[variable_name].values)

            # TODO: we also need to check if any values are outside valid range
            # TODO: in the config file, we need a replace with missing handler for this test

        return results_array

    def _replace_invalid_values(self, fill_value, variable_name: str):
        valid_min = DSUtil.get_valid_min(self.ds, variable_name)
        valid_max = DSUtil.get_valid_max(self.ds, variable_name)

        if valid_min is not None and valid_max is not None:
            values = self.ds[variable_name].values
            keep_array = np.logical_not( (values < valid_min) | (values > valid_max))
            replaced_values = np.where(keep_array, values, fill_value)
            self.ds[variable_name].data = replaced_values


class CheckMin(QualityOperator):

    def run(self, variable_name: str) -> Optional[np.ndarray]:
        # Get the minimum value
        _min = self.ds[variable_name].attrs.get(self.params["key"], None)
        if isinstance(_min, List):
            _min = _min[0]

        # If no minimum value is available, then we just skip this test
        results_array = None
        if _min is not None:
            results_array = np.less(self.ds[variable_name].values, _min)

        return results_array


class CheckMax(QualityOperator):

    def run(self, variable_name: str) -> Optional[np.ndarray]:
        # Get the maximum value
        _max = self.ds[variable_name].attrs.get(self.params["key"], None)
        if isinstance(_max, List):
            _max = _max[-1]

        # If no maximum value is available, then we just skip this test
        results_array = None
        if _max is not None:
            results_array = np.greater(self.ds[variable_name].values, _max)

        return results_array


class CheckValidMin(CheckMin):

    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters):
        super().__init__(ds, previous_data, test, parameters=parameters)
        self.params["key"] = "valid_range"


class CheckValidMax(CheckMax):

    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters):
        super().__init__(ds, previous_data, test, parameters=parameters)
        self.params["key"] = "valid_range"


class CheckFailMin(CheckMin):

    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters):
        super().__init__(ds, previous_data, test, parameters=parameters)
        self.params["key"] = "fail_range"


class CheckFailMax(CheckMax):

    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters):
        super().__init__(ds, previous_data, test, parameters=parameters)
        self.params["key"] = "fail_range"


class CheckWarnMin(CheckMin):

    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters):
        super().__init__(ds, previous_data, test, parameters=parameters)
        self.params["key"] = "warn_range"


class CheckWarnMax(CheckMax):

    def __init__(self, ds: xr.Dataset, previous_data: xr.Dataset, test: QualityTestDefinition, parameters):
        super().__init__(ds, previous_data, test, parameters=parameters)
        self.params["key"] = "warn_range"


class CheckValidDelta(QualityOperator):

    def run(self, variable_name: str) -> Optional[np.ndarray]:

        valid_delta = self.ds[variable_name].attrs.get(ATTS.VALID_DELTA, None)

        # If no valid_delta is available, then we just skip this test
        results_array = None
        if valid_delta is not None:
            # We need to get the dim to diff on from the parameters
            # If dim is not specified, then we use the first dim for the variable
            dim = self.params.get('dim', None)

            if dim is None and len(self.ds[variable_name].dims) > 0:
                dim = self.ds[variable_name].dims[0]

            if dim is not None:
                # If previous data exists, then we must add the last row of
                # previous data as the first row of the variable's data array.
                # This is so that the diff function can compare the first value
                # of the file to make sure it is consistent with the previous file.

                # convert to np array
                variable_data = self.ds[variable_name].data
                axis = self.ds[variable_name].get_axis_num(dim)
                previous_row = None

                # Load the previous row from the other dataset
                if self.previous_data is not None:
                    previous_variable_data = self.previous_data.get(variable_name, None)
                    if previous_variable_data is not None:
                        # convert to np array
                        previous_variable_data = previous_variable_data.data

                        # Get the last value from the first axis
                        previous_row = previous_variable_data[-1]

                        # Insert that value as the first value of the first axis
                        variable_data = np.insert(variable_data, 0, previous_row, axis=axis)

                # If the variable is a time variable, then we convert to nanoseconds before doing our check
                if self.ds[variable_name].values.dtype.type == np.datetime64:
                    variable_data = DSUtil.datetime64_to_timestamp(variable_data)

                # Compute the difference between each two numbers and check if it exceeds valid_delta
                diff = np.absolute(np.diff(variable_data, axis=axis))
                results_array = np.greater(diff, valid_delta)

                if previous_row is None:
                    # This means our results array is missing one value for the first row, which is
                    # not included in the diff computation.
                    # We need to add False for the first row of results, since it won't fail
                    # the test.
                    first_row = np.zeros(results_array[0].size, dtype=bool)
                    results_array = np.insert(results_array, 0, first_row, axis=axis)

        return results_array


class CheckMonotonic(QualityOperator):

    def run(self, variable_name: str) -> Optional[np.ndarray]:

        results_array = None
        # We need to get the dim to diff on from the parameters
        # If dim is not specified, then we use the first dim for the variable
        dim = self.params.get('dim', None)

        if dim is None and len(self.ds[variable_name].dims) > 0:
            dim = self.ds[variable_name].dims[0]

        if dim is not None:
            # If previous data exists, then we must add the last row of
            # previous data as the first row of the variable's data array.
            # This is so that the diff function can compare the first value
            # of the file to make sure it is consistent with the previous file.

            # convert to np array
            variable_data = self.ds[variable_name].data
            axis = self.ds[variable_name].get_axis_num(dim)
            previous_row = None

            # Load the previous row from the other dataset
            if self.previous_data is not None and dim == "time":
                previous_variable_data = self.previous_data.get(variable_name, None)
                if previous_variable_data is not None:
                    # convert to np array
                    previous_variable_data = previous_variable_data.data

                    # Get the last value from the first axis
                    previous_row = previous_variable_data[-1]

                    # Insert that value as the first value of the first axis
                    variable_data = np.insert(variable_data, 0, previous_row, axis=axis)

            # If the variable is a time variable, then we convert to nanoseconds before doing our check
            if self.ds[variable_name].values.dtype.type == np.datetime64:
                variable_data = DSUtil.datetime64_to_timestamp(variable_data)

            # Compute the difference between each two numbers and check if they are either all
            # increasing or all decreasing
            diff = np.diff(variable_data, axis=axis)
            is_monotonic = np.all(diff > 0) | np.all(diff < 0) # this returns a scalar

            # Create a results array, with all values set to the results of the is_monotonic check
            results_array = np.full(variable_data.shape, not is_monotonic, dtype=bool)

        return results_array


# TODO: Other tests we might implement
# check_outlier(std_dev)




