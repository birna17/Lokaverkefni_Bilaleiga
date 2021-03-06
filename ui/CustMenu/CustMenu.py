import os
from services.CustomerManager import CustomerManager
from colorama import Fore

class CustMenu:
    def __init__(self, manager):
        self.__manager = manager
        self.__customer = CustomerManager()

    def customerMenu(self):
        selection = ""
        self.__manager.printHeader()
        while (selection != "9"):
            print(Fore.GREEN,end="")
            print("1. Lookup Customer")
            print("2. Register Customer")
            print(Fore.RED,end="")
            print("9. Go Back")
            print(Fore.WHITE,end="")
            print("--------------")
            selection = input()
            self.__manager.printHeader()

            # kallar í annan UI klasa sem spyr um SSN og leita af viðskiptavininum

            if selection == "1":
                self.__manager.gotoClass("lookupcustomer")

            # kallar í anna UI klasa sem spyr um upplýsingar um notandann sem sendi þær áfram
            # í service og niður i repo sem skrifar gögnin    
            #               
            elif selection == "2":
                self.__manager.gotoClass("registercustomer")

            else:
                self.__manager.gotoClass("mainmenu")
