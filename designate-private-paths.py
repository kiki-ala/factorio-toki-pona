#!/bin/python
import configparser

global CFG_FILENAME
CFG_FILENAME = ".private.cfg"

global PROJECTS
PROJECTS = [
    {
        "name": "factp",
        "paths": [
            {
                "name": "datadir",
                "desc": "factorio game data directory full path",
                "example": "somewhere ... steamapps/common/Factorio/data"
            },
            {
                "name": "moddir",
                "desc": "factorio mods directory",
                "example": "~/.factorio/mods"
            },
        ]
    }
]

if __name__ == "__main__":
    config = configparser.ConfigParser()
    with open(CFG_FILENAME, 'r', encoding='utf8') as f:
        config.read_file(f)
    print(f"projects: {[p["name"] for p in PROJECTS]}")
    if len(PROJECTS) > 1:
        pname = input("which project?\n")
        for projdef in PROJECTS:
            if pname == projdef["name"]:
                project = projdef
                break
    else:
        pname = "factorio"
        project = PROJECTS[0]

    if pname == "factorio":
        section_names = config.sections()
        for pe in project:
            if pe == "name":
                continue
            print(f"--> configuring {pname}-{pe}")
            obj = project[pe]
            for i, e in enumerate(obj):
                name = e["name"]
                desc = e["desc"]
                example = e["example"]
                print(f"\n{name}: {desc}\nexample: {example}\n")
                config[f"{pname}-{pe}"][f'{project[pe][i]["name"]}'] = input("--> provide it: ")

    with open(CFG_FILENAME, 'w', encoding='utf8') as f:
        config.write(f, space_around_delimiters=False)
