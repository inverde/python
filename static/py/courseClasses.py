from typing import List

class EnglishRows:
    def __init__(self, data: dict):
        self.PurposeAndImportance_EN = data.get("PurposeAndImportance_EN")
        self.CoreThemes_EN = data.get("CoreThemes_EN")
        self.UnitOutcomes_EN = data.get("UnitOutcomes_EN")
        self.Objectives_EN = data.get("Objectives_EN")
        self.WarmUp_EN = data.get("WarmUp_EN")
        self.KeyActivities_EN = data.get("KeyActivities_EN")
        self.DiscussionTopics_EN = data.get("DiscussionTopics_EN")
        self.CheckpointLabs_EN = data.get("CheckpointLabs_EN")
        self.AcademicMaterials_EN = data.get("AcademicMaterials_EN")
        self.Skills_EN = data.get("Skills_EN")
        self.Careers_EN = data.get("Careers_EN")


class SpanishRows:
    def __init__(self, data: dict):
        self.PurposeAndImportance_ES = data.get("PurposeAndImportance_ES")
        self.CoreThemes_ES = data.get("CoreThemes_ES")
        self.UnitOutcomes_ES = data.get("UnitOutcomes_ES")
        self.Objectives_ES = data.get("Objectives_ES")
        self.WarmUp_ES = data.get("WarmUp_ES")
        self.KeyActivities_ES = data.get("KeyActivities_ES")
        self.DiscussionTopics_ES = data.get("DiscussionTopics_ES")
        self.CheckpointLabs_ES = data.get("CheckpointLabs_ES")
        self.AcademicMaterials_ES = data.get("AcademicMaterials_ES")
        self.Skills_ES = data.get("Skills_ES")
        self.Careers_ES = data.get("Careers_ES")


class Lesson:
    def __init__(self, data: dict):
        self.LessonTitle = data.get("LessonTitle")
        self.EnglishRows = EnglishRows(data.get("EnglishRows", {}))
        self.SpanishRows = SpanishRows(data.get("SpanishRows", {}))


class Chapter:
    def __init__(self, data: dict):
        self.ChapterTitle = data.get("ChapterTitle")
        self.LessonTitles: List[Lesson] = [Lesson(ld) for ld in data.get("LessonTitles", [])]

class Course:
    def __init__(self, data: dict):
        self.CourseTitle = data.get("CourseTitle")
        self.ChapterTitles: List[Chapter] = [Chapter(cd) for cd in data.get("ChapterTitles", [])]
        self.CurrentYear = data.get("CurrentYear")
        self.CourseVersion = data.get("CourseVersion")
        self.LastUpdated = data.get("LastUpdated")
        self.CourseURL = data.get("CourseURL")
