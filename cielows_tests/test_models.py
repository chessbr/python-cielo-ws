# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

import pytest
from cielows.models import CieloFactory
from cielows.constants import CieloPaymentType, CieloCardBrand
from cielows_tests.fake_data import CIELO_REQUEST_COMPLETE,\
    CIELO_RESPONSE_COMPLETE, PAYMENTS_QUERY_RESULT
from cielows.exceptions import ValidationError, RequiredAttributeError


def test_cielo_customer():
    NAME = "Jorge da Silva"

    # @test: create from kwargs
    cielo_customer = CieloFactory.new_request_customer(name=NAME)
    assert cielo_customer.name == NAME
    assert cielo_customer.email == None
    assert cielo_customer.birth_date == None
    assert cielo_customer.address == None
    assert cielo_customer.delivery_address == None


    # @test: create from json dict
    cielo_customer = CieloFactory.new_response_customer(CIELO_REQUEST_COMPLETE)
    assert cielo_customer.name == CIELO_REQUEST_COMPLETE['Customer']['Name']
    assert cielo_customer.email == CIELO_REQUEST_COMPLETE['Customer']['Email']
    assert cielo_customer.birth_date == CIELO_REQUEST_COMPLETE['Customer']['Birthdate']

    assert cielo_customer.address.street == CIELO_REQUEST_COMPLETE['Customer']['Address']['Street']
    assert cielo_customer.address.number == CIELO_REQUEST_COMPLETE['Customer']['Address']['Number']
    assert cielo_customer.address.complement == CIELO_REQUEST_COMPLETE['Customer']['Address']['Complement']
    assert cielo_customer.address.zip_code == CIELO_REQUEST_COMPLETE['Customer']['Address']['ZipCode']
    assert cielo_customer.address.city == CIELO_REQUEST_COMPLETE['Customer']['Address']['City']
    assert cielo_customer.address.state == CIELO_REQUEST_COMPLETE['Customer']['Address']['State']
    assert cielo_customer.address.country == CIELO_REQUEST_COMPLETE['Customer']['Address']['Country']

    assert cielo_customer.delivery_address.street == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['Street']
    assert cielo_customer.delivery_address.number == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['Number']
    assert cielo_customer.delivery_address.complement == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['Complement']
    assert cielo_customer.delivery_address.zip_code == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['ZipCode']
    assert cielo_customer.delivery_address.city == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['City']
    assert cielo_customer.delivery_address.state == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['State']
    assert cielo_customer.delivery_address.country == CIELO_REQUEST_COMPLETE['Customer']['DeliveryAddress']['Country']


def test_cielo_customer_address():
    STREET = 'rua da silva'
    NUMBER = '324'
    COMPLEMENT = 'casa'
    ZIPCODE = '378327482'
    CITY = 'uma cidade'
    STATE = 'um estado'
    COUNTRY = 'um pais'

    customer_address = CieloFactory.new_customer_address(street=STREET,
                                                         number=NUMBER,
                                                         complement=COMPLEMENT,
                                                         zip_code=ZIPCODE,
                                                         city=CITY,
                                                         state=STATE,
                                                         country=COUNTRY)

    assert customer_address.street == STREET
    assert customer_address.number == NUMBER
    assert customer_address.complement == COMPLEMENT
    assert customer_address.zip_code == ZIPCODE
    assert customer_address.city == CITY
    assert customer_address.state == STATE
    assert customer_address.country == COUNTRY


