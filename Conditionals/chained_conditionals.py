import conditionals as condMod
# Some times we have more than two alternative branches to execute.
""" Chained conditionals are more than two mutually exclusive execution branches
Let's assume we need to assign letter grades to our students"""

def main():

    puntuation = get_puntuation()

    print(gpa(grade(puntuation)))

def get_puntuation():
    while True:
        x = float(input("Por favor ingrese la puntuacion para esta materia:? "))
        if x > 0:
            break
    return x

def grade(puntuation):
    if puntuation >= 90:
        return "A"
    elif puntuation >= 80:
        return "B"
    elif puntuation >= 70:
        return "C"
    elif puntuation >= 60:
        return "D"
    elif puntuation >= 0:
        return "F"
    else:
        raise VALUE_ERROR

def gpa(grade):

    match grade:
        case "A":
            return f"Grade {grade} is SUMMA CUM LAUDE"
        case "B":
            return f"Grade {grade} is MAGNA CUM LAUDE"
        case "C":
            return f"Grade {grade} is CUM LAUDE"
        case "D":
            return f"Grade {grade} is GRADUATION CONGRATULATIONS"
        case "F":
            return f"Grade {grade} is HOPE YOU ACHIEVE GOALS SOON"
        case _:
            return f"Grade {grade} is NOT AN IDENTIFIABLE GRADE"

condMod.set_testing(condMod.c_ON)

if condMod.is_testing():
    main()




