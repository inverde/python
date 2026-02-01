
course = {
    "CourseTitle": str,              # string
    "ChapterTitles": [               # list of chapters
        {
            "ChapterTitle": str,     # string
            "LessonTitles": [        # list of lessons
                {
                    "LessonTitle": str,   # string
                    "EnglishRows": {      # dict of English fields
                        "PurposeAndImportance_EN": str,
                        "CoreThemes_EN": str,
                        "UnitOutcomes_EN": str,
                        "Objectives_EN": str,
                        "WarmUp_EN": str,
                        "KeyActivities_EN": str,
                        "DiscussionTopics_EN": str,
                        "CheckpointLabs_EN": str, 
                        "AcademicMaterials_EN": str,
                        "Skills_EN": str,
                        "Careers_EN": str
                    },
                    "SpanishRows": {      # dict of Spanish fields
                        "PurposeAndImportance_ES": str,
                        "CoreThemes_ES": str,
                        "UnitOutcomes_ES": str,
                        "Objectives_ES": str,
                        "WarmUp_ES": str,
                        "KeyActivities_ES": str,
                        "DiscussionTopics_ES": str,
                        "CheckpointLabs_ES": str,
                        "AcademicMaterials_ES": str,
                        "Skills_ES": str,
                        "Careers_ES": str
                    }
                }
            ]
        }
    ],
    "CurrentYear": int,              # integer
    "CourseVersion": str,            # string
    "LastUpdated": str,              # ISO date string (e.g. "YYYY-MM-DD")
    "CourseURL": str                 # URI string
}
courses = list[course]

lesson = {
    "CourseTitle": str,
    "ChapterNumber": int,            # integer
    "ChapterTitle": str,             # string
    "LessonTitle": str,              # string
    "LessonNumber": int,             # integer
    "EnglishRows": {                 # dict of English fields
        "PurposeAndImportance_EN": str,
        "CoreThemes_EN": str,
        "UnitOutcomes_EN": str,
        "Objectives_EN": str,
        "WarmUp_EN": str,
        "KeyActivities_EN": str,
        "DiscussionTopics_EN": str,
        "CheckpointLabs_EN": str,
        "AcademicMaterials_EN": str,
        "Skills_EN": str,
        "Careers_EN": str
    },
    "SpanishRows": {                 # dict of Spanish fields
        "PurposeAndImportance_ES": str,
        "CoreThemes_ES": str,
        "UnitOutcomes_ES": str,
        "Objectives_ES": str,
        "WarmUp_ES": str,
        "KeyActivities_ES": str,
        "DiscussionTopics_ES": str,
        "CheckpointLabs_ES": str,
        "AcademicMaterials_ES": str,
        "Skills_ES": str,
        "Careers_ES": str
    }
}
englishRows = {
    "PurposeAndImportance_EN": str,
    "CoreThemes_EN": str,
    "UnitOutcomes_EN": str,
    "Objectives_EN": str,         # string 
    "WarmUp_EN": str,
    "KeyActivities_EN": str,
    "DiscussionTopics_EN": str,
    "CheckpointLabs_EN": str,
    "AcademicMaterials_EN": str,
    "Skills_EN": str,
    "Careers_EN": str
}

spanishRows = {
    "PurposeAndImportance_ES": str,
    "CoreThemes_ES": str,
    "UnitOutcomes_ES": str,
    "Objectives_ES": str,         # string
    "WarmUp_ES": str,
    "KeyActivities_ES": str,
    "DiscussionTopics_ES": str,
    "CheckpointLabs_ES": str,
    "AcademicMaterials_ES": str,
    "Skills_ES": str,
    "Careers_ES": str
}

lessons = list[lesson]

chapter = {
    "CourseTitle": str,
    "ChapterTitle": str,             # string
    "LessonTitles": [                # list of lessons
        lesson                  # lesson dict
    ]
}

