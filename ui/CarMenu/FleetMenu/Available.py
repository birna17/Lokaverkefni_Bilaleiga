import os
from colorama import Fore

class Available:
    def __init__(self, manager):
        self.__manager = manager
    def available(self):
        self.__manager.printHeader()
        menu_selection = ""
        while(menu_selection !="9"):
            Vehicles = self.__manager.getVehicleManager().getAvailable()
            print(Fore.BLUE,end="")
            for vehicle in Vehicles:
                print(vehicle)
            print(Fore.RED,end="")
            print("\n9. Back")
            print(Fore.WHITE,end="")
            upcoming_order_menu_selection = input()
            if upcoming_order_menu_selection == "9":
                self.__manager.gotoClass("fleetmenu")