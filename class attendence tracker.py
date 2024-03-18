class AttendanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name.strip() == "":
            print("Please enter a valid student name.")
            return
        if name not in self.students:
            self.students[name] = []
            print(f"Student '{name}' added successfully.")
        else:
            print(f"Student '{name}' already exists.")

    def mark_attendance(self, name, date):
        if name not in self.students:
            print(f"Student '{name}' not found.")
            return
        if date.strip() == "":
            print("Please enter a valid date.")
            return
        self.students[name].append(date)
        print(f"Attendance for '{name}' marked on {date}.")

    def view_attendance(self, name):
        if name not in self.students:
            print(f"Student '{name}' not found.")
            return
        if not self.students[name]:
            print(f"No attendance records found for '{name}'.")
            return
        print(f"Attendance for '{name}':")
        for date in self.students[name]:
            print(date)


def main():
    attendance_tracker = AttendanceTracker()

    print("\nWelcome to the Attendance Tracker!")

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            attendance_tracker.add_student(name)

        elif choice == '2':
            name = input("Enter student name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            attendance_tracker.mark_attendance(name, date)

        elif choice == '3':
            name = input("Enter student name: ")
            attendance_tracker.view_attendance(name)

        elif choice == '4':
            print("Exiting the Attendance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
