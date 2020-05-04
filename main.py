import os
import sys
import getpass
from getch import getch
from classes import User, Product

currentUser = None

#Hide the password with '*';
def win_getpass(prompt='Password: ', stream=None):
    """Prompt for password with echo off, using Windows getch()."""
    #if sys.stdin is not sys.__stdin__:
    #    return fallback_getpass(prompt, stream)
    import msvcrt
    for c in prompt:
        msvcrt.putwch(c)
    pw = ""
    while 1:
        c = msvcrt.getwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            if pw == '':
                pass
            else:
                pw = pw[:-1]
                msvcrt.putwch('\b')
                msvcrt.putwch(" ")
                msvcrt.putwch('\b')
        else:
            pw = pw + c
            msvcrt.putwch("*")
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    return pw

def firstScreen():
    os.system('cls')
    print('\t########## CUSTOM STORE - WELCOME ##########')
    print('\n\tWelcome to the Custom Store storage service!')
    print('\n\t\t1  Login')
    print('\n\t\t2  Register')

    option = input('\nType an option: ')

    if option == '1':
        loginScreen()
    elif option == '2':
        registerScreen()
    else:
        print('\nATTENTION: Type a valild value!')
        os.system('pause')
        firstScreen()    
 
def loginScreen():
    os.system('cls')
    print('\t########## CUSTOM STORE - LOGIN ##########')
    userLogin = input('\n\tLogin: ')

    if not checkLogin(userLogin):
        print('\n\tATTENTION: The login is NOT registered!')
        os.system('pause')
        firstScreen()

    userPassword = win_getpass('\n\tPassword: ')

    if not checkPassword(userLogin, userPassword):
        print('\n\tATTENTION: The login and password does not match!')
        os.system('pause')
        firstScreen()

    global currentUser

    currentUser = userLogin
    storeLayout()

def password():
    userPassword = win_getpass('\n\tPassword: ')
    rePassword = win_getpass('\n\tRetype password: ')

    if rePassword != userPassword:
        print('\n\tATTENTION: The passwords does not match!')
        password()

    return userPassword

def registerScreen():
    os.system('cls')
    print('\t########## CUSTOM STORE - REGISTER ##########')
    userName = input('\n\tFull name: ')
    userEmail = input('\n\tE-mail: ')
    userLogin = input('\n\tLogin: ')

    if checkLogin(userLogin):
        print('\n\tATTENTION: The login is already registered!')
        os.system('pause')
        registerScreen()

    userPassword = password()
    
    try:
        check = input('\nATTENTION: Are the data entered correct? (y/n) ')

        if check == 'y':
            createUser(userName, userEmail, userLogin, userPassword)
        elif check == 'n':
            registerScreen()
        else:
            print('\nATTENTION: Type a valild value!')
            os.system('pause')
            registerScreen() 
    except ValueError:
        print('\nATTENTION: Type a valild value!')
        os.system('pause')
        registerScreen()

def createUser(userName, userEmail, userLogin, userPassword):
    newUser = User(userName, userEmail, userLogin, userPassword)
    writeUsers(newUser)
    print('\n\tUser SUCCESSFULLY created!')
    os.system('pause')
    firstScreen()

def writeUsers(user):
    with open('_files\data.txt', 'a+') as f:
        f.write(user.write() + '\n')

def checkLogin(login):
    login = 'l=' + login + '\n'
    try:
        with open('_files\data.txt', 'r') as f:
            userdata = f.readlines()
            for line in userdata:
                if login == line:
                    return True
        return False
    except FileNotFoundError:
        print('\n\tERROR: Data file not found!')
        os.system('pause')
        os.system('cls')
        exit()

def checkPassword(login, password):
    password = 'p=' + password + '\n'
    login = 'l=' + login + '\n'
    prevLine = -1
    try:
        with open('_files\data.txt', 'r') as f:
            userdata = f.readlines()
            for line in userdata:
                if password == line and prevLine == login:
                    os.system('pause')
                    return True
                prevLine = line
        return False
    except FileNotFoundError:
        print('\n\tERROR: Data file not found!')
        os.system('pause')
        os.system('cls')
        exit()

