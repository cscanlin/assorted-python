
import Tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("progress bar")
        self.bar1 = "   "
        self.bar2 = "   "
        self.bar3 = "   "
        self.bar4 = "   "
        self.bar5 = "   "
        self.bar6 = "   "
        self.bar7 = "   "
        self.bar8 = "   "
        self.bar9 = "   "
        self.bar10 = "   "
        self.percent = 0
        self.progressbar = tk.Label(text="[{}{}{}{}{}{}{}{}{}{}] %{}".format(self.bar1,self.bar2,self.bar3,self.bar4,self.bar5,self.bar6,self.bar7,self.bar8,self.bar9,self.bar10,self.percent))

        self.start = tk.Button(text="Start Progress Bar",command = self.start_bar())
        self.pause = tk.Button(text="Pause Progress Bar",command = self.pause_bar())
        self.reset = tk.Button(text="Reset Progress Bar", command = self.reset_bar())

        self.quitgame = tk.Button(text="Quit",fg="red",command=self.destroywindow)

        self.progressbar.pack()
        self.start.pack()
        self.pause.pack()
        self.reset.pack()
        self.quitgame.pack()

    def destroywindow(self):
        self.root.destroy()

    def start_bar(self):
        self.barstarted = True
        self.update()

    def pause_bar(self):
        self.barstarted = False

    def reset_bar(self):
        self.barstarted = False
        self.bar1 = "   "
        self.bar2 = "   "
        self.bar3 = "   "
        self.bar4 = "   "
        self.bar5 = "   "
        self.bar6 = "   "
        self.bar7 = "   "
        self.bar8 = "   "
        self.bar9 = "   "
        self.bar10 = "   "
        self.progressbar.configure(text="[{}{}{}{}{}{}{}{}{}{}] %{}".format(self.bar1,self.bar2,self.bar3,self.bar4,self.bar5,self.bar6,self.bar7,self.bar8,self.bar9,self.bar10,self.percent))
    def addone(self):
        self.percent += 1
    def update(self):
        while self.barstarted:
            if self.percent == 10:
                self.bar1 = "="
                self.percent += 10
            elif self.percent == 20:
                self.bar2 = "="
                self.percent += 10
            elif self.percent == 30:
                self.bar3 = "="
                self.percent += 10
            elif self.percent == 40:
                self.bar4 = "="
                self.percent += 10
            elif self.percent == 50:
                self.bar5 = "="
                self.percent += 10
            elif self.percent == 60:
                self.bar6 = "="
                self.percent += 10
            elif self.percent == 70:
                self.bar7 = "="
                self.percent += 10
            elif self.percent == 80:
                self.bar8 = "="
                self.percent += 10
            elif self.percent == 90:
                self.bar9 = "="
                self.percent += 10
            elif self.percent == 100:
                self.bar10 = "="
                self.percent += 10
                self.reset_bar()
            self.progressbar.configure(text="[{}{}{}{}{}{}{}{}{}{}] %{}".format(self.bar1,self.bar2,self.bar3,self.bar4,self.bar5,self.bar6,self.bar7,self.bar8,self.bar9,self.bar10,self.percent))
            self.root.after(1, self.addone())

app = App()
while True:
    app.root.mainloop()
