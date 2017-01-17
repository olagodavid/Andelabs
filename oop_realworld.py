class Fees():
  def paid():
    pass
  
class Bankaccount(Ecobank):
  def __init__(self):
    self.balance = 10000
    
  
  def paid(self,paid):
    if type(paid) == int and paid !="":
      if deposit >= 0:
        self.balance += paid
        return self.balance

      else:
        return 'No money'

    else:
      raise ValueError()

 
