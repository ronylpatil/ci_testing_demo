import pytest
from main import bmi
from exceptions import *

test_cases = {
     'incor1' : {
          'weight' : 24,    # incor. wt
          'height' : 1.17    # correct ht
     },

     'incor2' : {
          'weight' : -1,
          'height' : 00
     },

     'incor3' : {
          'weight' : 70,    # cor
          'height' : 500    # incor
     },

     'cor1' : {
          'weight' : 30,    
          'height' :  1.16   
     },

     'incor4': {
          'weight' : 'None',
          'height' : 'None'
     }     
}

op_range = {
     'min' : 13,
     'max' : 40
}

# params = test_cases['cor1']
# print(params)
# print(bmi(params['weight'], params['height']))

def test_invalid_weight() : 
     params = test_cases['incor1']
     # match = 'Weight must be in range'
     # we can also pass error message, it will give us more control over the assertion on the exp.
     with pytest.raises(InvalidWeight) : 
          bmi(params['weight'], params['height'])

def test_both_invalid() : 
     params = test_cases['incor2']
     with pytest.raises((InvalidHeight, InvalidWeight)) : 
          bmi(params['weight'], params['height'])

def test_invalid_height() : 
     params = test_cases['incor3']
     with pytest.raises(InvalidHeight) : 
          bmi(params['weight'], params['height'])

def test_valid_inputs() : 
     params = test_cases['cor1']
     assert op_range['min'] <= bmi(params['weight'], params['height']) <= op_range['max']

def test_both_none() : 
     params = test_cases['incor4']
     with pytest.raises(InputNotFound) : 
          bmi(params['weight'], params['height'])
