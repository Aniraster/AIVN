import time

def writeFile(userInput):
    f = open("../text.txt", "w")
    data = ['1', userInput]
    f.seek(0)
    f.truncate()
    f.writelines(data)
    f.close()


def checkFile():
    active = True
    while active:
        f = open("../text.txt", "r")
        prompt = f.read()
        if prompt[:1] == '0':
            active = False
        time.sleep(0.300)
        f.close()
    return prompt[1:]

def writeRead(text):
    writeFile(text)
    return(checkFile())
