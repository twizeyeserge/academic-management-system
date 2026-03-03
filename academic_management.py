from pathlib import Path

class AcademicManagementSystem:
    def __init__(self, directory_path):
        # Store directory path
        self.directory_path = Path(directory_path)

        # Create directory if it does not exist
        if not self.directory_path.exists():
            self.directory_path.mkdir(parents=True)

        # Define students file path
        self.students_file = self.directory_path / "students.txt"

    def store_student_info(self, reg_no, name, level):
        # Open file in append mode
        with self.students_file.open("a", encoding="utf-8") as file:
            file.write(f"RegNo: {reg_no}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Level: {level}\n")
            file.write("------------------\n")

    def read_student_info(self):
        # Check if file exists
        if not self.students_file.exists():
            print("No student records found.")
            return

        # Read and display file content
        with self.students_file.open("r", encoding="utf-8") as file:
            content = file.read()
            print("STUDENT RECORDS")
            print("------------------")
            print(content)