#Sachin Garg
#E22MCAG0029
from GreekPizza import *
from ChicagoPizza import *
from NewYorkStylePizza import *
from SicillianPizza import *
from MozzarellaChesse import *
from ParmesanChesse import *
from ProvoloneChesse import *
from RegiannoChesse import *
from PlumTomatoSause import *
from PumpkinSauce import *
from MarinaraSauce import *
from BarbecueSauce import *
from ThinCrustDough import *
from ThickCrustDough import *
from Pizza import *
from Cheese import *
from abc import ABC

tot_cost=0
doughP,cheese_cost,pizza_price,sauceP=0,0,0,0
cost=0

def calculateCost(res1):
    global tot_cost
    tot_cost+=res1

def displayDetails(price):
    global cost
    cost=price
    return f"Pizza price total: {cost}"

def dough():
    global doughP
    print("1. Thin Crust Dough")
    print("2. Thick Crust Dough")
    d=int(input("Enter your choice: "))
    if(d==1):
        do=ThinCrustDough(300)
        doughP=do.get_price()
        calculateCost(doughP)
    elif(d==2):
        do=ThickCrustDough(200)
        doughP=do.get_price()
        calculateCost(doughP)
    else:
        print("Invalid input!!")

def sauce():
    global sauceP
    print("1. Plum Tomato Sause")
    print("2. Pumpkin Sause")
    print("3. Marinara Sauce")
    print("4. Barbecue Sauce")
    s=int(input("Enter your choice: "))
    if(s==1):
        sa=PlumTomatoSauce(100)
        dough()
        sauceP=sa.get_price()
        calculateCost(sauceP)
    elif(s==2):
        sa=PumpkinSauce(50)
        dough()
        sauceP=sa.get_price()
        calculateCost(sauceP)
    elif(s==3):
        sa= MarinaraSause(140)
        dough()
        sauceP=sa.get_price()
        calculateCost(sauceP)
    elif(s==4):
        sa= BarbecueSauce(90)
        dough()
        sauceP=sa.get_price()
        calculateCost(sauceP)
    else:
        print("Invalid input!!")
    
def cheese():
    global cheese_cost
    print("1. Mozzarella Chesse")
    print("2. Provolone Chesse")
    print("3. ParmesanChesse")
    print("4. Regianno Chesse")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        che= MozzarellaChesse(190)
        cheese_cost=che.get_price()
        sauce()
        return calculateCost(cheese_cost)
    elif(ch==2):
        che= ParmesanChesse(150)
        cheese_cost=che.get_price()
        sauce()
        return calculateCost(cheese_cost)
    elif(ch==3):
        che= ProvoloneChesse(100)
        cheese_cost=che.get_price()
        sauce()
        return calculateCost(cheese_cost)
    elif(ch==4):
        che= RegiannoChesse(150)
        cheese_cost=che.get_price()
        sauce()
        return calculateCost(cheese_cost)
    else:
        print("Invalid input!!")

def main():
    global pizza_price
    print("1. Greek Pizza")
    print("2. Chicago Pizza")
    print("3. New York Style Pizza")
    print("4. Sicillian Pizza")
    p=int(input("Enter your choice: "))
    if(p==1):
        pi= GreekPizza(250)
        pizza_price=pi.get_price()
        cheese()
        calculateCost(pizza_price)
    elif(p==2):
        pi= ChicagoPizza(500)
        pizza_price=pi.get_price()
        cheese()
        calculateCost(pizza_price)
    elif(p==3):
        pi= NewYorkStylePizza(260)
        pizza_price=pi.get_price()
        cheese()
        calculateCost(pizza_price)
    elif(p==4):
        pi= SicillianPizza(350)
        pizza_price=pi.get_price()
        cheese()
        calculateCost(pizza_price)
    else:
        print("Invalid input!!")

main()
ms=displayDetails(tot_cost)
print(ms)