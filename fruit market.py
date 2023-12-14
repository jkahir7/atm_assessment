
products = {}

menu = """

        WELCOME TO FRUIT MARKET

        1) manager
        2) customer
        
"""

print(menu)
flage = True
while flage:
    choice = int(input("select your role : "))
    if choice == 1:
        print(" FRUITE MARKET MANAGER ")

        menu_1 = """

            1) add fruit stock
            2) view fruit stock
            3)update fruit stock

            """
        print(menu_1)
        status = True    
        while status:
            print(" ")
            choice = int(input("enter a choice : "))

            if choice == 1:
                spesific_product = {}
                print(" ")
                product_name = input("enter product name : ")
                product_qty = int(input("enter qty :"))
                product_price = int(input("enter product price of 1 kg : "))


                if product_name in products:
                    # fatch old qty from the dictionary
                    old_qty = products[product_name]['qty']
                    spesific_product['qty'] = old_qty + product_qty
                    spesific_product['price'] = product_price

                else:
                    spesific_product['qty'] = product_qty
                    spesific_product['price'] = product_price

                products[product_name] = spesific_product
                print(" ")


                print("products = ",products)
                print(" ")
                choice = input("do you want to add more product : ")
                if choice == 'y' or choice == 'Y':
                    status = True

                else:
                    status = False


            elif choice == 2:
                for k in products.keys():
                    print(f"{k} - 1kg price re.{products[k]['price']}")

                choice = input("do you want to perform more operations : press y for yes and n for not ")
                if choice == 'y':
                    flage = True
                else:
                    flage = False

            elif choice == 3:
                    spesific_product = {}
                    print(" ")
                    product_name = input("enter product name : ")
                    product_qty = int(input("enter qty :"))
                    product_price = int(input("enter product price of 1 kg : "))


                    if product_name in products:
                        # fatch old qty from the dictionary
                        old_qty = products[product_name]['qty']
                        spesific_product['qty'] = old_qty + product_qty
                        spesific_product['price'] = product_price

                    else:
                        spesific_product['qty'] = product_qty
                        spesific_product['price'] = product_price

                    products[product_name] = spesific_product
                    print(" ")


                    print("products = ",products)
                    print(" ")
                    choice = input("do you want to add more product : ")

                    if choice == 'y' or choice == 'Y':
                      status = True

                    else:
                          status = False



    elif choice == 2:
        print("--------------")
        print(" ")
        print(" customer panel ")

        
        net = 0
        status = True
        total_price = 0
        while status:
            #spesific_product = {}
            cart = {}
            product_n = input("enter your product name : ")
            print(product_n)
            print("")
            qty = int(input("enter your qty"))
            if qty <= spesific_product['qty'] and product_n in products:
                cart['qty'] = qty
                cart['price'] = product_price
                
                amount = qty * product_price
                print("net price is :",amount)
                print(" ")


                #print(cart) 
            

            else:
              print("insuficiant stock")
            
            print(" ")
            choice = input("do you want to perform more operations : press y for yes and n for not ")
            if choice == 'y':
                status = True
            else:
                status = False
            
            net+=amount
            print("total amount",net)
            flage = False
