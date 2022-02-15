pwd = ''


def file(pwd):
    return open(pwd, 'a')


def printFile(string):
    print('# ' + str(string) + '\n', file=file(pwd))
