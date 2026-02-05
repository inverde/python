# Declare globals types

menu_linktype = {"en":{"label":str, "url":str},
                 "es":{"label":str, "url":str}
}

school_menu = menu_linktype

def menu_entry(menu:dir = school_menu, url:str, label_en, label_es:str = 'None', url_link:str)-> None:
    menu["en"]["label"] = label_en
    menu["es"]["url"] = url_link