def test_cielo_credit_card_success():
    CARD_NUMBER = '4916663711012443'
    HOLDER = 'Jose da Silva'
    EXPIRATION_DATE = '01/2001'
    SECURITY_CODE = '134'
    BRAND = CieloCardBrand.Visa

    # @test: create from kwargs
    cielo_cc = CieloFactory.new_request_credit_card(card_number=CARD_NUMBER,
                                                       holder=HOLDER,
                                                       expiration_date=EXPIRATION_DATE,
                                                       security_code=SECURITY_CODE,
                                                       brand=BRAND)
    assert cielo_cc.card_number == CARD_NUMBER
    assert cielo_cc.holder == HOLDER
    assert cielo_cc.expiration_date == EXPIRATION_DATE
    assert cielo_cc.security_code == SECURITY_CODE
    assert cielo_cc.brand == BRAND
    assert cielo_cc.card_token == None
    assert cielo_cc.save_card == False


    # @test: create from json dict
    cielo_cc = CieloFactory.new_request_credit_card(cielo_data=CIELO_REQUEST_COMPLETE)
    assert cielo_cc.card_number == CIELO_REQUEST_COMPLETE["Payment"]["CreditCard"]["CardNumber"]
    assert cielo_cc.holder == CIELO_REQUEST_COMPLETE["Payment"]["CreditCard"]["Holder"]
    assert cielo_cc.expiration_date == CIELO_REQUEST_COMPLETE["Payment"]["CreditCard"]["ExpirationDate"]
    assert cielo_cc.security_code == CIELO_REQUEST_COMPLETE["Payment"]["CreditCard"]["SecurityCode"]
    assert cielo_cc.save_card == CIELO_REQUEST_COMPLETE["Payment"]["CreditCard"]["SaveCard"]
    assert cielo_cc.brand == CIELO_REQUEST_COMPLETE["Payment"]["CreditCard"]["Brand"]
    assert cielo_cc.card_token == None


def test_cielo_request_credit_card_error():
    CARD_NUMBER = '4916663711012443'
    HOLDER = 'Jose da Silva'
    EXPIRATION_DATE = '01/2001'
    SECURITY_CODE = '134'
    BRAND = CieloCardBrand.Visa


    with pytest.raises(ValidationError) as excinfo:
        # @test: invalid credit card
        CieloFactory.new_request_credit_card(card_number='21321321',
                                                holder=HOLDER,
                                                expiration_date=EXPIRATION_DATE,
                                                security_code=SECURITY_CODE,
                                                brand=BRAND)
    assert 'invalid card number' in excinfo.value


    # @test: missing attributes
    with pytest.raises(RequiredAttributeError) as excinfo:
        CieloFactory.new_request_credit_card(card_number=CARD_NUMBER,
                                                holder=HOLDER,
                                                expiration_date=EXPIRATION_DATE,
                                                security_code=SECURITY_CODE,
                                                brand=BRAND)
    assert 'holder' in excinfo.attributes
    assert 'expiration_date' in excinfo.attributes
    assert 'security_code' in excinfo.attributes
    assert 'brand' in excinfo.attributes


    # @test: missing attributes
    with pytest.raises(RequiredAttributeError) as excinfo:
        CieloFactory.new_request_credit_card(cielo_data={})
    assert 'card_number' in excinfo.attributes
    assert 'holder' in excinfo.attributes
    assert 'expiration_date' in excinfo.attributes
    assert 'security_code' in excinfo.attributes
    assert 'brand' in excinfo.attributes

    # @test: invalid date format in expiration date
    with pytest.raises(ValidationError) as excinfo:
        CieloFactory.new_request_credit_card(card_number=CARD_NUMBER,
                                             holder=HOLDER,
                                             expiration_date='3231/11',
                                             security_code=SECURITY_CODE,
                                             brand=BRAND)
    assert 'invalid expiration date' in excinfo.value

def test_cielo_response_credit_card_success():
    CARD_NUMBER = '4916663711012443'
    HOLDER = 'Jose da Silva'
    EXPIRATION_DATE = '01/2001'
    SECURITY_CODE = '134'
    BRAND = CieloCardBrand.Visa
    SAVE_CARD = True
    CARD_TOKEN = '6e1bf77a-b28b-4660-b14f-455e2a1c95e9'


    cielo_cc = CieloFactory.new_response_credit_card(card_number='21321****321',
                                                     holder=HOLDER,
                                                     expiration_date=EXPIRATION_DATE,
                                                     security_code=SECURITY_CODE,
                                                     brand=BRAND,
                                                     save_card=SAVE_CARD,
                                                     card_token=CARD_TOKEN)
    assert cielo_cc.card_number == CARD_NUMBER
    assert cielo_cc.holder == HOLDER
    assert cielo_cc.expiration_date == EXPIRATION_DATE
    assert cielo_cc.security_code == SECURITY_CODE
    assert cielo_cc.brand == BRAND
    assert cielo_cc.save_card == SAVE_CARD
    assert cielo_cc.card_token == CARD_TOKEN

    cielo_cc = CieloFactory.new_response_credit_card(cielo_data=CIELO_RESPONSE_COMPLETE)
    assert cielo_cc.card_number == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["CardNumber"]
    assert cielo_cc.holder == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Holder"]
    assert cielo_cc.expiration_date == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["ExpirationDate"]
    assert cielo_cc.brand == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Brand"]
    assert cielo_cc.save_card == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["SaveCard"]
    assert cielo_cc.security_code == None
    assert cielo_cc.card_token == None



