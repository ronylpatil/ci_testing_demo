
class InvalidHeight(Exception) : 
     def __init__(self, arg) :
          self.message = arg
          super().__init__(arg)

class InvalidWeight(Exception) : 
     def __init__(self, arg) :
          self.message = arg
          super().__init__(arg)
 
class InputNotFound(Exception) : 
     def __init__(self, arg) :
          self.message = arg
          super().__init__(arg)