def chapter_1_intro():
    while True:
        print("The vast emptiness of space surrounded the derelict colony of Ronuke. Silence was the only greeting.")
        next_action = input("Do you want to explore the docking station, rest in the explorer's ship, or access the central computer? (docking/rest/computer): ")
        if next_action.lower() == "docking":
            return explore_docking_station()
        elif next_action.lower() == "rest":
            return rest_in_explorers_ship()
        elif next_action.lower() == "computer":
            return access_central_computer()
        else:
            print("Invalid choice. Please try again.")

def explore_docking_station():
    while True:
        print("You are exploring the docking station.")
        next_action = input("Do you want to access the central computer or move towards the residential area? (computer/residential): ")
        if next_action.lower() == "computer":
            return access_central_computer()
        elif next_action.lower() == "residential":
            return move_towards_residential_area()
        else:
            print("Invalid choice. Please try again.")

def rest_in_explorers_ship():
    while True:
        print("You rest in the explorer's ship.")
        next_action = input("Do you want to explore the docking station or access the central computer? (docking/computer): ")
        if next_action.lower() == "docking":
            return explore_docking_station()
        elif next_action.lower() == "computer":
            return access_central_computer()
        else:
            print("Invalid choice. Please try again.")

def access_central_computer():
    while True:
        print("You access the central computer.")
        next_action = input("Do you want to explore the docking station or move towards the residential area? (docking/residential): ")
        if next_action.lower() == "docking":
            return explore_docking_station()
        elif next_action.lower() == "residential":
            return move_towards_residential_area()
        else:
            print("Invalid choice. Please try again.")

def move_towards_residential_area():
    print("You move towards the residential area.")
    return 'chapter_2'
#I dont think I need to write any comments on here