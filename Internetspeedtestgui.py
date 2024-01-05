from tkinter import *
import speedtest

def speedcheck():
    sp= speedtest.Speedtest()
    sp.get_servers()
    down = str( round(sp.download()/(10**6),3))+ "Mbps"
    up = str( round(sp.upload()/(10**6),3))+ "Mbps"
    lap_down.config(text=down)
    lap_up.config(text=up)



sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("500x650")
sp.config(bg="Black")

lap = Label(sp,text="Internet Speed Test", font=("Times New Roman",30,"bold"),bg="Black",fg="Red")
lap.place(x=60,y=40,height=50,width=380)

lap = Label(sp,text="Download Speed", font=("Times New Roman",30,"bold"),bg="white",fg="Red")
lap.place(x=60,y=130,height=50,width=380)

lap_down = Label(sp,text="00", font=("Times New Roman",30,"bold"),bg="white",fg="Red")
lap_down.place(x=60,y=200,height=50,width=380)

lap = Label(sp,text="Upload Speed", font=("Times New Roman",30,"bold"),bg="white",fg="Red")
lap.place(x=60,y=290,height=50,width=380)

lap_up = Label(sp,text="00", font=("Times New Roman",30,"bold"),bg="white",fg="Red")
lap_up.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="CHECK SPEED", font=("Times New Roman",30,"bold"),bg="white",fg="Red",relief=RAISED,command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()

