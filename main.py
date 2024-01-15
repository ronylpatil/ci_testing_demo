import sys
from exceptions import InvalidHeight, InvalidWeight, InputNotFound

def bmi(w, h) : 
     lower_height = 1.12
     upper_height = 1.80
     lower_weight = 25
     upper_weight = 170
     if h == 'None' and w == 'None' : 
          raise InputNotFound('Invalid input')
     elif h <  lower_height or h > upper_height : 
          raise InvalidHeight(f'Height must be in range {lower_height}-{upper_height} m')
     elif w < lower_weight or w > upper_weight :
          raise InvalidWeight(f'Weight must be in range {lower_weight}-{upper_weight} kg')
     else : 
          return  float('{:.2f}'.format((w / (h)**2)))


if __name__ == '__main__' : 
     if len(sys.argv) < 3 or len(sys.argv) > 3 :
          raise InputNotFound('Enter valid input')
     else :
          if sys.argv[1] == 'None' or sys.argv[2] == 'None' : 
               raise InputNotFound('Invalid inputs')
          else : 
               weight = float(sys.argv[1])
               height = float(sys.argv[2])
               print(bmi(weight, height))
