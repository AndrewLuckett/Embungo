'''
Gui folder/file selector and then calls EmPyVm.py with the args
'''

def getFolder():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(title="Select Embungo File",
                                      filetypes=[("Text File", "txt em")])
    root.destroy()
    return filename

def main():
    global path
    path = getFolder()
    if path is None or path == "":
        return

    import EmPyVm
    a = EmPyVm.Vm(path)
    a.runTape()
    input("Press Enter to close")

if __name__ == "__main__":
    main()
