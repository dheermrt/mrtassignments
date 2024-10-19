nall=[[1,'quattro','ferrari','1999',1000,True,'Supercharged',0],[2,'q','Nissan','1989',1000,False,'turbocharged',4]]
customerinfo=[[1,'John',121,[1,1],0,'regular'],[2,'james',123,[1],0,'regular']]   
from datetime import date,datetime,timedelta
from time import sleep
import multiprocessing


class Vehicle:
    vehicle_type='Car'
     
    
    def __init__(self,vehicleid,make,model,year,rental_rate,availability):
        self.vehicleid=vehicleid
        self.make=make
        self.model=model
        self.year=year
        self.rental_rate=rental_rate
        self.availability=availability
         
    def printer(self):
        vehiclelist=[self.vehicleid,self.make,self.model,self.year,self.rental_rate]
        if(self.availability==True):
            vehiclelist.append('True')
        else:
            vehiclelist.append('False')
        return vehiclelist
    
          
    def renter(customer_id,rental_duration):
        t=int(input("Enter vehicle id you want to check"))
        for i in nall:
            if(i[0]==t):

              
             if(i[5]==True):
                print('Available')
                i[5]=False
                for t in customerinfo:
                    if(t==customer_id):
                        t[3].append(i[0])
                        t[4]=t[4]+1
                    if(t[5]=='premium'):
                        print('For you the rental rate =',0.9*i[4])

             else:
                print('Not Available')
            else:
                print('Vehicle not in inventory')
            
    def returnvehicle():
        m=int(input('Enter your customer id'))
        t=int(input("Enter Vehicle id you want to return"))
        c=0
        for i in nall:
         for j in customerinfo:
            if(j[3][len(j[3])-1]==i[0]):

         
             if(i[0]==t):
                c=1
                if(i[5]==True):
                    print('Vehicle already returned')
                else:
                    print('Thank you for returning vehicle')
        if(c==0):
            print('You did not rent this vehicle you cannot return it')   
class LuxuryVehicle(Vehicle):
    def __init__(self,extra_features):
        self.extra_features=extra_features
    def ins():
        for i in nall:
            if(i[6]!='none'):
                i[4]=i[4]*1.2
        print('The new rental rate =',i[4])
        print('The extra feature is',i[6])
class Customer():
    def __init__(self,customer_id,name,contact_info,rental_history,royaltypoints,customertype):
        self.customer_id=customer_id
        self.name=name
        self.contact_info=contact_info
        self.rental_history=rental_history
        self.royaltypoints=royaltypoints
        self.customertype=customertype
    def printer(self):
        customerinfo=[self.customer_id,self.name,self.contact_info,self.rental_history]
        print('Rental history  is')
        for i in self.rental_history:
            print(i)
        return customerinfo
    def registercustomer():
        t=[]
        t.append(int(input('Enter customer id')))
        t.append(input('Enter your name'))
        t.append(int(input('Enter your contact info')))
        t.append([])
        t.append([])
        t.append('regular')
        customerinfo.append(t)
    def returncustomerdetails():
        r =(input('Please Enter your name'))
        c=0
        for i in customerinfo:
            if(i[1]==r):
                c=1
                for u in i:
                    print(u)
        if(c==0):
            print('You are not a old customer\n')
            t=int(input('Press 1 to continue and register with us \n press 2 to exit'))
            if(t==1):
                Customer.registercustomer()
            elif(t==2):
                return
            else:
                print('Please enter valid output')
            
class PremiumCustomer(Customer):
    for i in customerinfo:
        if (i[4]>=5) :
             i[5]='premium'
