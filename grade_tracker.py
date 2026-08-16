
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