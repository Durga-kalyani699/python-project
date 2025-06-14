
from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=491236870f82e91a0c8a72d52df1faed").json()
    w_Label1.config(text=data["weather"][0]["main"])
    wb_Label1.config(text=data["weather"][0]["description"])
    temp_Label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_Label1.config(text=data["main"]["pressure"])



win = Tk()
win.title("Weather App")
win.config(bg="black")
win.geometry("500x600")

name_Label = Label(win,text="weather app",
                   font=("Time New Roman",40,"bold"))
name_Label.place(x=25,y=50,height=50,width=450)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="weather app",values=list_name,
                   font=("Time New Roman",30,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_Label = Label(win,text="weather climate",
                   font=("Time New Roman",20))
w_Label.place(x=25,y=260,height=50,width=210)

w_Label1 = Label(win,text="",
                   font=("Time New Roman",20))
w_Label1.place(x=250,y=260,height=50,width=210)

wb_Label = Label(win,text="weather description",
                   font=("Time New Roman",18))
wb_Label.place(x=25,y=330,height=50,width=210)

wb_Label1 = Label(win,text="",
                   font=("Time New Roman",18))
wb_Label1.place(x=250,y=330,height=50,width=210)

temp_Label = Label(win,text="temperature",
                   font=("Time New Roman",20))
temp_Label.place(x=25,y=400,height=50,width=210)

temp_Label1 = Label(win,text="",
                   font=("Time New Roman",20))
temp_Label1.place(x=250,y=400,height=50,width=210)
per_Label = Label(win,text="pressure",
                   font=("Time New Roman",20))
per_Label.place(x=25,y=470,height=50,width=210)

per_Label1 = Label(win,text="",
                  font=("Time New Roman",20))
per_Label1.place(x=250,y=470,height=50,width=210)
done_button = Button(win,text="Done",
                   font=("Time New Roman",30,"bold"),command=data_get)

done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()
