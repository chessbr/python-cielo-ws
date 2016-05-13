
# -*- coding: utf-8 -*-
# This file is part of Python Cielo Webservice.
#
# Copyright (c) 2016, Rockho Team. All rights reserved.
# Author: Christian Hess
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

from cielows.utils import validate_cc

def test_validate_cc():
    # Visa
    assert validate_cc('4539696011571731') == True
    assert validate_cc('4824449019263420') == True
    assert validate_cc('4485157518938000') == True
    assert validate_cc('4413560587130028') == True
    assert validate_cc('4539670615108786') == True
    assert validate_cc('4537812738173812') == False # invalid
    assert validate_cc('4391289189189191') == False # invalid
    assert validate_cc('4583983383395895') == False # invalid

    # Mastercard
    assert validate_cc('5511953211524302') == True
    assert validate_cc('5330143760876266') == True
    assert validate_cc('5344020126000993') == True
    assert validate_cc('5388628000508308') == True
    assert validate_cc('5839123912839128') == False # invalid
    assert validate_cc('5019021902938229') == False # invalid

    # Discover
    assert validate_cc('6011294481664517') == True
    assert validate_cc('6011315737906673') == True
    assert validate_cc('6011854462949680') == True
    assert validate_cc('6011980888821193') == True
    assert validate_cc('6318398129319819') == False # invalid
    assert validate_cc('6391301283839282') == False # invalid

    # Amex
    assert validate_cc('342598853898955') == True
    assert validate_cc('343997784676457') == True
    assert validate_cc('376983503268081') == True
    assert validate_cc('349469664661441') == True
    assert validate_cc('395495849859485') == False # invalid
    assert validate_cc('375485847584758') == False # invalid

    # JCB
    assert validate_cc('3530111333300000') == True
    assert validate_cc('3518918918171722') == False # invalid

    # Diners
    assert validate_cc('30569309025904') == True
    assert validate_cc('30569197327327') == False # invalid

    # Elo
    assert validate_cc('6362970000457013') == True
    assert validate_cc('6362970000457013') == True
    assert validate_cc('6362187584575484') == False # invalid

    # Hiper
    assert validate_cc('3841001111222233334') == True
    assert validate_cc('3841001111232367236') == False # invalid

