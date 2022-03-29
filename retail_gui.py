from tkinter import *

class RetailCalculator:
    def __init__(self):
        self.__window = Tk()
        self.__window.geometry("500x500")
        self.__window.title("Retail Calculator")

        self.__item_count_text = Label(self.__window, text="Enter item count: ")
        self.__item_count_text.grid(row=0,columnspan=3, padx=(10,10))
        self.__item_count = Entry(self.__window)
        self.__item_count.grid(row=1,columnspan=3, padx=(10,10))

        self.__price_text = Label(self.__window, text="Enter item price in USD: ")
        self.__price_text.grid(row=2,columnspan=3, padx=(10,10))
        self.__price = Entry(self.__window)
        self.__price.grid(row=3,columnspan=3, padx=(10,10))

        self.__state_code_text = Label(self.__window, text="Enter state code: ")
        self.__state_code_text.grid(row=4,columnspan=3, padx=(10,10))
        self.__state_code = Entry(self.__window)
        self.__state_code.grid(row=5,columnspan=3, padx=(10,10))

        self.__calc_button = Button(self.__window, text="Calculate", command=self.calculate)
        self.__calc_button.grid(row=6,columnspan=3, padx=(10,10))
    
        self.__error_label = Label(self.__window)
        self.__error_label.grid(row=7,columnspan=3,padx=(10,10))

        self.__initial_order_value = Label(self.__window)
        self.__initial_order_value.grid(row=8,columnspan=3,padx=(10,10))

        self.__discount_value = Label(self.__window)
        self.__discount_value.grid(row=9,columnspan=3,padx=(10,10))

        self.__tax_value = Label(self.__window)
        self.__tax_value.grid(row=10,columnspan=3,padx=(10,10))

        self.__total_order_value = Label(self.__window)
        self.__total_order_value.grid(row=11,columnspan=3,padx=(10,10))



        self.__init_order_value = 0.00  #before discount
        self.__order_value = 0.00 #after discount
        self.__inputted_state = ""
        self.__discount = 0.00

        self.__states = {"UT": 0.0685, "NV": 0.0800, "TX": 0.0625, "AL": 0.0400, "CA": 0.0825}

    def calculate(self):
        print(self.__item_count.get())
        # initial value
        try:
            self.__init_order_value = float(self.__item_count.get()) * float(self.__price.get())
        except:
            self.__error_label.configure(text="Invalid count or price!")
            self.__item_count.delete(0,END)
            self.__price.delete(0,END)

        state_tax = 0
        inp_state = self.__state_code.get()
        if inp_state not in self.__states:
            self.__error_label.configure(text="Invalid state")
            return

        self.__inputted_state = inp_state
        state_tax = self.__states[inp_state]

        discount = 0
    
        if self.__init_order_value >= 50000:
            self.__discount += 0.15
            
        elif self.__init_order_value >= 10000:
             self.__discount += 0.10

        elif self.__init_order_value >= 7000:
             self.__discount += 0.07

        elif self.__init_order_value >= 5000:
             self.__discount += 0.05

        elif self.__init_order_value >= 1000:
             self.__discount += 0.03
        
        order_value = self.__init_order_value * (1 - discount)
        total = order_value * (1+state_tax)    
               
        initial_order_value_text = "Initial order value: " + str(self.__init_order_value)
        self.__error_label.configure(text="")
        self.__initial_order_value.configure(text=initial_order_value_text)

        discount_value_text = "Amount of discount: " + str(round(self.__init_order_value * self.__discount , 2))
        self.__discount_value.configure(text=discount_value_text)

        tax_value_text = "Amount of tax: " + str(round(order_value * state_tax, 2))
        self.__tax_value.configure(text=tax_value_text)

        total_order_value_text = "Total order value: " + str(round(total, 2))
        self.__total_order_value.configure(text=total_order_value_text)

    def start(self):
        self.__window.mainloop()


def main():
    ui = RetailCalculator()
    ui.start()




main()