# Declare globals types

menu_linktype = {"en":{"url":str, "label":str},
                 "es":{"url":str, "label":str}
}

school_menu = menu_linktype

def menu_entry(menu:dir, label:str, url:str)-> None:
    global lang
    if lang=="es":
        

