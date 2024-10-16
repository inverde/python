# Some times we have more than two alternative branches to execute.
""" Chained conditionals are more than two mutually exclusive execution branches
Let's assume we need to assign letter grades to our students"""


def grade(puntuation):
    if puntuantion >= 90:
        return A
    elif puntuation >= 80:
        return B
    elif puntuation >= 70:
        return C
    elif puntuation >= 60:
        return D
    elif puntuation >= 0:
        return F
    else:
        raise VALUE_ERROR

def gpa(grade):

    match grade:
        case "A":
            return f"{grade} is SUMMA CUM LAUDE"
        case "B":
            return f"{grade} is MAGNA CUM LAUDE"
        case "C":
            return f"{grade} is CUM LAUDE"
        case "D":
            return f"{grade} is GRADUATION CONGRATULATIONS"
        case "F":
            return f"{grade} is HOPE YOU ACHIEVE GOALS SOON"
        else:
            return f"{grade} is NOT AN IDENTIFIABLE GRADE"





