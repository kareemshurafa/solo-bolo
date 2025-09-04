import datetime
import csv

def welcome():
    now = datetime.datetime.now()
    print("Welcome Kareem! Today's time and date is: " + str(now))

def goodbye():
    print("Thanks for logging your workout! Have a good day Kareem! ")


def user_action():
    actions = ["Add a workout", "View previous workouts", "Change a workout", "Exit"]
    lister(actions)
    action = input("Please select what you would like to do: ")
    
    match(action):
        case "1":
            workout_input()
        case "2":
            workout_view()
        case "3":
            workout_change()
        case "4":
            goodbye()
        case _:
            print("Error - please select a valid function")
            user_action()
    
def workout_input():
    workouts = []
    file = open("workouts.csv", 'r')
    for line in file.readlines():
        workouts.append(line.strip())
    splitter()
    lister(workouts)
    action = int(input("Please select a workout that you would like to add in: "))
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = int(input("Weight(kgs): "))
    volume = calc_vol(sets, reps, weight)
    print("Volume for " + workouts[action - 1] + ": " + str(volume))



def workout_view():
    pass


def workout_change():
    workouts = []
    file = open("workouts.csv", 'r')
    for line in file.readlines():
        workouts.append(line.strip())
    splitter()
    print("Current workouts: ")
    lister(workouts)
    splitter()
    actions = ["Add a new type of workout", "Remove a type of workout", "Amend a current type of workout", "Go back to main menu"]
    action = input("What would you like to do?")

    match(action):
        case "1":
            pass

def calc_vol(sets, reps, weight):
    return sets * reps * weight

def splitter():
    print("---------------------------------------------------------------")

def lister(list):
    for i in range(len(list)):
        print(str(i+1) + ". " + list[i])

def main():
    """Main program entry point"""
    
    welcome()
    user_action()
    
    # TODO: Initialize gym tracker
    # TODO: Load previous data
    # TODO: Start main menu loop
    
    pass

if __name__ == "__main__":
    main()