import sys
from exceptions import InvalidHeight, InvalidWeight, InputNotFound

def bmi(w, h) : 
     lower_height = 100
     upper_height = 192
     lower_weight = 25
     upper_weight = 170
     if h <  lower_height or h > upper_height : 
          raise InvalidHeight(f'Height must be in range {lower_height}-{upper_height}')
     elif w < lower_weight or w > upper_weight :
          raise InvalidWeight(f'Weight must be in range {lower_weight}-{upper_weight}')
     else : 
          return  (w / (h)**2)


if __name__ == '__main__' : 
     if len(sys.argv) < 3 or len(sys.argv) > 3 : 
          raise InputNotFound('Input not found')
     else :
          weight = int(sys.argv[1])
          height = int(sys.argv[2])
          bmi()

