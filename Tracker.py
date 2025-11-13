# Name: Tushar Singh
# Date: 12/11/2025 
# Assignment: Attendance Tracker

import csv
from datetime import datetime
attendance = {}
def include_attendance():
    print("\n ----------Insert the Entry ----------")
    while True :
        students = input("Enter name of the student :").strip()
        if students =="":
            print("Invalid name")
            continue
        elif students in attendance :
            print("Name is already recorded")
            continue
       
        time = input("Enter arrival time (HH:MM AM/PM) :").strip()
        if time.strip() == " ":
            print("INVALID Enter again")
            continue
        
        attendance[students]= time 
        print(f"{students} Arrived at {time}")

        another = input("do you want to add another record of new student (y/n) :").strip().lower()
        if another != "y":
            break


def record_attendance():
    if len(attendance) == 0:
        print("\n No records found ")
        return

    print("\n ========== ATTENDANCE  ==========\n ")
    print("Student Name\t\t Arrival Time")
    print("-------------------------------------------")

    for student, arrive in attendance.items():
        print(f"{student}\t\t{arrive}")

    print("-------------------------------------------")
    print(f"Total Students Present: {len(attendance)}")

def file_csv():
    if len(attendance) == 0:
        print("\n No records present.")
        return

    filename = "attendance_log.csv"
    n = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([" Attendance "])
        writer.writerow([f"Generated on: {n}"])
        writer.writerow([])
        writer.writerow(["Student Name", "Arrival Time"])

        for student, time in attendance.items():
            writer.writerow([student, time])

        writer.writerow([])
        writer.writerow(["Total Students Present", len(attendance)])

    print(f"\n Attendance has been saved to '{filename}'")

def absent_student():
    if len(attendance) == 0:
        print("\nThe record is empty")
        return
    try:
        total = int(input("\n Enter total number of students in class: "))
        absent = total - len(attendance1)
        print(f"Total Present: {len(attendance)}")
        print(f"Total Absent: {absent}")
    except:
        print("Invalid number. Try again.")

def menu_view():
    while True:
        print("=========================")
        print("\n========== MENU ==========")
        print("1. Insert Attendance")
        print("2. View the saved attendance")
        print("3. Save inside CSV file")
        print("4. Number of students absent")
        print("5. Exit")
        print("==========================")

        choice = input(" Your choice (1-5): ")
        if choice == "1":
            include_attendance()
        elif choice == "2":
            record_attendance()
        elif choice == "3":
            file_csv()
        elif choice == "4":
            absent_student()
        elif choice == "5":
            print("\nThank you for using Attendance Tracker")
            break
        else:
            print("Invalid choice. Try again.")
menu_view()