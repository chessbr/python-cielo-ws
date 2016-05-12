# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

class CieloWS(object):
    merchant_id = None
    merchant_key = None
    sandbox = False

    def __init__(self, merchant_id, merchant_key, sandbox=False):
        pass

    def authorize(self, order_id, customer, payment):
        pass

    def capture(self, payment_id, amount, service_tax_amount):
        pass

    def cancel(self, payment_id, amount):
        pass

    def query_payment(self, payment_id):
        pass

    def query_payments(self, order_id):
        pass

