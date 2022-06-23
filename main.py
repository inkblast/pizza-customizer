sizes = {'S': 'Small', 'M': 'Medium', 'L': 'Large'}
pizza_option = {'M': "Meat", 'V': "Veggie", 'S': "Supreme"}
crust_option = {'O': "Original", 'S': "Stuffed", 'H': "Hand Tossed", 'C': "Crispy"}
options = {'M' :["[O]riginal crust" ,"[S]tuffed"], 'V': ["[O]riginal crust", "[C]rispy crust"], 'S': ["[O]riginal crust" ,"[S]tuffed crust" ,"[H]and Tossted crust"]}

def display_bill(size,type,crust):
    prices_size = {"S":10.00,"M":12.00,"L":15.00}
    prices_type ={'M': 2.00,'V': 0.00,'S': 4.00}
    prices_crust ={'O': 0.00,'H': 1.00,'C': 1.50,'S': 3.00}
    total_price = prices_size[size] + prices_type[type] + prices_crust[crust]
    print(45*'*')
    print("\t\t\tYour Order Summery")
    print(f"your pizza size:\t{sizes[size]}\t\t\t ${prices_size[size]:.2f}")
    print(f"your pizza type:\t{pizza_option[type]}\t\t\t+$ {prices_type[type]:.2f}")
    print(f"your pizza crust:\t{crust_option[crust]}\t\t\t+$ {prices_crust[crust]:.2f}")
    print(45*"=")
    print(f"Total price:\t\t\t\t\t\t ${total_price:.2f}")

def build_pizza():
    print("Build your pizza!")


    isvalid_size = True
    isvalid_type = True
    isvalid_crust = True

    user_input1 = "We have [S]mall,[M]edium, or [L]arge pizza, which size do you prefer?"
    user_input2 = "Would you like [M]eat pizza, [V]eggie pizza or [S]upreme pizza with both meat and veggie? "


    while isvalid_size:
        size = input(user_input1)
        size = size.capitalize()
        if size in ['S','M','L']:
            isvalid_size = False
            print(f"You have choosen a {sizes[size]} pizza. ")
            while isvalid_type:
                po = input(user_input2)
                po = po.capitalize()
                if po in ['M','V','S']:
                    isvalid_type = False
                    print(f"You have choosen a {sizes[size]} {pizza_option[po]} pizza. ")


                    if po == 'S':
                        user_input4 = f"Would you like {options[po][0]} or {options[po][1]} or {options[po][2]}? "
                        while isvalid_crust:
                            crust=input(user_input4)
                            crust=crust.capitalize()
                            if crust in ['O','H','S','C']:
                                isvalid_crust = False
                                display_bill(size,po,crust)
                            else:

                                user_input4 = f"Please enter your crust preference, {options[po][0]} or {options[po][1]} or {options[po][2]}: "


                    else:
                        user_input3 = f"Would you like {options[po][0]} or {options[po][1]}? "
                        while isvalid_crust:
                            crust=input(user_input3)
                            crust=crust.capitalize()
                            if crust in ['O', 'H', 'S', 'C']:
                                isvalid_crust = False
                                display_bill(size, po, crust)
                            else:

                                user_input3 = f"Please enter your crust preference, {options[po][0]} or {options[po][1]}: "
                else:
                    user_input2 = "Please enter your what pizza would like to order, [M]eat pizza, [V]eggie pizza or [S]upreme pizza: "

        else:
            user_input1 = "Your pizza is only available in size [S]mall,[M]edium, or [L]arge: "



build_pizza()