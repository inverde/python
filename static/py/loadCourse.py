import json
from courseClasses import Course, Chapter, Lesson, EnglishRows, SpanishRows
from courses import lesson as LessonDict, course as CourseDict, chapter as ChapterDict
import flags

# Define initial list of courses to test first version of web app
initial_courses = [
    {
        "CourseName":str,
        "CourseTitle":str,
        "ChapterTitles":list[ChapterDict]
    }
]



def chapterTitles_listtype()->list[dict]:
    course = CourseDict
    return course['ChapterTitles']

def lessonTitles_listtype()->list[dict]:
    chapter = ChapterDict
    return chapter['LessonTitles']

# Global listType
lessonsList = lessonTitles_listtype()

# Global listType
chaptersList = chapterTitles_listtype()

def lessonTitles_list(course_title:str, chapter_title:str) ->list[str]:
    course = CourseDict
    return [lesson["LessonTitle"] for lesson in course[course_title]["ChapterTitles"][chapter_title]["LessonTitles"]]

def set_base_pathDir(course_title:str, chapter_title:str = None) ->str:
    if chapter_title is not None:
        base_pathDir = f"../data/json/{course_title}/{chapter_title}"
    else:
        base_pathDir = f"../data/json/{course_title}"

    return base_pathDir

def print_lesson(lesson_name:str, lesson_data:dict):
    print(f"Lesson: {lesson_name}")
    for key, value in lesson_data.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for sub_key, sub_value in value.items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")

# Load JSON file

def lesson_data_from_json(path_dir, path_file) -> dict:

    with open(f"{path_dir}/{path_file}", "r", encoding="utf-8") as f:
        data = json.load(f)

    lesson_dict = LessonDict
    lesson_dict["CourseTitle"] = data["CourseTitle"]
    lesson_dict["ChapterTitle"] = data["ChapterTitle"]
    lesson_dict["ChapterNumber"] = data["ChapterNumber"]
    lesson_dict["LessonTitle"] = data["LessonTitle"]
    lesson_dict["LessonNumber"] = data["LessonNumber"]
    lesson_dict["EnglishRows"] = data["EnglishRows"]
    lesson_dict["SpanishRows"] = data["SpanishRows"]

    return lesson_dict


def course_data_from_json(path_dir, path_file)-> dict:
    """
    This function goes to data/json directory in the parent directory and looks in a specific course folder for the CourseTitle.
    From here extract all the chapters' basic information for the.
    For each chapter builds a chapter directory that
    will be saved in a list program structure that will be kept in a system data file for easy retrieval.
    """
    # Define chapters list structure

    global chaptersList
    course = CourseDict

    with open(f"{path_dir}/{path_file}", "r", encoding="utf-8") as file:
        data = json.load(file)

    course["CourseTitle"] = data["CourseTitle"]
    chapters = data["Chapters"]
    # Loop through all the chapters
    for chapter in chapters:
        chapter_dict = ChapterDict
        chapter_dict["CourseTitle"] = data["CourseTitle"]
        chapter_dict["ChapterNumber"] = chapter["ChapterNumber"]
        chapter_dict["ChapterTitle_en"] = chapter["ChapterTitle_en"]
        chapter_dict["ChapterTitle_es"] = chapter["ChapterTitle_es"]


    course_dict = {"CourseTitle": data["CourseTitle"], "Chapters": chapters}
    return course_dict


# Set debug mode
flags.set_debug_mode(flags.c_ON)

def main():
    unitOverviewLessonDir =  lesson_data_from_json(f"{set_base_pathDir('AI-Foundations', 'Problem-Solving-With-AI')}", 'unit-overview.json')
    print_lesson("Unit Overview Lesson", unitOverviewLessonDir)
    courseAIFoundationsDir = course_data_from_json(f"{set_base_pathDir('AI-Foundations', None)}", 'chapter_links.json')
    print(json.dumps(courseAIFoundationsDir,indent=4, ensure_ascii=False))

if __name__ == "__main__":
    if flags.is_debug_mode():
        main()
    else:
        print("ai-foundations".upper().title())
        print("Debug mode is off. Enable debug mode to run the main function.")






