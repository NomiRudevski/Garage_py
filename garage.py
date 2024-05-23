from enum import Enum
from print_color import print
import json

cars = []


class Actions(Enum):
    ALL_CARS = 1
    ADD_CAR = 2
    UPDATE_CAR = 3
    DELETE_CAR = 4
    INFO = 5
    DELET_ALL_DATA = 6
    EXIT = 7

def load_data_from_json():
    global cars
    try:
        with open('data.json', 'r') as file:
            cars = json.load(file)
    except:
        cars = []


def print_options():
    for action in Actions:
        print(f'{action.value} - {action.name}')


#validating if user selection is a valid option
def validate_user_selection(user_input):
    while True:
        try:                                                            #check if user entered a num
            selection = int(user_input)
            if selection in [action.value for action in Actions]:       #check if user selection is an existing option
                return Actions(selection)
            else:
                print("Input invalid", color = 'red')
                user_input = input("please enter a valid option: ")
        except:
            print("Input invalid", color = 'red')
            user_input = input("please enter a valid option: ")


def show_all_cars():
    if cars == []: return print("No cars available", color="red")
    for i,car in enumerate(cars):
        print(f'{i+1} - {car["name"]} | {car["color"]} | {car["owner"]}', color='cyan')


def add_new_car():
    print("Please enter new car ditails", color='yellow')
    cars.append({"name" : input("Car company: "), "color" : input("Car color: "), "owner" : input("Car owner: ")})
    print("new car added successfully", color = 'green')


def get_car_index():
    show_all_cars()
    index_selection = input("Please enter car number to select: ")
    while True:
        try:
            index = int(index_selection)-1
            if 0 <= index < len(cars):
                print(f'{cars[index]["owner"]}`s car was selected', color='green')
                return index
            else:
                print("Input invalid", color = 'red')
                index_selection = input("please enter a valid option: ")
        except:
            print("Input invalid", color = 'red')
            index_selection = input("please enter a valid option: ")


def update_existing_car():
    if cars == []: return print("No cars available", color="red")
    index = get_car_index()
    cars[index] = {"name" : input("Car company: "), "color" : input("Car color: "), "owner" : input("Car owner: ")}
    print('Update successfully!', color='green')


def delete_car():
    if cars == []: return print("No cars available", color="red")
    index = get_car_index()
    print("Car was deleted successfully", color='red')
    cars.pop(index)


def info_all_cars():
    print(f'ther are {len(cars)} cars in the garage!', color='yellow')


def delete_all_data():
    print("This action will clear all the data. Do you wish to proceed", color='red')
    while True:
        confirmation = input("please enter y/n: ")
        if confirmation.lower() == 'y':
            global cars
            with open('data.json', 'w') as file:
                json.dump([], file)
            cars = []
            print("All data was cleared sucssesfuluy.", color='red')
            break
        elif confirmation.lower() == 'n':
            print("Data was not deleted", color='red')
            break
        else:
            print("input invalid", color='red')


def close_program():
    with open('data.json', 'w') as file:
        json.dump(cars, file, indent=4)
    print("All changes saved! Goodbay!", color='magenta')
    exit()


if __name__ == "__main__":
    load_data_from_json()
    while True:
        print_options()
        user_selection = validate_user_selection(input("Enter your selection: "))
        if user_selection == Actions.ALL_CARS: show_all_cars()
        if user_selection == Actions.ADD_CAR: add_new_car()
        if user_selection == Actions.UPDATE_CAR: update_existing_car()
        if user_selection == Actions.DELETE_CAR: delete_car()
        if user_selection == Actions.INFO: info_all_cars()
        if user_selection == Actions.DELET_ALL_DATA: delete_all_data()
        if user_selection == Actions.EXIT: close_program()