def test_cielo_request_payment_success():
    cielo_cc = CieloFactory.new_request_credit_card(cielo_data=CIELO_REQUEST_COMPLETE)

    TYPE = CieloPaymentType.CreditCard
    AMOUNT = 332043
    INSTALLMENTS = 2
    PROVIDER = 'Jorge Portolo'

    cielo_payment = CieloFactory.new_request_payment(payment_type=TYPE,
                                                     amount=AMOUNT,
                                                     provider=PROVIDER,
                                                     installments=INSTALLMENTS,
                                                     credit_card=cielo_cc)
    assert cielo_payment.payment_type == TYPE
    assert cielo_payment.amount == AMOUNT
    assert cielo_payment.provider == PROVIDER
    assert cielo_payment.installments == INSTALLMENTS
    assert cielo_payment.credit_card == cielo_cc
    assert cielo_payment.service_tax_amount == 0
    assert cielo_payment.interest == None
    assert cielo_payment.capture == False
    assert cielo_payment.authenticate == False
    assert cielo_payment.soft_descriptor == None


    cielo_payment = CieloFactory.new_request_payment(cielo_data=CIELO_REQUEST_COMPLETE)
    assert cielo_payment.payment_type == CIELO_REQUEST_COMPLETE["Payment"]["Type"]
    assert cielo_payment.amount == CIELO_REQUEST_COMPLETE["Payment"]["Amount"]
    assert cielo_payment.provider == CIELO_REQUEST_COMPLETE["Payment"]["Provider"]
    assert cielo_payment.installments == CIELO_REQUEST_COMPLETE["Payment"]["Installments"]
    assert cielo_payment.credit_card.card_number == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["CardNumber"]
    assert cielo_payment.credit_card.holder == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Holder"]
    assert cielo_payment.credit_card.expiration_date == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["ExpirationDate"]
    assert cielo_payment.credit_card.brand == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Brand"]
    assert cielo_payment.credit_card.save_card == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["SaveCard"]
    assert cielo_payment.service_tax_amount == 0
    assert cielo_payment.interest == None
    assert cielo_payment.capture == False
    assert cielo_payment.authenticate == False
    assert cielo_payment.soft_descriptor == None


def test_cielo_request_payment_error():

    with pytest.raises(RequiredAttributeError) as excinfo:
        CieloFactory.new_request_payment()
    assert 'payment_type' in excinfo.attributes
    assert 'amount' in excinfo.attributes
    assert 'provider' in excinfo.attributes
    assert 'installments' in excinfo.attributes
    assert 'credit_card' in excinfo.attributes


    with pytest.raises(RequiredAttributeError) as excinfo:
        CieloFactory.new_request_payment(cielo_data={})
    assert 'payment_type' in excinfo.attributes
    assert 'amount' in excinfo.attributes
    assert 'provider' in excinfo.attributes
    assert 'installments' in excinfo.attributes
    assert 'credit_card' in excinfo.attributes



    cielo_cc = CieloFactory.new_request_credit_card(cielo_data=CIELO_REQUEST_COMPLETE)

    TYPE = CieloPaymentType.CreditCard
    AMOUNT = 332043
    INSTALLMENTS = 2
    PROVIDER = 'Jorge Portolo'

    # amount is not int
    with pytest.raises(TypeError) as excinfo:
        CieloFactory.new_request_payment(payment_type=TYPE,
                                            amount='asds',
                                            provider=PROVIDER,
                                            installments=INSTALLMENTS,
                                            credit_card=cielo_cc)
    assert 'amount is not int' in excinfo.value


    # type is not valid
    with pytest.raises(ValidationError) as excinfo:
        CieloFactory.new_request_payment(payment_type='xpto',
                                            amount=AMOUNT,
                                            provider=PROVIDER,
                                            installments=INSTALLMENTS,
                                            credit_card=cielo_cc)
    assert 'invalid payment type' in excinfo.value


    # type is not valid
    with pytest.raises(TypeError) as excinfo:
        CieloFactory.new_request_payment(payment_type=TYPE,
                                            amount=AMOUNT,
                                            provider=PROVIDER,
                                            installments=INSTALLMENTS,
                                            credit_card=0)
    assert 'invalid credit card object' in excinfo.value


