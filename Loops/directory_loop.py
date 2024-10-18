phoneBook = {
            'Manuel Oscar De Los Santos': 8099095551,
            'Jose Luis Valenzuela': 8098504623,
            'Orlando Herrera': 8099966195,
            'Alexis Ortega':  8297159500,
}
students =  [
            {
             'electoral_id': '00100973486',
             'personal_data': {
                'firstName': 'Manuel',
                'middleName': 'Oscar',
                'lastName': 'De Los Santos',
                'Address': 'Calle Santa Teresa #10, Torre DKI, Apt 7A',
                'telephone': 8099095551,
                'dayOfBirth': '11-06-1961',
                'civilStatus': 'Single'
            },
            'academic_record': {
                'major': 'Ciencias Computacionales',
                'studentID': 180584,
                'GPA': 3.60,
                'coursesTaken': ['Python', 'C Language', 'Algorithms', 'Web Development'],
                'academicLoad': ['Data Science', 'Pre-Algebra']
            }
}]

for classmate in phoneBook:
    formatted_string = f"{str(phoneBook[classmate])[:3]}-{str(phoneBook[classmate])[3:6]}-{str(phoneBook[classmate])[6:]}"
    print(f"El teléfono de {classmate} es {formatted_string}")
print()
for student in students:
    print(f"Estudiante {student['personal_data']['lastName']}, ", end="")
    print(f"matrícula {student['academic_record']['studentID']} ", end="")
    print(f"es de {student['academic_record']['major']}")
print()
print(phoneBook.keys)
print(phoneBook.values)
