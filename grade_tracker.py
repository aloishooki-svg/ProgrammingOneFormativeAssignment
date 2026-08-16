
# Parent class for all assignments
class Assignment:

    def __init__(self, subject, title, score, max_score, due_date, atype):
        # Store the subject
        self.subject = subject.lower().strip()

        # Store the assignment title
        self.title = title.strip()

        # Store scores as numbers
        self.score = float(score)
        self.max_score = float(max_score)

        # Store due date
        self.due_date = due_date.strip()

        # Store assignment type
        self.type = atype.lower().strip()

    # Calculate percentage score
    def percentage(self):
        return (self.score / self.max_score) * 100

    # Display assignment information
    def display(self):
        print(f"Subject: {self.subject.title()}")
        print(f"Title: {self.title}")
        print(f"Score: {self.score:g}/{self.max_score:g}")
        print(f"Percentage: {self.percentage():.2f}%")
        print(f"Due Date: {self.due_date}")
        print(f"Type: {self.type.title()}")
        print("-" * 45)

        # Homework inherits from Assignment
class Homework(Assignment):

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(
            subject,
            title,
            score,
            max_score,
            due_date,
            "homework"
        )


# Exam inherits from Assignment
class Exam(Assignment):

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(
            subject,
            title,
            score,
            max_score,
            due_date,
            "exam"
        )
        # GradeTracker manages all assignments
class GradeTracker:

    def __init__(self):
        # Store assignments in memory
        self.assignments = []

    # Add homework
    def add_homework(self):

        print("\n--- Add Homework ---")

        subject = input("Subject: ")
        title = input("Title: ")
        score = float(input("Score: "))
        max_score = float(input("Maximum score: "))
        due_date = input("Due date (YYYY-MM-DD): ")

        # Create a Homework object
        homework = Homework(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        # Add homework to the assignment list
        self.assignments.append(homework)

        print("Homework added successfully!")

    # Add exam
    def add_exam(self):

        print("\n--- Add Exam ---")

        subject = input("Subject: ")
        title = input("Title: ")
        score = float(input("Score: "))
        max_score = float(input("Maximum score: "))
        due_date = input("Due date (YYYY-MM-DD): ")

        # Create an Exam object
        exam = Exam(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        # Add exam to the assignment list
        self.assignments.append(exam)

        print("Exam added successfully!")

          # List all assignments
    def list_assignments(self):

        print("\n--- All Assignments ---")

        # Check if there are no assignments
        if not self.assignments:
            print("No assignments available.")
            return

        # Display each assignment
        for number, assignment in enumerate(
            self.assignments,
            start=1
        ):
            print(f"\nAssignment {number}")

            # Use the display method from Assignment
            assignment.display()


               # Filter assignments
    def filter_assignments(self):

        # Check if there are no assignments
        if not self.assignments:
            print("\nNo assignments available.")
            return

        print("\n--- Filter Assignments ---")
        print("1) By subject")
        print("2) By type")
        print("3) By month")
        print("0) Back")

        # Get filter choice
        choice = input("Choose a filter: ").strip()

        # Store matching assignments
        results = []

        # Filter by subject
        if choice == "1":

            subject = input(
                "Enter subject: "
            ).lower().strip()

            for assignment in self.assignments:

                if assignment.subject == subject:
                    results.append(assignment)

        # Filter by homework or exam
        elif choice == "2":

            atype = input(
                "Enter type (homework/exam): "
            ).lower().strip()

            if atype not in ["homework", "exam"]:
                print("Invalid type.")
                return

            for assignment in self.assignments:

                if assignment.type == atype:
                    results.append(assignment)

        # Filter by month
        elif choice == "3":

            month = input(
                "Enter month (YYYY-MM): "
            ).strip()

            for assignment in self.assignments:

                if assignment.due_date.startswith(month):
                    results.append(assignment)

        # Return to the main menu
        elif choice == "0":
            return

        # Invalid filter choice
        else:
            print("Invalid filter choice.")
            return

        # Check whether anything matched
        if not results:
            print("\nNo matching assignments found.")
            return

        # Display matching assignments
        print("\n--- Filter Results ---")

        for number, assignment in enumerate(
            results,
            start=1
        ):
            print(f"\nAssignment {number}")
            assignment.display()

              # Show grade summary
    def show_summary(self):

        print("\n--- Grade Summary ---")

        # Check if there are no assignments
        if not self.assignments:
            print("No assignments available.")
            return

        # Calculate the overall average
        total_percentage = 0

        for assignment in self.assignments:
            total_percentage += assignment.percentage()

        overall_average = (
            total_percentage / len(self.assignments)
        )

        print(
            f"Overall average: "
            f"{overall_average:.2f}%"
        )

        # Create a dictionary to store scores by subject
        subjects = {}

        for assignment in self.assignments:

            subject = assignment.subject

            if subject not in subjects:
                subjects[subject] = []

            subjects[subject].append(
                assignment.percentage()
            )

        # Display the average for each subject
        print("\nPer-subject averages:")

        for subject, scores in subjects.items():

            average = sum(scores) / len(scores)

            print(
                f"{subject.title()}: "
                f"{average:.2f}%"
            )

        # Find the highest scoring assignment
        highest = max(
            self.assignments,
            key=lambda assignment:
            assignment.percentage()
        )

        # Find the lowest scoring assignment
        lowest = min(
            self.assignments,
            key=lambda assignment:
            assignment.percentage()
        )

        print("\nHighest scoring assignment:")

        print(
            f"{highest.title} - "
            f"{highest.percentage():.2f}%"
        )

        print("\nLowest scoring assignment:")

        print(
            f"{lowest.title} - "
            f"{lowest.percentage():.2f}%"
        )


# Main program
def main():

    # Create the GradeTracker
    tracker = GradeTracker()

    # Keep showing the menu
    while True:

        print("\n========================================")
        print(" STUDENT GRADE/ASSIGNMENT TRACKER")
        print("========================================")
        print("1) Add homework")
        print("2) Add exam")
        print("3) List assignments")
        print("4) Filter assignments")
        print("5) Show summary")
        print("0) Exit")

        # Get the user's choice
        choice = input("Choose an option: ")

        # Add homework
        if choice == "1":
            tracker.add_homework()

        # Add exam
        elif choice == "2":
            tracker.add_exam()

        # List assignments
        elif choice == "3":
            tracker.list_assignments()

        # Filter assignments
        elif choice == "4":
            tracker.filter_assignments()
            

        # Show grade summary
        elif choice == "5":
            tracker.show_summary()

        # Exit the program
        elif choice == "0":
            print("Goodbye!")
            break

        # Handle invalid choices
        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
        