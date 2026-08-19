def calculate_workday(hours_worked):
    # A workday cannot contain more than 24 recorded hours.
    if hours_worked < 0 or hours_worked > 24:
        raise ValueError("Hours worked must be between 0 and 24")

    if hours_worked < 8:
        return {"status": "under_time", "hours": 8 - hours_worked}
    elif hours_worked > 8:
        return {"status": "overtime", "hours": hours_worked - 8}
    else:
        return {"status": "full_day", "hours": 0}