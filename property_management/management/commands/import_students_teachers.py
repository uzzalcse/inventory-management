import csv
from django.core.management.base import BaseCommand
from property_management.models import Student, Teacher

class Command(BaseCommand):
    help = 'Import student and teacher data from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('students_csv', type=str, help='Path to the students CSV file')
        parser.add_argument('teachers_csv', type=str, help='Path to the teachers CSV file')

    def handle(self, *args, **kwargs):
        students_csv = kwargs['students_csv']
        teachers_csv = kwargs['teachers_csv']

        # Import students
        try:
            with open(students_csv, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    name, city, cgpa = row
                    cgpa = float(cgpa)  # Ensure CGPA is stored as a float
                    Student.objects.create(name=name, city=city, cgpa=cgpa)
                self.stdout.write(self.style.SUCCESS('Successfully imported students'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing students: {e}'))

        # Import teachers
        try:
            with open(teachers_csv, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    name, city, cgpa = row
                    cgpa = float(cgpa)  # Ensure CGPA is stored as a float
                    Teacher.objects.create(name=name, city=city, cgpa=cgpa)
                self.stdout.write(self.style.SUCCESS('Successfully imported teachers'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing teachers: {e}'))
