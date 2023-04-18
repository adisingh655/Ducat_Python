import database
cont=[]
counter=0
for i in database.cur:
    cont.append(i)
    counter+=1
    if counter==1:
        break
    
print(cont)
class Atm:
    def __init__(self):
        self.custmer_id=cont[0][0]
        self.card_number=cont[0][1]
        self.pin=cont[0][2]
        self.balance=cont[0][3]
        print(type(self.pin))
        print("Welcome to Kotak Mahindra Bank")
        a=input("Kindly enter your pin :")
        if a==self.pin:
            option=input("""
            Kindly choose one option:
            1.Withdrawal
            2.Change Pin
            3.Balance enquiry
            4.Kyc""")
            if option=="1":
                self.withdrawal()
            elif option=="2":
                self.change_pin()
            elif option=="3":
                self.balance_enquiry()
            elif option=="4":
                self.kyc()
            else:
                print("go to hell")
    def kyc(self):
        customerID=int(input("Enter your 10 digit mobile number:"))
        card_number=customerID
        pin_customer=input("enter your 4 digit pin:")
        balance_customer=float(input("Enter your bank balance: "))
        database.cur.execute(f"insert into banking values({customerID},{card_number},'{pin_customer}',{balance_customer})".format())
        database.cur.execute("commit")
    def withdrawal(self):
        pin2=input("Enter your pin to check withdrawal :")
        if pin2==self.pin:
            print("Kindly collect your cash")

        else:
            print("kindly enter a valid pin")
    def change_pin(self):

        print("welcome to change pin section ")
        cur.execute()
    
    def balance_enquiry(self):

        print("Welcome to balance enquiry section")


krishna=Atm()