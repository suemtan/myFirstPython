#getter and setter bank account and log file

class BankAccount:
    #initialize balance to 0
    def __init__(self, name, balance = 0.0):
        self.log("Account created !")
        self.name = name
        self.balance = balance

    #getter method with return value and log
    def getBalance(self):
        self.log("\nBalance checked at " + str(self.balance))
        return self.balance

    # setter method with parameter and log
    def setBalance(self, newBalance):
        self.balance = newBalance
        self.log("\nBalance changed to " + str(newBalance))

    #deposit
    def deposit(self, amount):
        self.balance += amount
        self.log("\n - " + str(amount) + ": " + str(self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        self.log("\n - " + str(amount) + ": " + str(self.balance))

    #log function for file log
    def log(self, message):
        myLog = open("log.txt", "a")
        myLog.write(message)
        #print(myLog.read())
        myLog.close()


myBankAccount = BankAccount("David Joyner")
myBankAccount.deposit(100.0)
print(myBankAccount.getBalance())

myBankAccount.withdraw(20.0)
print(myBankAccount.getBalance())

f = open("log.txt", "r")
message = f.read()
print(message)
f.close()
