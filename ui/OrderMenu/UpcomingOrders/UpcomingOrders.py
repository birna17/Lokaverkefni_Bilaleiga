import os

#This class calls a service class that returns this class a list of upcoming orders
#This class then displays that to the user
#Action should be to select one of the orders and to go back
class UpcomingOrders:
    def __init__(self):
        pass
    def upcomingOrders(self):
        os.system('cls')
        upcoming_order_menu_selection = ""
        while(upcoming_order_menu_selection !="9"):
            print("Upcoming orders class call here")
            print("9. Back")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                pass