class RentalManager():
    def printavailablevehicles():
        for i in nall:
            if (i[5]== True):
                for t in range(0,5):
                    print(i[t])
                 
                if(i[6]!='none'):
                    LuxuryVehicle.ins()                    
    def addnewvehicles():
        u=[]
         
         
        u.append(int(input('Enter vehicle id')))
        u.append(input('Enter make'))
        u.append(input('Enter model'))
        u.append(int(input('Enter year')))
        u.append(int(input('Enter rental_rate')))
        u.append(True)
        u.append(input('Enter luxury features if any type none if no extra features'))
        u.append(0) #for rental duration which is set by default to 0
        nall.append(u)         
    def removevehicles():
        c=0
        t=int(input('Enter vehicle id you want to remove'))
        for i in nall:
            if(i[0]==t and i[5]==True):
                print('The removed Vehicle details are')
                for a in i:
                    print(a)
                nall.remove(i)
                c=1
                break
        if (c==0):
            print('The vehicle is already rented out or is not in the inventory')
    def rentedout():
        
        for i in nall:
            if(i[5]==False):
                for a in i:
                    print(a,end =" ")
                print("\n")
                for a in customerinfo: 
                    if((a[3])[len(a[3])-1]== i[0]):
                        for t in a:
                            print(t,end=" ")
    def bookvehicle():
        c=0
        y=input('Enter the vehicle model you want to prebook')
        for i in nall:
            c=1
            if(i[2]==y):
                n1=int(input('After how many days you want to pick up the new vehicle'))
                n2=int(input('For how long do you want to pick up the new vehicle'))
                if((n1-i[7]>0)):
                    print('The vehicle is prebooked for you')
                    i[7]=i[7]+n1+n2
                else:
                    print('Vehicle not available')
        if(c==0):
            print('This vehicle does not exist in our inventory')
 
class SearchVehicles():
     
    def printsortedlist():
        t=int(input('press 1 if you want to search based on model \n press 2 if you want to search based on rental rate range \n press 3 if you want to sort based on availability status'))
        if(t==1):
            y=input('Enter model you want to search')
            sorted=[]
             
            for i in nall:
                if(i[2]==y):
                     
                    sorted.append(i)
            for i in range (0,len(sorted)):
                for j in range(i+1,len(sorted)):
                    if(sorted[i][0]>sorted[j][0]):
                        sorted[i],sorted[j]=sorted[j],sorted[i]
            if(len(sorted)==0):
              print('No such model found')
            else:
             for i in sorted:
                print(i,'\n')


        elif(t==2):
            sorted=[]
            lowerrange=int(input('Enter lower range of rent rate'))
            higherrange=int(input('Enter upper range of rent rate'))
            for i in nall:
                if(i[4] in range(lowerrange,higherrange+1)):
                    sorted.append(i)
            for i in range (0,len(sorted)):
                for j in range(i+1,len(sorted)):
                    if(sorted[i][0]>sorted[j][0]):
                        sorted[i],sorted[j]=sorted[j],sorted[i]
            if(len(sorted)==0):
              print('No vehicle is present in your rent range')
            else:
             for i in sorted:
                print(i,'\n')
            


        elif(t==3):
            RentalManager.printavailablevehicles()
        else:
            print('Please choose a valid input')
                

 
class userinterface():
    def choose():
        y=int(input('Press 1 if you are a Employee, press 2 if you are a customer'))
        if(y==1):
            t=int(input('Press1  if you want to remove a vehicle \n press2 if you want to add a vehicle \n press 3 if you want to view all rented out vehicles'))
            if(t==1):
                RentalManager.removevehicles()
            elif(t==2):
                RentalManager.addnewvehicles()
            elif(t==3):
                RentalManager.rentedout()
            else:
                print('Please choose a valid option')
        elif (y==2):
            t=int(input('Press 1 if you are a new customer \n Press 2 if you are a old customer  '))
            if(t==1):
                Customer.registercustomer()
            elif(t==2):
                y=int(input('Press 1 if you want to view your history \n Press 2 if you want to return a vehicle \n Press 3 if you want to rent a vehicle \n Press 4 if you want to view available vehicles \n Press 5 if you want to check availability and prebook a vehicle\n Press 6 if you want to Search vehicles based on given parameters'))
                if(y==1):
                    Customer.returncustomerdetails()
                elif(y==2):
                    Vehicle.returnvehicle()
                elif(y==3):
                    
                    Vehicle.renter(int(input('Enter your customer id')),int(input('Enter rental duration')))
                elif(y==4):
                    RentalManager.printavailablevehicles()
                elif(y==5):
                    RentalManager.bookvehicle()
                elif(y==6):
                    SearchVehicles.printsortedlist()
                else:
                    print('Please choose the correct option')
def notificationalert():
    for i in nall:
        if(i[5]==False and i[7]<5):
            for j in customerinfo:
                if(j[3][len(j[3])-1]==i[0]):
                    print(j[1],'Your rental duration is going to end soon')
userinterface.choose()
notificationalert()
     
  



           
                 
                

             
     
   
    





                        





        
 
 






                 
            
 
            

    



             
            


   
 

        