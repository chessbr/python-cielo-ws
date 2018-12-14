# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.


class ValidationError(Exception):
    '''
    A validation error exception
    '''
    pass


class RequiredAttributeError(Exception):
    '''
    Some required attributes were not set
    '''
    attributes = []

    def __init__(self, attributes=[]):
        self.attributes = attributes
