# import csv
# import os
# from django.core.management.base import BaseCommand
# from property_management.models import Student, Teacher

# class Command(BaseCommand):
#     help = "Import Student and Teacher data from CSV files"

#     def handle(self, *args, **kwargs):
#         data_dir = "/app/data"  # Path where CSV files are located inside the Docker container

#         # Import students
#         students_file = os.path.join(data_dir, 'students.csv')
#         self.stdout.write(f'Importing students from {students_file}...')
#         self.import_students(students_file)

#         # Import teachers
#         teachers_file = os.path.join(data_dir, 'teachers.csv')
#         self.stdout.write(f'Importing teachers from {teachers_file}...')
#         self.import_teachers(teachers_file)

#     def import_students(self, file_path):
#         with open(file_path, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 Student.objects.update_or_create(
#                     name=row['name'],
#                     city=row['city'],
#                     cgpa=row['cgpa']
#                 )
#         self.stdout.write(self.style.SUCCESS('Successfully imported students'))

#     def import_teachers(self, file_path):
#         with open(file_path, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 Teacher.objects.update_or_create(
#                     name=row['name'],
#                     city=row['city'],
#                     cgpa=row['cgpa']
#                 )
#         self.stdout.write(self.style.SUCCESS('Successfully imported teachers'))


import csv
from django.core.management.base import BaseCommand
from property_management.models import Student, Teacher


class Command(BaseCommand):
    help = "Import students and teachers data from CSV files"

    def handle(self, *args, **kwargs):
        students_file = "/app/data/students.csv"
        teachers_file = "/app/data/teachers.csv"

        self.import_students(students_file)
        self.import_teachers(teachers_file)

    def import_students(self, file_path):
        self.stdout.write(f"Importing students from {file_path}...")
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Row: {row}")  # Debug: Print row contents
                Student.objects.create(
                    name=row['name'],
                    city=row['city'],
                    cgpa=row['cgpa']
                )
        self.stdout.write(self.style.SUCCESS("Successfully imported students"))

    def import_teachers(self, file_path):
        self.stdout.write(f"Importing teachers from {file_path}...")
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Row: {row}")  # Debug: Print row contents
                Teacher.objects.create(
                    name=row['name'],
                    city=row['city'],
                    cgpa=row['cgpa']
                )
        self.stdout.write(self.style.SUCCESS("Successfully imported teachers"))
