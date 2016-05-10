# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

def test_authorize_simple_transaction_success():
    '''
    Simple transaction authorization success
    '''
    cielo_ws = CieloWS(MerchantId='1234', MerchantKey='4567')
    
    cielo_customer = CieloCustomer(name="Jorge da Silva")

    cielo_cc = CieloCreditCard(card_number='31382173821',
                               holder='Jose da silva',
                               expiration_date='13/2001',
                               security_code='213',
                               brand=CieloBrand.Visa)

    cielo_payment = CieloRequestPayment(type=PaymentType.CreditCard,
                                        amount=32240,
                                        provider='Silumado',
                                        installments=2,
                                        credit_card=)
 
    cielo_response = cielo_ws.authorize(order_id="HDYQWD78218J131D",
                                        customer=cielo_customer,
                                        payment=cielo_payment)

    assert cielo_response.payment.status == CieloPaymentStatus.Authorized
    assert cielo_response.payment.return_code == CieloPaymentReturnCode.OperationSuccessful

