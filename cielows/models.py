# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.


class CieloJSONObject(object):

    '''
    Cielo JSON compatible object model.
    Cielo base object models must override this class,
    to be able to be instantiated from a valid Cielo JSON dictionary.
    '''

    def __init__(self, json):
        '''
        Initialize the instance populating attributes
        with the given Cielo JSON data from ´json´

        :param json: Cielo REST JSON as a dictionary
        :type json: dict
        '''
        self.from_json(json)

    def from_json(self, json):
        '''
        Populates the attributes with the given Cielo JSON data

        :param json: Cielo REST JSON as a dictionary
        :type json: dict
        '''
        raise NotImplementedError("Implement this method.")

    def to_json(self):
        '''
        Returns this object as a JSON dictionary to be used on requests
        '''
        raise NotImplementedError("Implement this method.")


class CieloCustomerAddress(CieloJSONObject):
    street = ''
    number = ''
    complement = ''
    zip_code = ''
    city = ''
    state = ''
    country = ''


class CieloCustomer(CieloJSONObject):
    name = ''
    email = ''
    birth_date = ''
    identity = ''
    identity_type = None
    address = None
    delivery_address = None


class CieloCreditCard(CieloJSONObject):
    card_number = ''
    holder = ''
    expiration_date = ''
    security_code = ''
    brand = None
    save_card = False


class CieloResponseCreditCard(CieloJSONObject):
    card_number = ''
    holder = ''
    expiration_date = ''
    security_code = ''
    brand = None
    save_card = False
    card_token = ''


class CieloResponsePaymentLink(CieloJSONObject):
    method = ''
    rel = ''
    href = ''


class CieloRequestPayment(CieloJSONObject):
    payment_type = None
    credit_card = None
    amount = 0
    currency = ''
    country = ''
    provider = ''
    service_tax_amount = 0
    installments = 0
    interest = None
    capture = False
    authenticate = False
    soft_descriptor = ''


class CieloResponsePayment(CieloJSONObject):
    service_tax_amount = 0
    installments = 0
    interest = ''
    capture = False
    authenticate = False
    credit_card = None
    proof_of_sale = ''
    tid = ''
    authorization_code = ''
    payment_id = ''
    payment_type = None
    currency = ''
    country = ''
    extra_data_collection = []
    status = 0
    return_code = ''
    return_message = ''
    links = []
    amount = 0
    captured_amount = 0


class CieloResponse(CieloJSONObject):
    merchant_order_id = ''
    customer = None
    payment = None


class CieloFactory(object):

    '''
    Creates and configures Cielo objects
    '''

    @classmethod
    def new_customer(name):
        '''
        Creates a new CieloCostumer object
        '''

        pass

    @classmethod
    def new_customer_from_cielo(cielo_data):
        '''
        Creates a new CieloCostumer object from Cielo JSON data
        :param: cielo_data Cielo JSON data
        :type: cielo_data dict
        '''

        pass

    @classmethod
    def new_customer_address():
        '''
        Creates a new CieloCustomerAddress object
        '''

        pass

    @classmethod
    def new_request_credit_card(params),
        '''
        Creates a new CieloRequestCreditCard object
        '''

        pass

    @classmethod
    def new_request_credit_card_from_cielo(cielo_data)
        '''
        Creates a new CieloRequestCreditCard object from Cielo JSON data
        :param: cielo_data Cielo JSON data
        :type: cielo_data dict
        '''

        pass

    @classmethod
    def new_response_credit_card():
        '''
        Creates a new CieloResponseCreditCard object
        '''

        pass

    @classmethod
    def new_response_credit_card_from_cielo(cielo_data):
        '''
        Creates a new CieloResponseCreditCard object from Cielo JSON data
        :param: cielo_data Cielo JSON data
        :type: cielo_data dict
        '''

        pass

    @classmethod
    def new_request_payment():
        '''
        Creates a new CieloRequestPayment object
        '''

        pass

    @classmethod
    def new_request_payment_from_cielo(CIELO_REQUEST_COMPLETE)
        '''
        Creates a new CieloRequestPayment object from Cielo JSON data
        :param: cielo_data Cielo JSON data
        :type: cielo_data dict
        '''

        pass

    @classmethod
    def new_response_payment(payment_type=TYPE,
        '''
        Creates a new CieloResponsePayment object
        '''

        pass

    @classmethod
    def new_response_payment_from_cielo(CIELO_RESPONSE_COMPLETE)
        '''
        Creates a new CieloResponsePayment object from Cielo JSON data
        :param: cielo_data Cielo JSON data
        :type: cielo_data dict
        '''

        pass

    @classmethod
    def new_request(ORDER_ID, cielo_customer, cielo_payment)
        pass

    @classmethod
    def new_response(ORDER_ID, cielo_customer, cielo_payment)
        pass

    @classmethod
    def new_webservice(merchant_id, merchant_key, sandbox=False)
        pass

