phoneBook = {
            'Manuel Oscar De Los Santos': 809905551,
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
                'major': 'Computer Sciences',
                'studentID': 180584,
                'GPA': 3.60,
                'coursesTaken': ['Python', 'C Language', 'Algorithms', 'Web Development'],
                'academicLoad': ['Data Science', 'Pre-Algebra']
            }
}]

for classmate in phoneBook:
    print(classmate, phoneBook[classmate])
    print(classmate, f"{phoneBook[classmate]: 000-000-0000}")


