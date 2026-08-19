def get_valid_hours():
    while True:
        try:
            hours_worked = int(input("How many hours did you work today? "))
            if hours_worked >= 0 and hours_worked <= 24:
                return hours_worked
            else:
                print("Please enter a number of hours between 0 and 24.")
    
        except ValueError:
            print("Please enter a valid number of hours.")

def work_day_calculator():
    
    name = input("What is your name? ")
    hours_worked = get_valid_hours()
    if hours_worked < 8:
        under_time = 8 - hours_worked
        print(f"{name} worked {hours_worked} hours today.")
        print(f"You are {under_time} hours short of a full workday.")
    elif hours_worked > 8:
        overtime = hours_worked - 8
        print(f"{name} worked {hours_worked} hours.")
        print(f"You have worked {overtime} hours of overtime.")
    else:
        print(f"{name} worked {hours_worked} hours today.")
        print(f"You have worked a full workday.")


if __name__ == "__main__":
    work_day_calculator()
    