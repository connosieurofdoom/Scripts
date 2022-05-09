from tkinter import * #required.
from tkinter import messagebox #for messagebox.

App = Tk() #required.
App.withdraw() #for hide window.

print("Message Box in Console")
messagebox.showinfo("Notification", "Hello World!") #msgbox

App.mainloop() #required.
