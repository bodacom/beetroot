class Currency:
    
    def __init__(self, name, exchange_rate):
        self.name = name
        self.exchange_rate = exchange_rate
    
    @property    
    def exchange_rate(self):
        return self.__exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        if exchange_rate <= 0:
            raise ValueError("Exchange rate cannot be lower or equal to zero.")
        self.__exchange_rate = exchange_rate
      
    @exchange_rate.deleter
    def exchange_rate(self):
        del self.__exchange_rate

usd = Currency('USD', 2)
print(usd.exchange_rate)
usd.exchange_rate = 42
print(usd.exchange_rate)
del usd.exchange_rate
print(usd.exchange_rate)


