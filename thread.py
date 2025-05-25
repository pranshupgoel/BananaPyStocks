import threading 
import time
import random
from data import *

#Total company count
n = 8

count = 0
thr = [0 for i in range(n)]
companies = read_companies()

def simulation(): 
    global count
    global companies
    

    #Randimizing the addition and reduction of supplies 
    while True:
        companies = read_companies()
        
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
        time.sleep(5)
            

if __name__ == "__main__": 

    #Handling the threads
    for i in range(n):
        count = i
        thr[i] = threading.Thread(target=simulation)
        thr[i].start()
        time.sleep(5)
        
    for i in range(n):
        thr[i].join()