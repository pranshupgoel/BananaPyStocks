import threading 
import time
import random
from data import *

#Total company count
n = 8

count = 1
companies = read_companies()
l = [0,1,2,3,4,5,6,7]

def simulation(): 
    global count
    global companies
    global l
    

    #Randimizing the addition and reduction of supplies 
    while True:
        companies = read_companies()
        count = random.choice(l)
        l.remove(count)
        
        x = round(random.random()*random.choice([2,-2]),2)
        
        prev = companies[count][2]
        curr = prev + x
        
        companies[count][1], companies[count][2] = round(prev,2), round(curr,2) 
        
        companies[count][3] = round(((curr-prev)*100)/prev, 2) #Fluctuation
        
        if companies[count][4] < curr:  #Highest
            companies[count][4] = round(curr,2)
            
        if companies[count][5] > curr:  #Lowest
            companies[count][5] = round(curr,2)
        
        store_companies(companies)
        if len(l) == 0:
            l = [0,1,2,3,4,5,6,7]
            time.sleep(5)
            
simulation()