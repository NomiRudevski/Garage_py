# Garage
### This is a simple Python script for managing a list of cars.
### All CRUD actions are available.
### The data is saved to and loaded back up or each iteration.

## Getting started
After cloning the project make sure to set up venv, and download the requirements.

### Functions
- load_data_from_json: Loads car data from data.json into the global cars list.
- print_options: Prints the available actions.
- validate_user_selection: Validates the user's selection and returns the corresponding action.
- show_all_cars: Displays all cars in the list.
- add_new_car: Adds a new car to the list.
- get_car_index: Prompts the user to select a car from the list and returns its index once validated.
- update_existing_car: Updates the details of an existing car.
- delete_car: Deletes a car from the list.
- info_all_cars: Displays the total number of cars.
- delete_all_data: Clears all car data after user confirmation.
- close_program: Saves the car list to 'data.json' and exits the program.