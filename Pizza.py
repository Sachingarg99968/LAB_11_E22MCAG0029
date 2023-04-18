#Sachin Garg
#E22MCAG0029
from abc import ABC
class Pizza(ABC):
    def __init__(self, basePrice):
        self.__basePrice = basePrice
    
    def get_price(self):
        return self.__basePrice

    def calculateCost(self):
       pass
    
    def displayDetails(self):
       pass