def storeLayout():
    os.system('cls')
    print('\t########## CUSTOM STORE ##########')
    print('\n\t\t1  Products')
    print('\n\t\t2  Employees')
    print('\n\t\t3  Clients')
    print('\n\t\t4  Sales')
    print('\n\t\t5  Quit')

    op = input('\nType an option: ')

    if op == '1':
            productsMenu()
    elif op == '2':
            pass
    elif op == '3':
        pass
    elif op == '4':
        pass
    elif op == '5':
        print('\n\tLeaving the application...')
        os.system('pause')
        os.system('cls')
        exit()
    else:
        print('\nATTENTION: Type a valild value!')
        os.system('pause')
        storeLayout()
    
def productsMenu():
    os.system('cls')
    print('\t########## CUSTOM STORE - PRODUCTS ##########')
    print('\n\t\t1  Search')
    print('\n\t\t2  Sell')
    print('\n\t\t3  Register')
    print('\n\t\t4  Previous Menu')
    
    op = input('\nType an option: ')

    if op == '1':
        searchProductsMenu()
    elif op == '3':
        regiterProductsMenu()
    elif op == '4':
        storeLayout()
    else:
        print('\nATTENTION: Type a valild value!')
        os.system('pause')
        productsMenu()

def searchProductsMenu():
    os.system('cls')
    print('\t########## CUSTOM STORE - SEARCH PRODUCTS ##########')
    print('\n\t\t1  Search for Name')
    print('\n\t\t2  Search for Code')
    print('\n\t\t3  Search for Brand')
    print('\n\t\t4  Show all Products')
    print('\n\t\t5  Previous Menu')

    op = input('\nType an option: ')

    if op == '1':
        searchProductNameMenu()
    if op == '2':
        searchProductsCodeMenu()
    elif op == '5':
        productsMenu()
    else:
        print('\nATTENTION: Type a valild value!')
        os.system('pause')
        productsMenu()

def regiterProductsMenu():
    os.system('cls')
    print('\t########## CUSTOM STORE - REGISTER PRODUCTS ##########')
    print("\n\tPress 'i' if you want to review the Register Product rules;")
    info = getch()

    if info == 'i':
        pass

    try:
        name = input('\n\tProduct Name: ')
        brand = input('\n\tProduct Brand: ')
        code = input('\n\tProduct Code: ')

        if checkCode(code):
            print('\nATTENTION: The product is already registered!')
            os.system('pause')
            productsMenu()

        category = input('\n\tProduct Category: ')
        price = float(input('\n\tProduct Price: '))
        n = int(input('\n\tNumber of products: '))
        user = currentUser

        name = name.replace(name, name.upper())
        brand = brand.replace(brand, brand.upper())
        category = category.replace(category, category.upper())

        createProduct(name, brand, code, category, price, n, user)
    except ValueError:
        print('\nATTENTION: Type a valid value!')
        os.system('pause')
        regiterProductsMenu()

def checkCode(code):
    code = code + '\n'
    try:
        with open('_files\codes.txt', 'r') as f:
            userdata = f.readlines()
            for line in userdata:
                if code in line:
                    return True
        return False
    except FileNotFoundError:
        print('\n\tERROR: Data file not found!')
        os.system('pause')
        os.system('cls')
        exit()

def createProduct(name, brand, code, category, price, n, user):
    product = Product(name, brand, category, price, code, n, user)
    registerProduct(product)

def registerProduct(product):
    with open('_files\products.txt', 'a+') as f:
        f.write(product.write())
    with open('_files\codes.txt', 'a+') as f:
        f.write(product.writeCode())
    
    print('\n\tProduct SUCCESSFULLY registered!')
    os.system('pause')
    productsMenu()

