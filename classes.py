class User:
    def __init__(self, name, email, login, password):
        self.__name = name
        self.__email = email
        self.__login = login
        self.__password = password

    def __str__(self):
        return '\n\tName: %s\n\tEmail: %s\n\tLogin: %s\n\t' %(self.name, self.email, self.login)
    def write(self):
        return 'n=%s\ne=%s\nl=%s\np=%s' %(self.name, self.email, self.login, self.password)

    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    @property
    def login(self):
        return self.__login
    @property
    def password(self):
        return self.__password

    @name.setter
    def name(self, name):
        self.__name = name
    @email.setter
    def email(self, email):
        self.__email = email
    @login.setter
    def login(self, login):
        self.__login = login
    @password.setter
    def password(self, password):
        self.__password = password

class Product:
    def __init__(self, name, brand, category, price, code, stock, user):
        self.__name = name
        self.__brand = brand
        self.__category = category
        self.__price = price
        self.__code = code
        self.__salesThisMonth = 0
        self.__stock = stock
        self.__user = user
        #self.__totalSales = 0

    def write(self):
        return 'n=%s\nb=%s\nct=%s\np=%f\nc=%s\ns=%d\nu=%s\n' %(self.name, self.brand, self.category, self.price, self.code, self.stock, self.user)
    def writeCode(self):
        return '%s\n' %(self.code)
    def __str__(self):
        return '\n\tName: %s\n\tBrand: %s\n\tCategory: %s\n\tPrice: %f\n\tCode: %s\n\tStock: %d\n' %(self.name, self.brand, self.category, self.price, self.code, self.stock)

    @property
    def name(self):
        return self.__name
    @property
    def brand(self):
        return self.__brand
    @property
    def category(self):
        return self.__category
    @property
    def price(self):
        return self.__price
    @property
    def code(self):
        return self.__code
    @property
    def salesThisMonth(self):
        return self.__salesThisMonth
    @property
    def stock(self):
        return self.__stock
    @property
    def user(self):
        return self.__user
    #@property
    #def __totalSales(self):
    #    return self.__totalSales

    @name.setter
    def name(self, name):
        self.__name = name
    @brand.setter
    def brand(self, brand):
        self.__brand = brand
    @category.setter
    def category(self, category):
        self.__category = category
    @price.setter
    def price(self, price):
        self.__price = price
    @code.setter
    def code(self, code):
        self.__code = code
    @salesThisMonth.setter
    def salesThisMonth(self, sales):
        self.__salesThisMonth = sales
    @stock.setter
    def stock(self, stock):
        self.__stock = stock
    @user.setter
    def user(self, user):
        self.__user = user
    #@totalSales.setter
    #def totalSales(self, sales):
    #   self.__totalSales = sales