def test_cielo_response_payment_success():
    cielo_cc = CieloFactory.new_response_credit_card(cielo_data=CIELO_RESPONSE_COMPLETE)

    TYPE = CieloPaymentType.CreditCard
    AMOUNT = 332043
    INSTALLMENTS = 2
    PROVIDER = 'Jorge Portolo'

    cielo_payment = CieloFactory.new_response_payment(payment_type=TYPE,
                                                      amount=AMOUNT,
                                                      provider=PROVIDER,
                                                      installments=INSTALLMENTS,
                                                      credit_card=cielo_cc)
    assert cielo_payment.payment_type == TYPE
    assert cielo_payment.amount == AMOUNT
    assert cielo_payment.provider == PROVIDER
    assert cielo_payment.installments == INSTALLMENTS
    assert cielo_payment.credit_card == cielo_cc
    assert cielo_payment.service_tax_amount == 0
    assert cielo_payment.interest == None
    assert cielo_payment.capture == False
    assert cielo_payment.authenticate == False
    assert cielo_payment.soft_descriptor == None
    assert cielo_payment.proof_of_sale == None
    assert cielo_payment.tid == None
    assert cielo_payment.authorization_code == None
    assert cielo_payment.payment_id == None
    assert cielo_payment.currency == None
    assert cielo_payment.country == None
    assert cielo_payment.extra_data_collection == []
    assert cielo_payment.status == -1
    assert cielo_payment.return_code == None
    assert cielo_payment.return_message == None
    assert cielo_payment.links == []


    # from json dict
    cielo_payment = CieloFactory.new_response_payment(cielo_data=CIELO_RESPONSE_COMPLETE)
    assert cielo_payment.payment_type == CIELO_REQUEST_COMPLETE["Payment"]["Type"]
    assert cielo_payment.amount == CIELO_REQUEST_COMPLETE["Payment"]["Amount"]
    assert cielo_payment.provider == CIELO_REQUEST_COMPLETE["Payment"]["Provider"]
    assert cielo_payment.installments == CIELO_REQUEST_COMPLETE["Payment"]["Installments"]
    assert cielo_payment.credit_card.card_number == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["CardNumber"]
    assert cielo_payment.credit_card.holder == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Holder"]
    assert cielo_payment.credit_card.expiration_date == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["ExpirationDate"]
    assert cielo_payment.credit_card.brand == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Brand"]
    assert cielo_payment.credit_card.save_card == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["SaveCard"]
    assert cielo_payment.service_tax_amount == CIELO_RESPONSE_COMPLETE["Payment"]["ServiceTaxAmount"]
    assert cielo_payment.interest == CIELO_RESPONSE_COMPLETE["Payment"]["Interest"]
    assert cielo_payment.capture == CIELO_RESPONSE_COMPLETE["Payment"]["Capture"]
    assert cielo_payment.authenticate == CIELO_RESPONSE_COMPLETE["Payment"]["Authenticate"]
    assert cielo_payment.soft_descriptor == CIELO_RESPONSE_COMPLETE["Payment"]["SoftDescriptor"]
    assert cielo_payment.proof_of_sale == CIELO_RESPONSE_COMPLETE["Payment"]["ProofOfSale"]
    assert cielo_payment.tid == CIELO_RESPONSE_COMPLETE["Payment"]["Tid"]
    assert cielo_payment.authorization_code == CIELO_RESPONSE_COMPLETE["Payment"]["AuthorizationCode"]
    assert cielo_payment.payment_id == CIELO_RESPONSE_COMPLETE["Payment"]["PaymentId"]
    assert cielo_payment.currency == CIELO_RESPONSE_COMPLETE["Payment"]["Currency"]
    assert cielo_payment.country == CIELO_RESPONSE_COMPLETE["Payment"]["Country"]
    assert cielo_payment.extra_data_collection == CIELO_RESPONSE_COMPLETE["Payment"]["DataCollection"]
    assert cielo_payment.status == CIELO_RESPONSE_COMPLETE["Payment"]["Status"]
    assert cielo_payment.return_code == CIELO_RESPONSE_COMPLETE["Payment"]["ReturnCode"]
    assert cielo_payment.return_message == CIELO_RESPONSE_COMPLETE["Payment"]["ReturnMessage"]
    assert cielo_payment.links == CIELO_RESPONSE_COMPLETE["Payment"]["Links"]