def searchProductNameMenu():
    os.system('cls')
    print('\t########## CUSTOM STORE - SEARCH PRODUCTS ##########')

    tempName = input('\n\tType the product name: ')
    tempName = tempName.replace(tempName, tempName.upper())
    tempName = tempName.split(' ')

    products = searchProductsName(tempName)

    if products == -1:
        print('\nATTENTION: The product was not found!')
        os.system('pause')
        searchProductsMenu()

    for i in range(len(products)):
        print(products[i])
    
    os.system('pause')
    searchProductsMenu()

def searchProductsName(names):
    products = []
    otherStuff = []
    found = False
    count = 0

    for i in range(len(names)):
        check = False
        with open('_files\products.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if names[i] in line and line[0] == 'n':
                    productName = line[2:(len(line) - 1)]
                    found = True
                    count = 7
                if found and count > 0:
                    if line[2] == '=':
                        line = line[3:(len(line) -1)]
                    else:
                        line = line[2:(len(line) -1)]
                    otherStuff.append(line)
                    count -= 1

        if len(otherStuff) == 0:
            return -1

        while(len(otherStuff) > 0):
            productName = otherStuff[0]
            productBrand = otherStuff[1]
            productCategory = otherStuff[2]
            productPrice = float(otherStuff[3])
            productCode = otherStuff[4]
            productStock = int(otherStuff[5])
            productUser = otherStuff[6]

            product = Product(productName, productBrand, productCategory, productPrice, productCode, productStock, productUser)
            for p in products:
                if product.name == p.name:
                    check = True
            if not check:
                products.append(product)
            otherStuff = otherStuff[7: len(otherStuff)]
    
    toRemove = []
    for i in range(len(products)):
        for name in names:
            if name not in products[i].name:
                toRemove.append(products[i])

    for p in toRemove:
        if p in products:
            products.remove(p)

    return products

def searchProductsCodeMenu():
    os.system('cls')
    print('\t########## CUSTOM STORE - SEARCH PRODUCTS ##########')

    code = input('\n\tType the product code: ')
    code = code + '\n'
    product = searchProductsCode(code)
    print(product)
    
    os.system('pause')
    searchProductsMenu()

def searchProductsCode(code):
    exists = False
    try:
        with open('_files\codes.txt') as f:
            codes = f.readlines()
            for line in codes:
                if code == line:
                    exists = True        
    except FileNotFoundError:
        print('\n\tERROR: Data file not found!')
        os.system('pause')
        os.system('cls')
        exit()

    if not exists:
        print('\nATTENTION: The product was not found!')
        os.system('pause')
        searchProductsMenu()
    else:
        code = code[0: (len(code) - 1)]
        stop = False
        try:
            with open('_files\products.txt') as f:
                lines = f.readlines()
                index = 0
                for line in lines:
                    if line[0] == 'n' and not stop:
                        mark = index
                    if line[0] == 'c' and line[1] == '=':
                        tempCode = line[2:(len(line) - 1)]
                        if code == tempCode:
                            stop = True
                            name = lines[mark]
                            brand = lines[mark + 1]
                            category = lines[mark + 2]
                            price = lines[mark + 3]
                            code = code
                            stock = lines[mark + 5]

                            name = name[2: (len(name) - 1)]
                            brand = brand[2: (len(brand) - 1)]
                            category = category[3: (len(category) - 1)]
                            price = float(price[2: (len(price) - 1)])
                            stock = int(stock[2: (len(stock) -1)])

                            product = Product(name, brand, category, price, code, stock, currentUser)
                            return product
                    index += 1
                            
        except FileNotFoundError:
            print('\n\tERROR: Data file not found!')
            os.system('pause')
            os.system('cls')
            exit()

def searchProductBrandMenu():
    os.system('cls')
    print('\t########## CUSTOM STORE - SEARCH PRODUCTS ##########')

    brand = input('\n\tType the product brand: ')
    brand = brand + '\n'

def searchProductBrand(brand):
    pass

firstScreen()