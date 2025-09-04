import datetime

def welcome():

    now = datetime.datetime.now()

    print("Welcome K.S!")
    print("Today's time and date is: " + str(now))
    print("Have fun, and keep gymming!")
    action = int(input("Please select what you would like to do: "))
    if action == 1:
        workout_input()

def workout_input():
    workouts = ["1. Lat Raise", "2. Chest Press", "3. Preacher Curl"]
    splitter()
    print(workouts)
    action = int(input("Please select a workout that you would like to add in: "))
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    weight = int(input("Weight(kgs): "))

    volume = calc_vol(sets, reps, weight)

    print("Volume for " + workouts[action - 1] + ": " + str(volume))

def calc_vol(sets, reps, weight):
    return sets * reps * weight


def splitter():
    print("---------------------------------------------------------------")



def main():
    """Main program entry point"""
    welcome()
    
    # TODO: Initialize gym tracker
    # TODO: Load previous data
    # TODO: Start main menu loop
    
    pass

if __name__ == "__main__":
    main()