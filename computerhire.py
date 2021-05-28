import datetime

class RentComputers:
    
    def __init__(self,stock=0):
        self.stock=stock
    def displaystock(self):
        return f"we currently have {self.stock} computers available"
    def rent_Hourly(self,a):

        if a > self.stock:
            return f"Sorry!! we currently have {self.stock} computerrs to hire"
    
        elif a <=0:
            return"sorry!! Invalid choice"

        else:
            current_time= datetime.datetime.now()
            print(f"you have hired {a} computers at on hourly basis {current_time.hour} ")
            print("you will be charged ksh200 per hour")
            print("I hope you enjoy our services")

            self.stock-=a
            

    def rent_Daily(self,a):

        if a > self.stock:
            return f"Sorry!! we currently have {self.stock} computerrs to hire"
    
        elif a <=0:
            return"sorry!! Invalid choice"

        else:
            current_time= datetime.datetime.now()
            print(f"you have hired {a} computers at on daily basis {current_time.hour()} ")
            print("you will be charged ksh 1500 per day")
            print("we hope you enjoy our service")
            self.stock-=a

    def rent_Weekly(self,a):
        if a > self.stock:
            return f"Sorry!! we currently have {self.stock} computerrs to hire"
    
        elif a <=0:
            return"sorry!! Invalid choice"

        else:
            current_time= datetime.datetime.now()
            print(f"you have hired {a} computers at weekly basis {current_time.hour()} ")
            print("you will be charged ksh 5000 per week")
            print("we hope you enjoy our service")
            self.stock-=a

    def return_computer(self,request):
        renttime,rentbasis,numofcomputers = request
        bill=0
        if renttime and rentbasis and numofcomputers:
            self.stock+=numofcomputers
            current_time=datetime.datetime.now()
            rentalperiod=current_time-renttime

            if rentbasis == 1:
                bill = round(rentalperiod.seconds/3600)*200*numofcomputers

            elif rentbasis == 2:
                bill = round(rentalperiod.days)*1500*numofcomputers

            elif rentbasis == 3:
                bill = round(rentalperiod.days/7)*5000*numofcomputers
            if(3<= numofcomputers <=5):
                print("you have qualified for our bulk rental promotion of 25percent discount")
                bill=bill*0.5

                print("thankyou for returning your computer")
                print("we heope you enjoyed our services")
                print(f"you bill is {bill}")

            else:
                print("looks like you did not rent a computer from us")

class Customer:
    def __init__(self):
        self.computers=0
        self.rentbasis=0
        self.rentaltime=0
        self.bill=0

    def request_Computers(self):

        computers=int(input("how many computers do you want?:"))

        if computers < 1:
            print("invalid! number of computers should be greater than 0")
            return-1
        else:
            self.computers=computers
            return self.computers

    def return_computer(self):
        if self.rentbasis and self.rentaltime and self.computers:
            return self.rentbasis,self.rentaltime,self.computers
        else:
            return 0,0,0


                
        






    




    


    





    

