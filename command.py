import json

with open("keywords.json", "r", encoding="utf-8") as file:
    jsonFile = json.loads(file.read())

# functionDict = jsonFile['Function']
# moduleDict = jsonFile['Module']
# normalDict = jsonFile['Normal']


class cmd:
    line = ''
    cd = ''


def addcmd(string):
    cmd.line += string


def WriteCmd(title):
    addcmd('cd ' + title)
    keys = jsonFile[title].keys()
    for k in keys:
        addcmd("\ncd " + str(k)+'\ntouch')
        for n in jsonFile[title][k]:
            addcmd(" " + n + ".py")
        addcmd('\ncd ..\n')
    addcmd('cd ..\n')

WriteCmd('Normal')
WriteCmd('Module')
WriteCmd('Function')


print(cmd.line)
