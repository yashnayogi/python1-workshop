# it restrict access to certain 
'''
class bankaccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self._balance = balance

    def  get_balance(self):
        return self._balance


account1 = bankaccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())'''


# inheritance ==> allows you to create  new classes that inherit properties and methods from existng classs

class animals:
    def __init__(self,name):
        self.name = name

    def speaks(self):
        pass

class dog(animals):
    def speaks(self):
        return "woof!"
    
class cat(animals):
    def speaks(self):
        return "meow!"

dog1 = dog("buddy")
cat1 = cat("whiskers")
print(dog1.name,dog1.speaks())
print(cat1.name,cat1.speaks())