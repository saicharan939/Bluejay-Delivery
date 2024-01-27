import csv

# Assume that the file is in the same directory as this script
filename = "Assignment_Timecard.xlsx - Sheet1.csv"

# List to store employees that meet the criteria
consecutive_workdays = []
time_between_shifts = []
max_hours_in_shift = []

# Open the CSV file for reading
with open(filename, "r") as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Check if the employee has worked for 7 consecutive days
        if row["WorkDays"] == "7":
            consecutive_workdays.append(row)

        # Check if the employee has less than 10 hours of time between shifts but greater than 1 hour
        time_between_shifts_int = int(row["TimeBetweenShifts"])
        if 1 < time_between_shifts_int < 10:
            time_between_shifts.append(row)

        # Check if the employee has worked for more than 14 hours in a single shift
        max_hours_in_shift_int = int(row["MaxHoursInShift"])
        if max_hours_in_shift_int > 14:
            max_hours_in_shift.append(row)

# Print the results in the console
print("Employees with 7 consecutive workdays:")
for employee in consecutive_workdays:
    print(f"{employee['Name']} - {employee['Position']}")

print("\nEmployees with less than 10 hours of time between shifts but greater than 1 hour:")
for employee in time_between_shifts:
    print(f"{employee['Name']} - {employee['Position']}")

print("\nEmployees who have worked for more than 14 hours in a single shift:")
for employee in max_hours_in_shift:
    print(f"{employee['Name']} - {employee['Position']}")