#Embungo vm

class Commands:
    class jumps:
        def jump(a):
            global headLocation
            if type(a) != int:
                a = int(a)
            headLocation = a-2
            return True

        def jumpPos(a):
            global acc, headLocation
            if type(a) != int:
                a = int(a)
            if acc > 0:
                headLocation = a-2
            return True
        
        def jumpNeg(a):
            global acc, headLocation
            if type(a) != int:
                a = int(a)
            if acc < 0:
                headLocation = a-2
            return True

        def jumpZero(a):
            global acc, headLocation
            if type(a) != int:
                a = int(a)
            if acc == 0:
                headLocation = a-2
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

    class mem:
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

    class math:
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

    class io:
        def aprint(a):
            global acc
            print(chr(acc),end="")
            return True

        def vprint(a):
            global acc
            print(acc, end="")
            return True

        commands = {
            "aprint":aprint,
            "vprint":vprint
        }

#######

headLocation = 0
acc = 0
tape = []
commands = {}

commands.update(Commands.jumps.commands)
commands.update(Commands.mem.commands)
commands.update(Commands.io.commands)
commands.update(Commands.math.commands)

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
        if runCommand(command) == False:
            return

        headLocation += 1

def getDat(line):
    global tape
    command = tape[line].split("//")[0].split(" ")
    while command.count(""):
        command.remove("")
    return command

def runCommand(command):
    global acc,headLocation
    if len(command) == 0:
        print(">> ERR: Tried to execute an empty line") 
        return False
    com = command[0].lower()

    func = commands.get(com)

    if func == None:
        print(">> ERR: Tried to execute an invalid command")
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
