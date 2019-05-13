#Embungo vm

class Commands:
    class Jumps:
        def jump(a):
            global headLocation
            if type(a) != int:
                a = int(a)
            headLocation = a-1
            return True

        def jumpPos(a):
            global acc, headLocation
            if type(a) != int:
                a = int(a)
            if acc > 0:
                headLocation = a-1
            return True
        
        def jumpNeg(a):
            global acc, headLocation
            if type(a) != int:
                a = int(a)
            if acc < 0:
                headLocation = a-1
            return True

        def jumpZero(a):
            global acc, headLocation
            if type(a) != int:
                a = int(a)
            if acc == 0:
                headLocation = a-1
            return True

        def done(a):
            return False

        commands = {
            "jump":jump,
            "jumpifpos":jumpPos,
            "jumpifneg":jumpNeg,
            "jumpifzero":jumpZero,
            "done":done
        }

    class Mem:
        def load(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc = int(getDat(a-1)[0])
            return True

        def store(a):
            global acc, tape
            if type(a) != int:
                a = int(a)
            tape[a-1] = acc
            return True

        def seta(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc = a
            return True

        commands = {
            "load":load,
            "store":store,
            "set":seta
        }

    class Math:
        def add(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc += int(getDat(a-1)[0])
            return True

        def sub(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc -= int(getDat(a-1)[0])
            return True

        def mult(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc *= int(getDat(a-1)[0])
            return True

        def div(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc = acc // int(getDat(a-1)[0])
            return True

        def mod(a):
            global acc
            if type(a) != int:
                a = int(a)
            acc = acc % int(getDat(a-1)[0])
            return True

        commands = {
            "add":add,
            "sub":sub,
            "mult":mult,
            "div":div,
            "mod":mod
        }

    class Io:
        def aprint(a):
            global acc
            print(chr(acc),end="")
            return True

        def vprint(a):
            global acc
            print(acc, end="")
            return True

        def inp(a):
            global acc
            inpu = input()
            try:
                inpu = int(inpu)
            except:
                inpu = ord(inpu[0])
            acc = inpu
            return True

        commands = {
            "aprint":aprint,
            "vprint":vprint,
            "input":inp
        }

#######

headLocation = 0
acc = 0
tape = []
commands = {}

commands.update(Commands.Jumps.commands)
commands.update(Commands.Mem.commands)
commands.update(Commands.Io.commands)
commands.update(Commands.Math.commands)

def loadTape(location):
    global tape
    with open(location) as f:
        for line in f:
            tape.append(line.replace("\n",""))

def runTape():
    global headLocation

    while(True):
        command = getDat(headLocation)
        #print(command)
        headLocation += 1
        if runCommand(command) == False:
            return

def getDat(line):
    global tape
    if type(tape[line]) == int:
        return [tape[line]] #Expected to return an array
    
    command = tape[line].split("//")[0].split(" ")
    while command.count(""):
        command.remove("")
    return command

def runCommand(command):
    global acc,headLocation
    if len(command) == 0:
        #print(">> ERR: Tried to execute an empty line") 
        return True
    
    com = command[0].lower()
    func = commands.get(com)

    if func == None:
        print(">> ERR: Tried to execute an invalid command :",com)
        return False

    if len(command) == 1:
        return func(None)

    return func(command[1])

#######

if __name__ == "__main__":
    import sys
    
    try:
        loadTape(sys.argv[1])
    except:
        print(">> ERR: Unable to load program")
        exit()

    if(len(sys.argv) >= 3):
        acc = int(sys.argv[2])

    runTape()
