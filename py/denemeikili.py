import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

pencere = tk.Tk()
pencere.title("Ikili Pencere")
pencere.config(background="#FFFFFF")

pencereCercevesi = tk.Frame(pencere, width=600, height=500)
pencereCercevesi.grid(row=0, column=0, pady=2, padx=10)

kamera = cv2.VideoCapture(0)

def goruntu_oynat():
    _, goruntu = kamera.read()
    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
    #goruntu = cv2.flip(goruntu, 1)
    image = cv2.cvtColor(goruntu, cv2.COLOR_BGR2RGBA)
    lower = np.array([0, 60, 146])
    upper = np.array([135, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    sonuc = cv2.bitwise_and(goruntu, goruntu, mask=mask)
    img = Image.fromarray(sonuc)
    imgtk = ImageTk.PhotoImage(image=img)
    img2 = Image.fromarray(image)
    imgtk2 = ImageTk.PhotoImage(image=img2)
    display1.imgtk = imgtk2 #Shows frame for display 1
    display1.configure(image=imgtk2)
    display2.imgtk = imgtk #Shows frame for display 2
    display2.configure(image=imgtk)
    pencere.after(10, goruntu_oynat)

display1 = tk.Label(pencereCercevesi)
display1.grid(row=0, column=1, padx=10, pady=2)  #Display 1
display2 = tk.Label(pencereCercevesi)
display2.grid(row=0, column=0) #Display 2

etiket1=tk.Label(pencereCercevesi,text="Düz")
etiket1.grid(row=1, column=1)

etiket2=tk.Label(pencereCercevesi,text="Maskeli")
etiket2.grid(row=1, column=0)


goruntu_oynat() #Display
pencere.mainloop()  #Starts GUI