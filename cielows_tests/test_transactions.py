# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

from cielows.models import CieloFactory
from cielows.cielo import CieloWS
from cielows.constants import CieloCardBrand, CieloPaymentType,\
    CieloPaymentStatus, CieloPaymentReturnCode


def test_authorize_simple_transaction_success():

    '''
    Simple transaction authorization with success
    '''

    ORDER_ID = '391321U3H12'

    cielo_ws = CieloFactory.new_webservice(merchant_id='1234',
                                           merchant_key='4567',
                                           sandbox=True)

    cielo_customer = CieloFactory.new_request_customer(name="Jorge da Silva")

    cielo_cc = CieloFactory.new_request_credit_card(card_number='4916663711012443',
                                                    holder='Jose da silva',
                                                    expiration_date='13/2001',
                                                    security_code='213',
                                                    brand=CieloCardBrand.Visa)

    cielo_payment = CieloFactory.new_request_payment(type=CieloPaymentType.CreditCard,
                                                     amount=32240,
                                                     provider='Simulado',
                                                     installments=2,
                                                     credit_card=cielo_cc)

    # autoriza
    cielo_auth_response = cielo_ws.authorize(order_id=ORDER_ID,
                                             customer=cielo_customer,
                                             payment=cielo_payment)

    assert cielo_auth_response.payment.status == CieloPaymentStatus.Authorized
    assert cielo_auth_response.payment.return_code == CieloPaymentReturnCode.OperationSuccessful


    # captura
    cielo_capture_response = cielo_ws.capture(payment_id=cielo_auth_response.payment.payment_id,
                                              amount=321312,
                                              service_tax_amount=0)
    assert cielo_capture_response.status == CieloPaymentStatus.PaymentConfirmed


    # cancela
    cielo_cancel_response = cielo_ws.cancel(payment_id=cielo_auth_response.payment.payment_id,
                                            amount=321312)
    assert cielo_cancel_response.status == CieloPaymentStatus.Voided

    # consulta
    query_response = cielo_ws.fetch_payment(payment_id=cielo_auth_response.payment.payment_id)
    assert query_response.order_id == ORDER_ID

    # consulta vendas
    payments_response = cielo_ws.fetch_payments(order_id=ORDER_ID)
    assert len(payments_response.payments) == 1

