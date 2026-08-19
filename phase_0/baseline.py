from app.workday import calculate_workday


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
    result = calculate_workday(hours_worked)

    if result["status"] == "overtime":
        print(f"{name}, you have {result['hours']} hours of overtime today.")
    elif result["status"] == "under_time":
        print(f"{name}, you have {result['hours']} hours of under time today.")
    else:
        print(f"{name}, you have worked exactly 8 hours today. No overtime or under time.")

if __name__ == "__main__":
    work_day_calculator()
