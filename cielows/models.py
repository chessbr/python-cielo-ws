# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from cielows.constants import CieloPaymentType, CieloCurrency,\
    CieloPaymentInterest
import six
from datetime import datetime
from cielows.utils import validate_cc
from cielows.exceptions import ValidationError


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

    def __init__(self, street, number, complement, zip_code, city, state, country):
        self.street = street
        self.number = number
        self.complement = complement
        self.zip_code = zip_code
        self.city = city
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
        self.name = cielo_data["Customer"].get("Name")
        self.email = cielo_data["Customer"].get("Email")
        self.birth_date = cielo_data["Customer"].get("Birthdate")
        self.identity = cielo_data["Customer"].get("Identity")
        self.identity_type = cielo_data["Customer"].get("IdentityType")

        if cielo_data["Customer"].get("Address"):
            self.address = CieloFactory.new_customer_address(
                street=cielo_data["Customer"]["Address"].get("Street"),
                number=cielo_data["Customer"]["Address"].get("Number"),
                complement=cielo_data["Customer"]["Address"].get("Complement"),
                zip_code=cielo_data["Customer"]["Address"].get("ZipCode"),
                city=cielo_data["Customer"]["Address"].get("City"),
                state=cielo_data["Customer"]["Address"].get("State"),
                country=cielo_data["Customer"]["Address"].get("Country"),
            )

        if cielo_data["Customer"].get("DeliveryAddress"):
            self.delivery_address = CieloFactory.new_customer_address(
                street=cielo_data["Customer"]["DeliveryAddress"].get("Street"),
                number=cielo_data["Customer"]["DeliveryAddress"].get("Number"),
                complement=cielo_data["Customer"]["DeliveryAddress"].get("Complement"),
                zip_code=cielo_data["Customer"]["DeliveryAddress"].get("ZipCode"),
                city=cielo_data["Customer"]["DeliveryAddress"].get("City"),
                state=cielo_data["Customer"]["DeliveryAddress"].get("State"),
                country=cielo_data["Customer"]["DeliveryAddress"].get("Country"),
            )

