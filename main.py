from academic_management import AcademicManagementSystem

# Create object and pass directory path
ams = AcademicManagementSystem("student_data")

# Store student records
ams.store_student_info("2024/001", "Twizeye Serge", "Level 5")


# Display all records
ams.read_student_info()