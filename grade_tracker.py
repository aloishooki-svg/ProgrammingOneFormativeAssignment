
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
        print("0) Exit")

        # Get the user's choice
        choice = input("Choose an option: ")

        # Add homework
        if choice == "1":
            tracker.add_homework()

        # Add exam
        elif choice == "2":
            tracker.add_exam()

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
        