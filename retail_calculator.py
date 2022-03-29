import tkinter as tk

def main():
    
    states = {"UT": 0.0685, "NV": 0.0800, "TX": 0.0625, "AL": 0.0400, "CA": 0.0825}
    
    while True:
        try:
            count = int(input("Enter item count: "))
        except:
            print("Count must be a number.")
        else:
            break

    while True:
        try:
            price = float(input("Enter item price in USD: "))
        except:
            print("Price must be a number.")
        else:
            break
    
    
    
    state_tax = 0
    while True:
        
        inputted_state = str(input("Enter state code: "))
        if inputted_state not in states:
            print("Invalid state code")

        else:                      
            state_tax += states[inputted_state]
            break
        
    init_order_value = count * price
    discount = 0
    
    if init_order_value >= 50000:
        discount += 0.15
          
    elif init_order_value >= 10000:
        discount += 0.10

    elif init_order_value >= 7000:
        discount += 0.07

    elif init_order_value >= 5000:
        discount += 0.05

    elif init_order_value >= 1000:
         discount += 0.03
    
    order_value = init_order_value * (1 - discount)
    total = order_value * (1+state_tax)    

    print("\nCount            " + str(count))
    print("Price per item   " + str(price))
    print("Discount " + str(discount * 100) + "%    -" + str(round(init_order_value*discount)))
    print("Tax " + str(round(state_tax*100,2)) + "%       " + str(round(order_value*state_tax,2)))
    print("-------------------------")
    print("Total            " + str(round(total, 2)))

if __name__ == "__main__":
    main()