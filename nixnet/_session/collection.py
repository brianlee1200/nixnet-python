﻿from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props


class Collection(object):
    """Collection of items in a session."""

    def __init__(self, handle):
        self._handle = handle
        self.__list_cache = None

    def __len__(self):
        return _props.get_session_num_in_list(self._handle)

    def __iter__(self):
        item_count = len(self)
        item_names = self._list_cache
        assert item_count == len(item_names), \
            "Frame count ({}) is out of sync with items ({})".format(item_count, item_names)
        for index, name in enumerate(item_names):
            yield self._create_item(self._handle, index, name)

    def __getitem__(self, index):
        if isinstance(index, six.integer_types):
            name = self._list_cache[index]
        elif isinstance(index, six.string_types):
            name = index
            item_names = self._list_cache
            try:
                index = item_names.index(name)
            except ValueError:
                _errors.check_error(_cconsts.NX_ERR_INVALID_ACTIVE_FRAME_NAME)
        else:
            _errors.check_error(_cconsts.NX_ERR_INVALID_ACTIVE_FRAME_INDEX)

        return self._create_item(self._handle, index, name)

    @property
    def _list_cache(self):
        if self.__list_cache is None:
            self.__list_cache = _props.get_session_list(self._handle)
        return self._list_cache

    def _create_item(self, index, name):
        raise NotImplementedError("Leaf classes must implement this")


class Item(object):
    """Item configuration for a session."""

    def __init__(self, handle, index, name):
        self._handle = handle
        self._index = index
        self._name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle and self._index == self._index
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __int__(self):
        return self._index

    def __str__(self):
        return self._name
