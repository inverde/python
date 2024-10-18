students =  [{
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

for key in range(len(students)):
    print(students[key]['electoral_id'], students[key])
