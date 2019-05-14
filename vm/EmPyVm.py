#Embungo vm

class Commands:
    class Jumps:
        def jump(parent,a):
            if type(a) != int:
                a = int(a)
            parent.headLocation = a-1
            return True

        def jumpPos(parent,a):
            if type(a) != int:
                a = int(a)
            if parent.acc > 0:
                parent.headLocation = a-1
            return True
        
        def jumpNeg(parent,a):
            if type(a) != int:
                a = int(a)
            if parent.acc < 0:
                parent.headLocation = a-1
            return True

        def jumpZero(parent,a):
            if type(a) != int:
                a = int(a)
            if parent.acc == 0:
                parent.headLocation = a-1
            return True

        def done(parent,a):
            return False

        commands = {
            "jump":jump,
            "jumpifpos":jumpPos,
            "jumpifneg":jumpNeg,
            "jumpifzero":jumpZero,
            "done":done
        }

    class Mem:
        def load(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc = int(parent.getDat(a-1)[0])
            return True

        def store(parent,a):
            if type(a) != int:
                a = int(a)
            parent.tape[a-1] = parent.acc
            return True

        def seta(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc = a
            return True

        commands = {
            "load":load,
            "store":store,
            "set":seta
        }

    class Math:
        def add(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc += int(parent.getDat(a-1)[0])
            return True

        def sub(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc -= int(parent.getDat(a-1)[0])
            return True

        def mult(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc *= int(parent.getDat(a-1)[0])
            return True

        def div(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc = parent.acc // int(parent.getDat(a-1)[0])
            return True

        def mod(parent,a):
            if type(a) != int:
                a = int(a)
            parent.acc = parent.acc % int(parent.getDat(a-1)[0])
            return True

        commands = {
            "add":add,
            "sub":sub,
            "mult":mult,
            "div":div,
            "mod":mod
        }

    class Io:
        def aprint(parent,a):
            print(chr(parent.acc),end="")
            return True

        def vprint(parent,a):
            print(parent.acc, end="")
            return True

        def inp(parent,a):
            inpu = input()
            try:
                inpu = int(inpu)
            except:
                inpu = ord(inpu[0])
            parent.acc = inpu
            return True

        def run(parent,a):
            b = Vm(parent.fileLocation.rsplit("/",1)[0] + "/" + a)
            b.acc = parent.acc
            b.runTape()
            parent.acc = b.acc
            return True
            
        commands = {
            "aprint":aprint,
            "vprint":vprint,
            "input":inp,
            "run":run
        }

#######
class Vm:
    def __init__(this, location):
        this.tape = []
        with open(location) as f:
            for line in f:
                this.tape.append(line.replace("\n",""))
        this.fileLocation = location
        this.headLocation = 0
        this.acc = 0
        
        this.commands = {}
        this.commands.update(Commands.Jumps.commands)
        this.commands.update(Commands.Mem.commands)
        this.commands.update(Commands.Io.commands)
        this.commands.update(Commands.Math.commands)

    def runTape(this):
        while(True):
            command = this.getDat(this.headLocation)
            #print(command)
            this.headLocation += 1
            if this.runCommand(command) == False:
                return

    def getDat(this,line):
        if type(this.tape[line]) == int:
            return [this.tape[line]] #Expected to return an array
        
        command = this.tape[line].split("//")[0].split(" ")
        while command.count(""):
            command.remove("")
        return command

    def runCommand(this,command):
        if len(command) == 0:
            #print(">> ERR: Tried to execute an empty line") 
            return True
        
        com = command[0].lower()
        func = this.commands.get(com)

        if func == None:
            print(">> ERR: Tried to execute an invalid command :",com,this.fileLocation)
            return False

        if len(command) == 1:
            return func(this,None)

        return func(this,command[1])

#######

if __name__ == "__main__":
    import sys
    
    try:
        a = Vm(sys.argv[1])
    except:
        print(">> ERR: Unable to load program")
        exit()

    if(len(sys.argv) >= 3):
        a.acc = int(sys.argv[2])

    a.runTape()