def test_cielo_payment_query_result():
    query_result = CieloFactory.new_payments_query_result(cielo_data=PAYMENTS_QUERY_RESULT)
    
    payment0 = query_result.payments[0]
    payment1 = query_result.payments[1]

    assert payment0.payment_id == PAYMENTS_QUERY_RESULT["Payments"][0]["PaymentId"]
    assert payment0.received_date == PAYMENTS_QUERY_RESULT["Payments"][0]["ReceivedDate"]

    assert payment1.payment_id == PAYMENTS_QUERY_RESULT["Payments"][1]["PaymentId"]
    assert payment1.received_date == PAYMENTS_QUERY_RESULT["Payments"][1]["ReceivedDate"]


def test_cielo_request():
    ORDER_ID = 'DAJD78Y2HEU8EY7HU'
    NAME = 'Test 1'
    cielo_customer = CieloFactory.new_request_customer(name=NAME)
    cielo_payment = CieloFactory.new_request_payment(cielo_data=CIELO_REQUEST_COMPLETE)
    cielo_request = CieloFactory.new_request(ORDER_ID, cielo_customer, cielo_payment)

    assert cielo_request.order_id == ORDER_ID
    assert cielo_request.customer == cielo_customer
    assert cielo_request.paument == cielo_payment

def test_cielo_response():
    ORDER_ID = 'DAJD78Y2HEU8EY7HU'
    cielo_customer = CieloFactory.new_response_customer(cielo_data=CIELO_RESPONSE_COMPLETE)
    cielo_payment = CieloFactory.new_response_payment(cielo_data=CIELO_RESPONSE_COMPLETE)
    cielo_response = CieloFactory.new_response(ORDER_ID, cielo_customer, cielo_payment)

    assert cielo_response.order_id == ORDER_ID
    assert cielo_response.customer == cielo_customer
    assert cielo_response.paument == cielo_payment


    cielo_response = CieloFactory.new_response(cielo_data=CIELO_RESPONSE_COMPLETE)

    assert cielo_response.order_id == CIELO_RESPONSE_COMPLETE['Customer']['MerchantOrderId']
    assert cielo_response.customer.name == CIELO_RESPONSE_COMPLETE['Customer']['Name']
    assert cielo_response.customer.email == CIELO_RESPONSE_COMPLETE['Customer']['Email']
    assert cielo_response.customer.birth_date == CIELO_RESPONSE_COMPLETE['Customer']['Birthdate']
    assert cielo_response.customer.identity == CIELO_RESPONSE_COMPLETE['Customer']['Identity']
    assert cielo_response.customer.identity_type == CIELO_RESPONSE_COMPLETE['Customer']['IdentityType']
    assert cielo_response.customer.address.street == CIELO_RESPONSE_COMPLETE['Customer']['Address']['Street']
    assert cielo_response.customer.address.number == CIELO_RESPONSE_COMPLETE['Customer']['Address']['Number']
    assert cielo_response.customer.address.complement == CIELO_RESPONSE_COMPLETE['Customer']['Address']['Complement']
    assert cielo_response.customer.address.zip_code == CIELO_RESPONSE_COMPLETE['Customer']['Address']['ZipCode']
    assert cielo_response.customer.address.city == CIELO_RESPONSE_COMPLETE['Customer']['Address']['City']
    assert cielo_response.customer.address.state == CIELO_RESPONSE_COMPLETE['Customer']['Address']['State']
    assert cielo_response.customer.address.country == CIELO_RESPONSE_COMPLETE['Customer']['Address']['Country']
    assert cielo_response.customer.delivery_address.street == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['Street']
    assert cielo_response.customer.delivery_address.number == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['Number']
    assert cielo_response.customer.delivery_address.complement == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['Complement']
    assert cielo_response.customer.delivery_address.zip_code == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['ZipCode']
    assert cielo_response.customer.delivery_address.city == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['City']
    assert cielo_response.customer.delivery_address.state == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['State']
    assert cielo_response.customer.delivery_address.country == CIELO_RESPONSE_COMPLETE['Customer']['DeliveryAddress']['Country']

    assert cielo_response.payment.payment_type == CIELO_RESPONSE_COMPLETE["Payment"]["Type"]
    assert cielo_response.payment.amount == CIELO_RESPONSE_COMPLETE["Payment"]["Amount"]
    assert cielo_response.payment.provider == CIELO_RESPONSE_COMPLETE["Payment"]["Provider"]
    assert cielo_response.payment.installments == CIELO_RESPONSE_COMPLETE["Payment"]["Installments"]
    assert cielo_response.payment.credit_card.card_number == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["CardNumber"]
    assert cielo_response.payment.credit_card.holder == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Holder"]
    assert cielo_response.payment.credit_card.expiration_date == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["ExpirationDate"]
    assert cielo_response.payment.credit_card.brand == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["Brand"]
    assert cielo_response.payment.credit_card.save_card == CIELO_RESPONSE_COMPLETE["Payment"]["CreditCard"]["SaveCard"]
    assert cielo_response.payment.service_tax_amount == CIELO_RESPONSE_COMPLETE["Payment"]["ServiceTaxAmount"]
    assert cielo_response.payment.interest == CIELO_RESPONSE_COMPLETE["Payment"]["Interest"]
    assert cielo_response.payment.capture == CIELO_RESPONSE_COMPLETE["Payment"]["Capture"]
    assert cielo_response.payment.authenticate == CIELO_RESPONSE_COMPLETE["Payment"]["Authenticate"]
    assert cielo_response.payment.soft_descriptor == CIELO_RESPONSE_COMPLETE["Payment"]["SoftDescriptor"]
    assert cielo_response.payment.proof_of_sale == CIELO_RESPONSE_COMPLETE["Payment"]["ProofOfSale"]
    assert cielo_response.payment.tid == CIELO_RESPONSE_COMPLETE["Payment"]["Tid"]
    assert cielo_response.payment.authorization_code == CIELO_RESPONSE_COMPLETE["Payment"]["AuthorizationCode"]
    assert cielo_response.payment.payment_id == CIELO_RESPONSE_COMPLETE["Payment"]["PaymentId"]
    assert cielo_response.payment.currency == CIELO_RESPONSE_COMPLETE["Payment"]["Currency"]
    assert cielo_response.payment.country == CIELO_RESPONSE_COMPLETE["Payment"]["Country"]
    assert cielo_response.payment.extra_data_collection == CIELO_RESPONSE_COMPLETE["Payment"]["DataCollection"]
    assert cielo_response.payment.payment.status == CIELO_RESPONSE_COMPLETE["Payment"]["Status"]
    assert cielo_response.payment.return_code == CIELO_RESPONSE_COMPLETE["Payment"]["ReturnCode"]
    assert cielo_response.payment.return_message == CIELO_RESPONSE_COMPLETE["Payment"]["ReturnMessage"]
    assert cielo_response.payment.links == CIELO_RESPONSE_COMPLETE["Payment"]["Links"]


def test_webservice():
    MERCHANT_ID = '12345'
    MERCHANT_KEY = '4567'
    cielo_ws = CieloFactory.new_webservice(merchant_id=MERCHANT_ID, merchant_key=MERCHANT_KEY)

    assert cielo_ws.merchant_id == MERCHANT_ID
    assert cielo_ws.merchant_key == MERCHANT_KEY
    assert cielo_ws.sandbox == False

