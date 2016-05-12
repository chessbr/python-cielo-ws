# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.


class CieloPaymentType(object):
    CreditCard = "CreditCard"


class CieloCardBrand(object):
    Visa = "Visa"
    Mastercard = "Mastercard"
    Amex = "Amex"
    Elo = "Elo"
    Auria = "Auria"
    JCB = "JCB"
    Diners = "Diners"
    Discover = "Discover"


class CieloPaymentInterest(object):
    ByMerchant = "ByMerchant"


class CieloPaymentReturnCode(object):
    OperationSuccessful = '4'
    NotAuthorized = '2'
    ProblemsWithCreditCard = '70'
    CanceledCreditCard = '77'
    BlockedCreditCard = '78'
    ExpiredCreditCard = '57'
    TimeOut = '99'


class CieloPaymentStatus(object):
    NotFinished = 0
    Authorized = 1
    PaymentConfirmed = 2
    Denied = 3
    Voided = 10
    Refunded = 11
    Pending = 12
    Aborted = 13
    Scheduled = 20


class CieloCurrency(object):
    BRL = "BRL"
    USD = "USD"
    MXN = "MXN"
    COP = "COP"
    CLP = "CLP"
    ARS = "ARS"
    PEN = "PEN"
    EUR = "EUR"
    PYN = "PYN"
    UYU = "UYU"
    VEB = "VEB"
    VEF = "VEF"
    GBP = "GBP"


CieloErrorsMap = {
    '100': 'RequestId is required',
    '101': 'MerchantId is required',
    '102': 'Payment Type is required',
    '103': 'Payment Type can only contain letters',
    '104': 'Customer Identity is required',
    '105': 'Customer Name is required',
    '106': 'Transaction ID is required',
    '107': 'You must provide CreditCard Number, Token or Alias',
    '108': 'Amount must be greater or equal to zero',
    '109': 'Payment Currency is required',
    '110': 'Invalid Payment Currency',
    '111': 'Payment Country is required',
    '112': 'Invalid Payment Country',
    '113': 'Invalid Payment Code',
    '114': 'The provided MerchantId is not in correct format',
    '115': 'The provided MerchantId was not found',
    '117': 'Credit Card Holder is required',
    '118': 'Credit Card Number is required',
    '119': 'At least one Payment is required',
    '120': 'Request IP not allowed. Check your IP White List',
    '121': 'Customer is required',
    '122': 'MerchantOrderId is required',
    '123': 'Installments must be greater or equal to one',
    '124': 'Credit Card is Required',
    '125': 'Credit Card Expiration Date is required',
    '126': 'Credit Card Expiration Date is invalid',
    '127': 'You must provide CreditCard Number, Token or Alias',
    '128': 'Card Number length exceeded',
    '129': 'Affiliation not found',
    '130': 'Could not get Credit Card',
    '131': 'MerchantKey is required',
    '132': 'MerchantKey is invalid',
    '133': 'Provider is not supported for this Payment Type',
    '134': 'FingerPrint length exceeded',
    '135': 'MerchantDefinedFieldValue length exceeded',
    '136': 'ItemDataName length exceeded',
    '137': 'ItemDataSKU length exceeded',
    '138': 'PassengerDataName length exceeded',
    '139': 'PassengerDataStatus length exceeded',
    '140': 'PassengerDataEmail length exceeded',
    '141': 'PassengerDataPhone length exceeded',
    '142': 'TravelDataRoute length exceeded',
    '143': 'TravelDataJourneyType length exceeded',
    '144': 'TravelLegDataDestination length exceeded',
    '145': 'TravelLegDataOrigin length exceeded',
    '146': 'SecurityCode length exceeded',
    '147': 'Address Street length exceeded',
    '148': 'Address Number length exceeded',
    '149': 'Address Complement length exceeded',
    '150': 'Address ZipCode length exceeded',
    '151': 'Address City length exceeded',
    '152': 'Address State length exceeded',
    '153': 'Address Country length exceeded',
    '154': 'Address District length exceeded',
    '155': 'Customer Name length exceeded',
    '156': 'Customer Identity length exceeded',
    '157': 'Customer IdentityType length exceeded',
    '158': 'Customer Email length exceeded',
    '159': 'ExtraData Name length exceeded',
    '160': 'ExtraData Value length exceeded',
    '161': 'Boleto Instructions length exceeded',
    '162': 'Boleto Demostrative length exceeded',
    '163': 'Return Url is required',
    '164': 'Return Url is invalid',
    '166': 'AuthorizeNow is required',
    '167': 'Antifraud not configured',
    '168': 'Recurrent Payment not found',
    '169': 'Recurrent Payment is not active',
    '300': 'MerchantId was not found',
    '301': 'Request IP is not allowed',
    '302': 'Sent MerchantOrderId is duplicated',
    '303': 'Sent OrderId does not exist',
    '304': 'Customer Identity is required',
    '306': 'Merchant is blocked',
    '307': 'Transaction not found',
    '308': 'Transaction not available to capture',
    '309': 'Transaction not available to void',
    '310': 'Payment method doest not support this operation',
    '311': 'Refund is not enabled for this merchant',
    '312': 'Transaction not available to refund',
    '313': 'Recurrent Payment not found',
    '314': 'Invalid Integration',
    '315': 'Cannot change NextRecurrency with pending payment'
}
