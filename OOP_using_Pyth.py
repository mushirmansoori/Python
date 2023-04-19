class Account:
    count = 0
    
    @classmethod
    def incr__count(cls):
        cls.count+=1
        
    @classmethod
    def get_count(cls):
        return cls.count
        
    @staticmethod   
    def print_Val():
        print("Static Method in account class")
        
    def __init__(self,cust_id,name,initial_bal=0):
        self.__id = cust_id
        self.__name = name
        self.__balance = initial_bal
        Account.incr__count()
        
    def get_balance(self):
        return self.__balance
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
        
    def deposite(self,ammount):
        self.__balance = self.__balance + ammount
        return self.__balance
        
    def withdraw(self,ammount):
        if ammount > self.__balance:
            return "Insufficient Balance"
        else:
            self.__balance -= ammount
            return self.__balance
            
class Saving_Account(Account):
    def __init__(self,id,name,initial_bal=0):
        super().__init__(id,name,initial_bal)
        self.limit = 50000
        
    def withdraw(self,ammount):
        if ammount < self.limit:
            new_bal = super().withdraw(ammount)
            self.limit -= ammount
            return new_bal
        else:
            print("Daily limit reached !")
        
cust1 = Saving_Account(101,"ABC")
print(cust1.__dict__)
print(cust1.deposite(80000))
print(cust1.withdraw(40000))    
print(cust1.withdraw(40000))   
