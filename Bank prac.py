class Account():

    def __init__(self,balance):
        self.balance = balance

    def getbalance(self):
        return self.balance

    def deposit(self,amt):
        if amt < 0:
            return False
        else:
            self.balance += amt
            return True

    def withdraw(self,amt):
        if self.balance < amt:
            return False
        else:
            self.balance -= amt
            return True
class Customer():

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.account = firstname + lastname
        self.accountlist = []
        self.straccountlist =[]
    def getaccountlist(self):
        return self.accountlist
    def getFirstName(self):
        return self.firstname
    def getLastName(self):
        return self.lastname
    def getAccount(self,index):
        return self.accountlist[index]
    def getallaccount(self):
        return self.straccountlist
    def setAccount(self,balance,name):
        self.accountlist.append(Account(balance))
        self.straccountlist.append(name)

class Bank():
    noOfCustomers = 0
    def __init__(self,bname):
        self.bname = bname
        self.customerlist = []
        self.strcustomerlist =[]

    def addCustomer(self,f,l):
        self.customer= str(f)+  " " +str(l)
        self.strcustomerlist.append(self.customer)
        self.customerlist.append(Customer(f,l))
    def getNumOfCustomer(self):
        return self.customerlist.count()
    def getcustomerlist(self):
        return self.strcustomerlist
    def getCustomer(self,index):
        customer = self.customerlist[index]
        return customer


def main():
    strBankList = []
    bankList = []
    StatusA = "Y"
    statusB ="Y"
    statusC = "Y"
    exit = "y"
    while exit.upper() != "N":
        exit = str(input("do you want to use atm Y/N "))
        choice = int(input("Choose 1 access a new bank, choose 2 to access an existing bank "))
        if choice == 1:
            bankname = str(input("please input name of bank "))
            strBankList.append(bankname)
            bankList.append(Bank(bankname))
        elif choice == 2:
            print(strBankList)
            indexValue = int(input("please put the index of the bank you want to access "))
            while statusB.upper() != "N":
                choice = int(input("choose 1 to add a new customer, choose 2 to access an existing customer "))
                bank = bankList[indexValue]
                if choice == 1:
                    firstname = str(input("fill in first name of the account "))
                    lastname = str(input("fill in last name of the account "))
                    bank.addCustomer(firstname,lastname)
                elif choice == 2:
                    print(bank.getcustomerlist())
                    index = int(input("please put the index of the Customer you want to access "))
                    while statusC.upper() != "N":
                        choice = int(input("Choose 1 to make a new account, choose 2 to use an existing account "))
                        if choice == 1:
                            initialDeposit = int(input("please input initial deposit "))
                            accountname = str(input("please type the name of the account"))
                            bank.getCustomer(index).setAccount(initialDeposit,accountname)
                        elif choice == 2:
                            print(bank.getCustomer(index).getallaccount())
                            account_index = int(input("please put the index of the account you want to access "))
                            while StatusA.upper() != "N":
                                optionChoice = int(input("Choose 1 to display balance, choose 2 to input deposit, choose 3 to withdraw deposit"))
                                if optionChoice == 1:
                                    print(bank.getCustomer(index).getAccount(account_index).getbalance())
                                elif optionChoice == 2:
                                    amt = int(input("what is the amount you want to put "))
                                    result = bank.getCustomer(index).getAccount(account_index).deposit(amt)
                                    if result == False:
                                        print("don't put in your debt")
                                    elif result == True:
                                        print(bank.getCustomer(index).getAccount(account_index).getbalance())
                                elif optionChoice == 3:
                                    amt = int(input("what is the amount you want to take "))
                                    result = bank.getCustomer(index).getAccount(account_index).withdraw(amt)
                                    if result == False:
                                        print("u too poor ")
                                    elif result == True:
                                        print(bank.getCustomer(index).getAccount(account_index).getbalance())
                                StatusA = str(input("do you still want to stay with this account Y/N"))
                        statusC = str(input("do you still want to stay with this customer Y/N"))
                statusB = str(input("Are you staying with this Bank? Y/N"))

    # firstname = str(input("fill in first name of the account"))
    # lastname = str(input("fill in last name of the account"))
    # bankname = str(input("please input name of bank"))
    # bank1 = Bank(bankname)
    # bank1.addCustomer(firstname,lastname)
    # bank1.getCustomer(0).setAccount(Account(50000))
    #
    # print(str(bank1.getCustomer(0).getAccount().getbalance()))



    # indexValue = 0
    # accList = []
    # while exit != "N":
    #     exit = str(input("do you want to use atm Y/N"))
    #     choice = int(input("Choose 1 to make a new account, choose 2 to use an existing account"))
    #     if choice == 1:
    #         accList.append(str(indexValue))
    #         accList[indexValue] = Customer()
    #         indexValue += 1
    #     elif choice == 2:
    #         accNo = int(input("please input which account you want to use "))
    #         optionChoice = int(input("Choose 1 to display balance, choose 2 to input deposit, choose 3 to withdraw deposit, choose 4 to displayAccount"))
    #         if optionChoice == 1:
    #             accNo = accList[accNo]
    #             print(accNo.getbalance())
    #         elif optionChoice == 2:
    #             amt = int(input("what is the amount you want to put "))
    #             result = accList[accNo].deposit(amt)
    #             if result == False:
    #                 print("don't put in your debt")
    #             elif result == True:
    #                 print(accList[accNo].getbalance())
    #         elif optionChoice == 3:
    #             amt = int(input("what is the amount you want to take "))
    #             result = accList[accNo].withdraw(amt)
    #             if result == False:
    #                 print("u too poor")
    #             elif result == True:
    #                 print(accList[accNo].getbalance())
    #
    #
main()
