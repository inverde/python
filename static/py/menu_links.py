# Declare globals types

menu_type = {
                "school":[
                    {"label_en":str, "label_es":str, "url":str}
                ],
                "admin":[
                    {"label_en":str, "label_es":str, "url":str}
                ]
}

lang = "es"


school_menu = menu_type
admin_menu = menu_type
courses_menu = menu_type


def menu_entry(label_en:str,url_link:str, label_es:str = 'None', menu:dir = courses_menu)-> None:
    menu.append({"label_en":label_en, "label_es":label_es, "url": url_link})



