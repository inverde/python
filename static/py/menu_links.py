# Declare globals types

menu_type = {
    [
        {"label_en", str, "label_es":str, "url":str}
    ]
}

school_menu = menu_type
admin_menu = menu_type

def menu_entry(menu:dir = school_menu, label_en, label_es:str = 'None', url_link:str)-> None:
    menu["en"].append({"label":label_en, "url": url_link})
    menu["es"].append({"label": label_es, "url": url_link})


