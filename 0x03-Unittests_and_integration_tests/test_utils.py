#!/usr/bin/env python3
'''A module for testing the utils module
'''

import unittest

from parameterized import parameterized
from typing import (
    Dict,
    Mapping,
    Sequence,
    Tuple,
    Union,
)

from utils import (
    access_nested_map
)


class TestAccessNestedMap(unittest.TestCase):
    '''Test case for `access_nested_map` function.
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]
            ) -> None:
        '''Tests `access_nexted_map`'s output
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception: Exception,
            ) -> None:
        '''Tests `access_nested_map`'s exception raising.
        '''
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