class CieloRequestCreditCard(object):
    card_number = None
    holder = None
    expiration_date = None
    security_code = None
    brand = None
    save_card = False
    card_token = None

    def __init__(self,
                 card_number,
                 holder,
                 expiration_date,
                 security_code,
                 brand,
                 save_card,
                 card_token):

        self.card_number = card_number
        self.holder = holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.brand = brand
        self.save_card = save_card
        self.card_token = card_token

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
        self.card_number = cielo_data["Payment"]["CreditCard"].get("CardNumber")
        self.holder = cielo_data["Payment"]["CreditCard"].get("Holder")
        self.expiration_date = cielo_data["Payment"]["CreditCard"].get("ExpirationDate")
        self.security_code = cielo_data["Payment"]["CreditCard"].get("SecurityCode")
        self.brand = cielo_data["Payment"]["CreditCard"].get("Brand")
        self.save_card = cielo_data["Payment"]["CreditCard"].get("SaveCard")
        self.card_token = cielo_data["Payment"]["CreditCard"].get("CardToken")

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
        self.credit_card = CieloFactory.new_response_credit_card(cielo_data)

        self.service_tax_amount = int(cielo_data["Payment"].get("ServiceTaxAmount"))
        self.installments = int(cielo_data["Payment"].get("Installments"))
        self.interest = cielo_data["Payment"].get("Interest")
        self.capture = cielo_data["Payment"].get("Capture")
        self.authenticate = cielo_data["Payment"].get("Authenticate")
        self.proof_of_sale = cielo_data["Payment"].get("ProofOfSale")
        self.tid = cielo_data["Payment"].get("Tid")
        self.authorization_code = cielo_data["Payment"].get("AuthorizationCode")
        self.payment_id = cielo_data["Payment"].get("PaymentId")
        self.payment_type = cielo_data["Payment"].get("Type")
        self.currency = cielo_data["Payment"].get("Currency")
        self.country = cielo_data["Payment"].get("Country")
        self.status = int(cielo_data["Payment"].get("Status"))
        self.return_code = cielo_data["Payment"].get("ReturnCode")
        self.return_message = cielo_data["Payment"].get("ReturnMessage")
        self.amount = int(cielo_data["Payment"].get("Amount"))
        self.captured_amount = int(cielo_data["Payment"].get("CapturedAmount"))

        self.links = [CieloFactory.new_payment_link(link["Method"], link["Rel"], link["Href"]) \
                        for link in cielo_data["Payment"].get("Links", [])]

        self.extra_data_collection = cielo_data["Payment"].get("ExtraDataCollection", [])


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
        self.customer = customer
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

        if not isinstance(name, six.string_types):
            raise TypeError("name must be a string")

        elif email and not isinstance(email, six.string_types):
            raise TypeError("email must be a string")

        elif birth_date:
            if not isinstance(birth_date, six.string_types):
                raise TypeError("birth_date must be a string")

            # convert string to datetime.. it must not throw exceptions..
            datetime.strptime(birth_date, '%Y-%m-%d')

        if address and not isinstance(address, CieloCustomerAddress):
            raise TypeError("address must be a CieloCustomerAddress instance")

        elif delivery_address and not isinstance(delivery_address, CieloCustomerAddress):
            raise TypeError("delivery_address must be a CieloCustomerAddress instance")

        return CieloRequestCustomer(name, email, birth_date, address, delivery_address)

    @staticmethod
    def new_response_customer(cielo_data):
        '''
        Creates a new CieloResponseCostumer object
        '''
        if not cielo_data or not isinstance(cielo_data, dict):
            raise TypeError("cielo_data must be a valid dictionary")

        return CieloResponseCustomer(cielo_data)

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

        if street and not isinstance(street, six.string_types):
            raise TypeError("street must be a string")

        elif number and not isinstance(number, six.string_types):
            raise TypeError("number must be a string")

        elif complement and not isinstance(complement, six.string_types):
            raise TypeError("complement must be a string")

        elif zip_code and not isinstance(zip_code, six.string_types):
            raise TypeError("zip_code must be a string")

        elif city and not isinstance(city, six.string_types):
            raise TypeError("city must be a string")

        elif state and not isinstance(state, six.string_types):
            raise TypeError("state must be a string")

        elif country and not isinstance(country, six.string_types):
            raise TypeError("country must be a string")

        return CieloCustomerAddress(street=street,
                                    number=number,
                                    complement=complement,
                                    zip_code=zip_code,
                                    city=city,
                                    state=state,
                                    country=country)

    @staticmethod
    def new_request_credit_card(card_number,
                                security_code,
                                expiration_date,
                                brand,
                                holder,
                                save_card=False,
                                card_token=None):
        '''
        Creates a new CieloRequestCreditCard object

        :type: card_number string
        :type: security_number string
        :param expiration_date Expiration date in format MM/YYYY
        :type: expiration_date string
        :type: brand CieloCardBrand
        :type: holder string
        :type: save_card bool
        :type: card_token string
        '''

        if not isinstance(card_number, six.string_types):
            raise TypeError("card_number must be a string")

        elif not validate_cc(card_number):
            raise ValidationError("invalid card number")

        elif not isinstance(security_code, six.string_types):
            raise TypeError("security_code must be a string")

        elif not isinstance(brand, six.string_types):
            raise TypeError("brand must be a string")

        elif not isinstance(holder, six.string_types):
            raise TypeError("holder must be a string")

        elif not isinstance(save_card, bool):
            raise TypeError("save_card must be a boolean")

        elif card_token and not isinstance(card_token, six.string_types):
            raise TypeError("card_token must be a string")

        elif not isinstance(expiration_date, six.string_types):
            raise TypeError("expiration_date must be a string")

        # convert string to datetime.. it must not throw exceptions..
        datetime.strptime(expiration_date, '%m/%Y')

        return CieloRequestCreditCard(card_number=card_number,
                                      holder=holder,
                                      expiration_date=expiration_date,
                                      security_code=security_code,
                                      brand=brand,
                                      save_card=save_card,
                                      card_token=card_token)


    @staticmethod
    def new_response_credit_card(cielo_data):
        '''
        Creates a new CieloResponseCreditCard object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        return CieloResponseCreditCard(cielo_data)

    @staticmethod
    def new_request_payment(amount,
                            installments,
                            credit_card,
                            provider,
                            payment_type=CieloPaymentType.CreditCard,
                            currency=CieloCurrency.BRL,
                            intereset=CieloPaymentInterest.ByMerchant,
                            capture=False,
                            authenticate=False,
                            service_tax_amount=0):
        '''
        Creates a new CieloRequestPayment object

        '''

        pass

    @staticmethod
    def new_response_payment(cielo_data):
        '''
        Creates a new CieloResponsePayment object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        return CieloResponsePayment(cielo_data)


    @staticmethod
    def new_payments_query_result(cielo_data):
        '''
        Creates a new CieloPaymentsQueryResult object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        pass

    @staticmethod
    def new_payment_link(method, rel, href):
        '''
        Creates a new CieloPaymentLink object

        :type: method string
        :type: rel string
        :type: href string
        '''

        if not isinstance(method, six.string_types):
            raise TypeError("method must be a string")

        elif not isinstance(rel, six.string_types):
            raise TypeError("rel must be a string")

        elif not isinstance(href, six.string_types):
            raise TypeError("href must be a string")

        return CieloPaymentLink(method, rel, href)

    @staticmethod
    def new_request(order_id, cielo_customer, cielo_payment):
        '''
        Creates a new CieloRequest object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''

        return CieloRequest(order_id, cielo_customer, cielo_payment)

    @staticmethod
    def new_response(cielo_data):
        '''
        Creates a new CieloResponse object

        :param: cielo_data Cielo JSON data
        :type: cielo_data dict|None
        '''
        
        return CieloResponse(cielo_data)


    @staticmethod
    def new_webservice(merchant_id, merchant_key, sandbox=False):
        pass

