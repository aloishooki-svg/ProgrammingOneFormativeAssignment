



# ASSIGNMENT PARENT CLASS


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



# HOMEWORK SUBCLASS


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



# EXAM SUBCLASS


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



# GRADE TRACKER CLASS


# GradeTracker manages all assignments
class GradeTracker:

    def __init__(self):

        # Store assignments in memory
        self.assignments = []

    
    # INPUT VALIDATION METHODS
    

    # Get text input and make sure it is not empty
    def get_text(self, message):

        while True:

            value = input(message).strip()

            if value:
                return value

            print("Input cannot be empty. Please try again.")

    # Get a valid maximum score
    def get_max_score(self):

        while True:

            try:

                max_score = float(
                    input("Maximum score: ")
                )

                # Maximum score must be greater than zero
                if max_score <= 0:

                    print(
                        "Maximum score must be greater than zero."
                    )

                    continue

                return max_score

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    # Get a valid score
    def get_score(self, max_score):

        while True:

            try:

                score = float(
                    input("Score: ")
                )

                # Score cannot be negative
                if score < 0:

                    print(
                        "Score cannot be negative."
                    )

                    continue

                # Score cannot be greater than maximum
                if score > max_score:

                    print(
                        "Score cannot be greater "
                        "than maximum score."
                    )

                    continue

                return score

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    # Get a valid date
    def get_date(self):

        while True:

            date = input(
                "Due date (YYYY-MM-DD): "
            ).strip()

            # Check basic YYYY-MM-DD format
            if (
                len(date) == 10
                and date[4] == "-"
                and date[7] == "-"
            ):

                try:

                    year = int(date[0:4])
                    month = int(date[5:7])
                    day = int(date[8:10])

                    # Check valid date ranges
                    if (
                        year > 0
                        and 1 <= month <= 12
                        and 1 <= day <= 31
                    ):

                        return date

                except ValueError:

                    pass

            print(
                "Invalid date. Please use YYYY-MM-DD."
            )

    # ADD HOMEWORK
    

    # Add homework
    def add_homework(self):

        print("\n--- Add Homework ---")

        # Get valid subject
        subject = self.get_text("Subject: ")

        # Get valid title
        title = self.get_text("Title: ")

        # Get valid maximum score
        max_score = self.get_max_score()

        # Get valid score
        score = self.get_score(max_score)

        # Get valid due date
        due_date = self.get_date()

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

    
    # ADD EXAM
    

    # Add exam
    def add_exam(self):

        print("\n--- Add Exam ---")

        # Get valid subject
        subject = self.get_text("Subject: ")

        # Get valid title
        title = self.get_text("Title: ")

        # Get valid maximum score
        max_score = self.get_max_score()

        # Get valid score
        score = self.get_score(max_score)

        # Get valid due date
        due_date = self.get_date()

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

    
    # LIST ASSIGNMENTs

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

    
    # FILTER ASSIGNMENTS

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

        
        # Filter by type
        

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

            # Check basic month format
            if (
                len(month) != 7
                or month[4] != "-"
            ):

                print(
                    "Invalid month format. "
                    "Please use YYYY-MM."
                )

                return

            try:

                year = int(month[0:4])
                month_number = int(month[5:7])

                if year <= 0 or not 1 <= month_number <= 12:

                    print(
                        "Invalid month. "
                        "Please use a valid YYYY-MM."
                    )

                    return

            except ValueError:

                print(
                    "Invalid month. "
                    "Please use YYYY-MM."
                )

                return

            for assignment in self.assignments:

                if assignment.due_date.startswith(month):

                    results.append(assignment)

        
        # Return to main menu


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

    
    # GRADE SUMMARY
    

    # Show grade summary
    def show_summary(self):

        print("\n--- Grade Summary ---")

        # Check if there are no assignments
        if not self.assignments:

            print("No assignments available.")
            return

        
        # Calculate overall average
        

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

        
        # Calculate per-subject averages
        

        # Dictionary for subject scores
        subjects = {}

        for assignment in self.assignments:

            subject = assignment.subject

            if subject not in subjects:

                subjects[subject] = []

            subjects[subject].append(
                assignment.percentage()
            )

        print("\nPer-subject averages:")

        for subject, scores in subjects.items():

            average = sum(scores) / len(scores)

            print(
                f"{subject.title()}: "
                f"{average:.2f}%"
            )


        # Find highest scoring assignment
    

        highest = max(
            self.assignments,
            key=lambda assignment:
            assignment.percentage()
        )

        
        # Find lowest scoring assignment
        

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



# MAIN PROGRAM


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
        choice = input("Choose an option: ").strip()

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

            print(
                "Invalid menu choice. "
                "Please choose 0, 1, 2, 3, 4, or 5."
            )

# START THE PROGRAM
#

if __name__ == "__main__":
    main()