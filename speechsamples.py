import os
import sys
import random
import json

path = '.'

combos = []

genderFilter = ""

if len(sys.argv) == 3 and sys.argv[2].startswith("gender="):
    genderFilter = sys.argv[2].split("=")[1]

for root, dirs, files in os.walk(path):
    dir_name = root.replace(".\\", "").replace("./", "")

    if dir_name == ".":
        continue

    for file in files:
        split = file.split(".")

        if split[1].lower() == "json":
            f = open(root + "\\" + file)
            data = json.load(f)

            obj = {
                "name_raw": split[0]
            }

            gender = ""

            # get voice name
            if "voiceName" in data['games'][0]:
                obj["name"] = data['games'][0]["voiceName"]

            # get gender
            if "gender" in data['games'][0]:
                gender = data['games'][0]["gender"]

            # get from name
            if "gameId" in data['games'][0]:
                obj["game_raw"] = data['games'][0]["gameId"]

                fromFile = open(f"{root}\\..\\..\\assets\\{obj['game_raw']}.json")
                fromFileData = json.load(fromFile)

                if "gameName" in fromFileData:
                    obj["game"] = fromFileData['gameName']

            # if gender filtering is enabled, filter the gender
            if genderFilter != "" and (gender != genderFilter and gender != "other"):
                continue

            obj["gender"] = gender

            combos.append(obj)

if len(sys.argv) > 1:
    if sys.argv[1] == "random":
        print(random.choice(combos))
    elif sys.argv[1] == "csv":
        data = ""

        for name in combos:
            data = f"{data}{name['game_raw']}|{name['name_raw']}||hifi|csv|1\n\r"

        print(data)
    elif sys.argv[1] == "filter":
        data = ""

        for name in combos:
            data = f"{data}{name['game_raw']}|{name['name_raw']}|{name['gender']}|hifi|filter|1"

        print(data)
    elif sys.argv[1] == "demo":
        data = ""

        for name in combos:
            data = f"{data}Hello, my name is {name['name']}, I am from {name['game']} and I am {name['gender']}\n\r"

        print(data)
    elif sys.argv[1] == "democsv":
        data = ""

        for name in combos:
            data = f"{data}{name['game_raw']}|{name['name_raw']}|Hello, my name is {name['name']}, " \
                   f"I am from {name['game']} and I am {name['gender']}|hifi|democsv|1\n\r"

        print(data)
    else:
        print("Command not found")
else:
    for name in combos:
        print(name)

print(f"Returned: {str(len(combos))} voices")