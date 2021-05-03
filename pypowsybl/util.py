#
# Copyright (c) 2020, RTE (http://www.rte-france.com)
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
import _pypowsybl
from typing import List
from typing import Callable
import pandas as pd
from _pypowsybl import PyPowsyblError


class ObjectHandle:
    def __init__(self, ptr):
        self.ptr = ptr

    def __del__(self):
        _pypowsybl.destroy_object_handle(self.ptr)


class ContingencyContainer(ObjectHandle):
    def __init__(self, ptr):
        ObjectHandle.__init__(self, ptr)

    def add_single_element_contingency(self, element_id: str, contingency_id: str = None):
        _pypowsybl.add_contingency(self.ptr, contingency_id if contingency_id else element_id, [element_id])

    def add_multiple_elements_contingency(self, elements_ids: List[str], contingency_id: str):
        _pypowsybl.add_contingency(self.ptr, contingency_id, elements_ids)

    def add_single_element_contingencies(self, elements_ids: List[str], contingency_id_provider: Callable[[str], str] = None):
        for element_id in elements_ids:
            contingency_id = contingency_id_provider(element_id) if contingency_id_provider else element_id
            _pypowsybl.add_contingency(self.ptr, contingency_id, [element_id])


def create_data_frame_from_series_array(series_array, index_column_name: str):
    series_dict = {}
    index = None
    for series in series_array:
        if series.type == 0:  # string
            if series.name == index_column_name:
                index = series.str_data
            else:
                series_dict[series.name] = series.str_data
        elif series.type == 1:  # double
            series_dict[series.name] = series.double_data
        elif series.type == 2:  # int
            series_dict[series.name] = series.int_data
        elif series.type == 3:  # boolean
            series_dict[series.name] = series.boolean_data
        else:
            raise PyPowsyblError(f'Unsupported series type ${series.type}')
    return pd.DataFrame(series_dict, index=index)
