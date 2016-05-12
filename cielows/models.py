# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.


class CieloJSONParsableObject(object):

    '''
    Cielo JSON parsable object
    This object has capabilities to
    populate attributes from a Cielo JSON data
    '''

    def from_json(self, json):
        '''
        Populates the attributes with the given Cielo JSON data

        :param json: Cielo REST JSON as a dictionary
        :type json: dict
        '''
        raise NotImplementedError("Implement this method.")


class CieloCustomerAddress(object):
    street = None
    number = None
    complement = None
    zip_code = None
    city = None
    state = None
    country = None

    def __init__(self, street, number, complement, zip_code, state, country):
        self.street = street
        self.number = number
        self.complement = complement
        self.zip_code = zip_code
        self.state = state
        self.country = country


class CieloRequestCustomer(object):
    name = None
    email = None
    birth_date = None
    address = None
    delivery_address = None

    def __init__(self, name, email, birth_date, address, delivery_address):
        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.address = address
        self.delivery_address = delivery_address


class CieloResponseCustomer(CieloJSONParsableObject):
    name = None
    email = None
    birth_date = None
    identity = None
    identity_type = None
    address = None
    delivery_address = None

    def __init__(self, cielo_data):
        self.from_json(cielo_data)

    def from_json(self, cielo_data):
        pass


class CieloRequestCreditCard(object):
    card_number = None
    holder = None
    expiration_date = None
    security_code = None
    brand = None
    save_card = False

    def __init__(self,
                 card_number, 
                 holder,
                 expiration_date,
                 security_code,
                 brand,
                 save_card):

        self.card_number = card_number
        self.holder = holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.brand = brand
        self.save_card = save_card


class CieloResponseCreditCard(CieloJSONParsableObject):
    card_number = None
    holder = None
    expiration_date = None
    security_code = None
    brand = None
    save_card = False
    card_token = None

    def __init__(self, cielo_data):
        self.from_json(cielo_data)

    def from_json(self, cielo_data):
        pass


class CieloPaymentLink(object):
    method = None
    rel = None
    href = None

    def __init__(self, method, rel, href):
        self.method = method
        self.rel = rel
        self.href = href


class CieloRequestPayment(object):
    amount = 0
    installments = 0
    credit_card = None
    payment_type = None
    currency = None
    country = None
    provider = None
    service_tax_amount = 0
    interest = None
    capture = False
    authenticate = False
    soft_descriptor = None

    def __init__(self, 
                 amount,
                 installments,
                 credit_card,
                 payment_type,
                 interest,
                 capture,
                 authenticate, 
                 currency,
                 country,
                 provider,
                 service_tax_amount,
                 soft_descriptor):

        self.amount = amount
        self.installments = installments
        self.credit_card = credit_card
        self.payment_type = payment_type
        self.intereset = interest
        self.capture = capture
        self.authenticate = authenticate
        self.currency = currency
        self.country = country
        self.provider = provider
        self.service_tax_amount = service_tax_amount
        self.soft_descriptor = soft_descriptor


class CieloResponsePayment(CieloJSONParsableObject):
    service_tax_amount = 0
    installments = 0
    interest = None
    capture = False
    authenticate = False
    credit_card = None
    proof_of_sale = None
    tid = None
    authorization_code = None
    payment_id = None
    payment_type = None
    currency = None
    country = None
    extra_data_collection = []
    status = -1
    return_code = None
    return_message = None
    links = []
    amount = 0
    captured_amount = 0

    def __init__(self, cielo_data):
        self.from_json(cielo_data)
    
    def from_json(self, cielo_data):
        pass

class CieloPaymentsQueryResult(CieloJSONParsableObject):

    class CieloPaymentQueryResult(object):
        payment_id = None
        received_date = None

        def __init__(self, payment_id, received_date):
            self.payment_id = payment_id
            self.received_date = received_date


    payments = []

    def __init__(self, cielo_data):
        self.from_json(cielo_data)
    
    def from_json(self, cielo_data):
        pass


class CieloRequest(object):
    order_id = None
    customer = None
    payment = None

    def __init__(self, order_id, customer, payment):
        self.order_id = order_id
        self.customer = curstomer
        self.payment = payment

class CieloResponse(CieloJSONParsableObject):
    order_id = None
    customer = None
    payment = None

    def __init__(self, cielo_data):
        self.from_json(cielo_data)

    def from_json(self, cielo_data):
        pass


class CieloFactory(object):

    '''
    Creates and configures Cielo objects
    '''

    @staticmethod
    def new_request_customer(name,
                             email=None,
                             birth_date=None,
                             address=None,
                             delivery_address=None):
        '''
        Creates a new CieloRequestCostumer object

        :type: name string
        :type: email string|None
        :param: birth_date customer birth date in format 'YYYY-MM-DD'
        :type: birth_date string|None
        :type: address CieloCustomerAddress|None
        :type: delivery_address CieloCustomerAddress|None
        '''

        pass

    @staticmethod
    def new_response_customer(cielo_data):
        '''
        Creates a new CieloResponseCostumer object
        '''

        pass

    @staticmethod
    def new_customer_address(street=None,
                             number=None,
                             complement=None,
                             zip_code=None,
                             city=None,
                             state=None,
                             country=None):
        '''
        Creates a new CieloCustomerAddress object
        '''

        pass

    @staticmethod
    def new_request_credit_card(card_number,
                                security_code,
                                expiration_date,
                                brand,
                                holder,
                                save_card=False):
        '''
        Creates a new CieloRequestCreditCard object

        :type: card_number string
        :type: security_number string
        :param expiration_date Expiration date in format MM/YYYY
        :type: expiration_date string
        :type: brand CieloCardBrand
        :type: holder string
        :type: save_card bool
        '''

        pass

    @staticmethod
    def new_response_credit_card(cielo_data):
        '''
        Creates a new CieloResponseCreditCard object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        pass

    @staticmethod
    def new_request_payment(amount,
                            installments,
                            credit_card,
                            provider,
                            payment_type=CieloPaymentType.CreditCard,
                            currency=CieloCurrency.BRL,
                            intereset=CieloPaymentInterest.ByMerchant,
                            capture=False,
                            authenticate=False
                            service_tax_amount=0):
        '''
        Creates a new CieloRequestPayment object

        '''

        pass

    @staticmethod
    def new_response_payment(cielo_data)
        '''
        Creates a new CieloResponsePayment object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        pass


    @staticmethod
    def new_payments_query_result(cielo_data):
        '''
        Creates a new CieloPaymentsQueryResult object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        pass


    @staticmethod
    def new_request(order_id, cielo_customer, cielo_payment)
        '''
        Creates a new CieloRequest object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''
        pass


    @staticmethod
    def new_response(cielo_data)
        '''
        Creates a new CieloResponse object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''
        pass


    @staticmethod
    def new_webservice(merchant_id, merchant_key, sandbox=False)
        pass

