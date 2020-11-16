import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_582=tk.Button(root)
        GButton_582["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_582["font"] = ft
        GButton_582["fg"] = "#000000"
        GButton_582["justify"] = "center"
        GButton_582["text"] = "Entrar"
        GButton_582.place(x=300,y=360,width=71,height=31)
        GButton_582["command"] = self.GButton_582_command

        GLineEdit_531=tk.Entry(root)
        GLineEdit_531["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_531["font"] = ft
        GLineEdit_531["fg"] = "#333333"
        GLineEdit_531["justify"] = "center"
        GLineEdit_531["text"] = ""
        GLineEdit_531.place(x=190,y=110,width=205,height=30)

        GLineEdit_547=tk.Entry(root)
        GLineEdit_547["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_547["font"] = ft
        GLineEdit_547["fg"] = "#333333"
        GLineEdit_547["justify"] = "center"
        GLineEdit_547["text"] = ""
        GLineEdit_547.place(x=190,y=170,width=206,height=30)

        GButton_579=tk.Button(root)
        GButton_579["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_579["font"] = ft
        GButton_579["fg"] = "#000000"
        GButton_579["justify"] = "center"
        GButton_579["text"] = "sair"
        GButton_579.place(x=200,y=360,width=67,height=31)
        GButton_579["command"] = self.GButton_579_command

        GLabel_534=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_534["font"] = ft
        GLabel_534["fg"] = "#333333"
        GLabel_534["justify"] = "center"
        GLabel_534["text"] = "Biblioteca UNIESP"
        GLabel_534.place(x=150,y=20,width=267,height=30)

        GLabel_766=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_766["font"] = ft
        GLabel_766["fg"] = "#333333"
        GLabel_766["justify"] = "center"
        GLabel_766["text"] = "__________________________________________________________________________________"
        GLabel_766.place(x=230,y=50,width=150,height=30)

        GLabel_942=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_942["font"] = ft
        GLabel_942["fg"] = "#333333"
        GLabel_942["justify"] = "center"
        GLabel_942["text"] = "usuário"
        GLabel_942.place(x=100,y=110,width=70,height=25)

        GLabel_918=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_918["font"] = ft
        GLabel_918["fg"] = "#333333"
        GLabel_918["justify"] = "center"
        GLabel_918["text"] = "senha"
        GLabel_918.place(x=100,y=170,width=70,height=25)

    def GButton_582_command(self):
        print("command")


    def GButton_579_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
