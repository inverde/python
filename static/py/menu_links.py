# Declare globals types

menu_type = {
    "en":[
        {"label":str, "url":str}
    ],
    "es":[
        {"label":str, "url":str}
    ]
}

school_menu = menu_type
admin_menu = menu_type

def menu_entry(menu:dir = school_menu, url:str, label_en, label_es:str = 'None', url_link:str)-> None:
    menu["en"].append({"label":label_en, "url": url_link})
    menu["es"].append({"label": label_es, "url": url_link})


