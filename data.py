n = 8 #Number of companies

#Extracting Company names
def read_companies():
    f = open("Companies.txt","r")
    companies = []
    for i in range(n):
        x = f.readline().rstrip().split(",")
        for i in range(1,len(x)):
            x[i] = float(x[i])
        companies.append(x)

    f.close()
    return companies

#Extracting valid credentials
def read_cred():
    f = open("Usernames.txt","r")
    cred = {}
    data = f.readlines()
    for line in data:
        line = line.split(",")
        cred[line[0]] = line[1].rstrip()
    f.close()

    return cred

#Extracting buy requests
def buy_requests():
    f = open("BuyRequests.txt","r")
    requests = []
    data = f.readlines()
    for line in data:
        x = line.rstrip().split(",")
        requests.append(x)
    f.close()

    return requests

#Extracting sell requests
def sell_requests():
    f = open("SellRequests.txt","r")
    sell_requests = []
    data = f.readlines()
    for line in data:
        x = line.rstrip().split(",")
        sell_requests.append(x)
    f.close()

    return sell_requests

def store_companies(companies):
    f = open("Companies.txt","w")
    
    for line in companies: #Converting all items of list to strings
        for i in range(len(line)):
            line[i] = str(line[i])
            
    for line in companies: #Adding the data in the companies file
        f.write(','.join(line)+"\n")
        
    f.close()
