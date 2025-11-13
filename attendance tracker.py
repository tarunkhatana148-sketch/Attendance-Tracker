import datetime
# Task 1 Implementation

'''
    Name: {--Tarun--}
    roll no:{2501940050}
    Date: {--12-11-2025--}
    Assignment Title: {Python-Based Command-Line Attendance Tracker}
'''
print('''
    ----------------Welcome to Attendance Tracker----------------------
    This Program records student check-ins with timestamps using Python.
    --------------------------------------------------------------------
''')


# Task 2  And Task 3 Implementation

attendance = {}

try:
    num_entries = int(input("Enter the total number of entries to record: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

for i in range(num_entries):
    print(f"\n--- Entry {i+1} ---")

    # 1. Input student name and time
    while True:
        student_name = input("Enter Student Name: ").strip()
        # --- Validation 1: Check for Empty Name ---
        if student_name == "":
            print("\n❌ Error: Student name cannot be empty. Please try again.\n")
            continue
        
        # --- Validation 2: Check for Duplicate Entry ---
        if student_name in attendance:
            print(f"\n⚠ Warning: {student_name} has already checked in at {attendance[student_name]}. Please try again.\n")
            continue
        break
    while True:
        check_in_time = input("Enter Check-in Time (e.g., 09:15 AM): ").strip()
        if check_in_time == "":
            print("\n❌ Error: Check-in Time is missing. Please re-enter the time.\n")
            continue
        break
    attendance[student_name] = check_in_time
    print(f"\n✅ Entry recorded for {student_name}")
print("\n--- Data Collection Complete ---")

# Task 5 (Optional) Implementation

print("\n\n--- Absentee Calculation ---")

# Ask the user for the total number of students in the class

total_present = len(attendance)
while True:
    try:
        total_class_strength = int(input("Enter the TOTAL number of students in the class: "))
        if total_class_strength < total_present:
            print(f"❌ Error: Total strength ({total_class_strength}) cannot be less than Total Present ({total_present}). Please re-enter.")
            continue
        if total_class_strength < 0:
            print("❌ Error: Total strength cannot be negative. Please re-enter.")
            continue
        break
    except ValueError:
        print("❌ Error: Invalid input. Please enter a whole number.")


# Total Absent
total_absent = total_class_strength - total_present

print(f"\nTotal Class Strength recorded: {total_class_strength}\n")
print("--- Calculation Complete ---")

# Task 4 Implementation

print("\n\n=============== ATTENDANCE SUMMARY ===============")
print("Student Name\t\tCheck-in Time")
print("--------------------------------------------------")

for name, time in attendance.items():
    # f-string formatting for alignment
    print(f"{name:<20}\t{time}") # <20 ensures min 20 characters for name

# Total Students Present
print("--------------------------------------------------")
print(f"Total Students Present: {total_present}")
print(f"Total Students Absent:  {total_absent}")
print(f"Total Class Strength:   {total_class_strength}")
print("==================================================")


# Task 6 (Bonus) Save Attendance Report to File

save_permission = input("\nDo you want to save the attendance record to a file? (yes/no): ").strip().lower()

if save_permission == 'yes':
    
    now = datetime.datetime.now()
    report_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    report_filename = "attendance_log.txt"

    
    # formatting report content
    report_content = f"K.R. MANGALAM UNIVERSITY ATTENDANCE REPORT\n"
    report_content += f"Generated On: {report_date_time}\n"
    report_content += "--------------------------------------------------\n"
    
    # Student Data
    report_content += "Student Name\t\tCheck-in Time\n"
    report_content += "--------------------------------------------------\n"
    for name, time in attendance.items():
        # f-string formatting for alignment
        report_content += f"{name:<20}\t{time}\n" 
    
    # Summary Data
    report_content += "--------------------------------------------------\n"
    report_content += f"Total Students Present: {total_present}\n"
    report_content += f"Total Students Absent:  {total_absent}\n"
    report_content += f"Total Class Strength:   {total_class_strength}\n"
    report_content += "=================================================="
    
    # File Writing Process
    try:
        with open(report_filename, 'w') as file:
            file.write(report_content)
        
        print(f"\n✅ SUCCESS: Attendance report saved to '{report_filename}'")
        
    except IOError:
        print(f"\n❌ ERROR: Could not write the file {report_filename}.")

else:
    print("\nFile saving skipped.")

print("\n---------------------------------------------------------")
print("Program finished. Thank you for using Attendance Tracker.")