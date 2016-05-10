# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

def test_cielo_customer():
    NAME = "Jorge da Silva"
    cielo_customer = CieloCustomer(name=NAME)
    assert cielo_customer.name == NAME

def test_cielo_credit_card():
    CARD_NUMBER = '4916663711012443'
    HOLDER = 'Jose da Silva'
    EXPIRATION_DATA = '01/2001'
    SECURITY_CODE = '134'
    BRAND = CieloCardBrand.Visa

    cielo_cc = CieloCreditCard(card_number=CARD_NUMBER,
                               holder=HOLDER,
                               expiration_date=EXPIRATION_DATE,
                               security_code=SECURITY_CODE,
                               brand=BRAND)

    assert cielo_cc.card_number == CARD_NUMBER
    assert cielo_cc.holder == HOLDER
    assert cielo_cc.expiration_date == EXPIRATION_DATE
    assert cielo_cc.security_code == SECURITY_CODE
    assert cielo_cc.brand = BRAND


def test_cielo_request_payment():
    CARD_NUMBER = '4916663711012443'
    HOLDER = 'Jose da Silva'
    EXPIRATION_DATA = '01/2001'
    SECURITY_CODE = '134'
    BRAND = CieloCardBrand.Visa

    cielo_cc = CieloCreditCard(card_number=CARD_NUMBER,
                               holder=HOLDER,
                               expiration_date=EXPIRATION_DATE,
                               security_code=SECURITY_CODE,
                               brand=BRAND)


    TYPE = PaymentType.CreditCard
    AMOUNT = 332043
    INSTALLMENTS = 2
    PROVIDER = 'Jorge Portolo'

    cielo_payment = CieloRequestPayment(payment_type=TYPE,
                                        amount=AMOUNT,
                                        provider=PROVIDER,
                                        installments=INSTALLMENTS,
                                        credit_card=cielo_cc)

    assert cielo_payment.payment_type == TYPE
    assert cielo_payment.amount == AMOUNT
    assert cielo_payment.provider == PROVIDER
    assert cielo_payment.installments == INSTALLMENTS
    assert cielo_payment.credit_card == cielo_cc

def test_cielo_response_payment():
    pass

def test_cielo_response():
    pass

def test_cielo_request():
    pass

