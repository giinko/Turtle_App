from tkinter import *
from turtle import RawPen
import turtle as t
from PIL import Image, ImageTk

class Application:

    def __init__(self):
        self.root = Tk()
        self.body()
        self.canvas()
        self.root.mainloop()

    # defnir la fenetre
    def body(self):
        self.root.title("Turtle prject")
        self.root.minsize(760, 550)
        self.root.maxsize(760, 550)
        self.root.config(bg="#bfbfbf")

        self.Title = Label(self.root, text="Quels figure voulez-vous dessinez ?",
                           font=("Arial Black", 15), bg="#bfbfbf", fg="black")
        self.Title.place(relx=0.5, rely=0.065, anchor=CENTER)

        self.fram_glob = Frame(self.root, bg="#bfbfbf")
        self.fram_glob.place(relx=0.5, rely=0.56, anchor=CENTER)

    # afficher le body de la page principal
    def canvas(self):
        canvas1 = Canvas(self.fram_glob, height=190, width=210, bg="#bfbfbf")
        img1 = Image.open("triangle.png")
        canvas1.image = ImageTk.PhotoImage(img1)
        canvas1.create_image(108, 99, image=canvas1.image)
        canvas1.grid(row=1, column=0, padx=20)

        self.button1 = Button(self.fram_glob, text="triangle", command=self.getbutton1)

        self.button1.grid(row=2, column=0, pady=7)

        canvas2 = Canvas(self.fram_glob, height=190, width=210, bg="#bfbfbf")
        img2 = Image.open("cercle.png")
        canvas2.image = ImageTk.PhotoImage(img2)
        canvas2.create_image(108, 99, image=canvas2.image)
        canvas2.grid(row=1, column=1, padx=20)

        self.button2 = Button(self.fram_glob, text="cercle", command=self.getbutton2)

        self.button2.grid(row=2, column=1, pady=7)

        canvas3 = Canvas(self.fram_glob, height=190, width=210, bg="#bfbfbf")
        img3 = Image.open("carre.png")
        canvas3.image = ImageTk.PhotoImage(img3)
        canvas3.create_image(108, 99, image=canvas3.image)
        canvas3.grid(row=1, column=2, padx=20)

        self.button3 = Button(self.fram_glob, text="carre", command=self.getbutton3)
        self.button3.grid(row=2, column=2, pady=7)

        canvas4 = Canvas(self.fram_glob, height=190, width=210, bg="#bfbfbf")
        img4 = Image.open("penta.png")
        canvas4.image = ImageTk.PhotoImage(img4)
        canvas4.create_image(108, 99, image=canvas4.image)
        canvas4.grid(row=3, column=0, padx=20)

        self.button4 = Button(self.fram_glob, text="penta", command=self.getbutton4)
        self.button4.grid(row=4, column=0, pady=7)

        canvas5 = Canvas(self.fram_glob, height=190, width=210, bg="#bfbfbf")
        img5 = Image.open("etoile.png")
        canvas5.image = ImageTk.PhotoImage(img5)
        canvas5.create_image(108, 99, image=canvas5.image)
        canvas5.grid(row=3, column=1, padx=20)

        self.button5 = Button(self.fram_glob, text="étoile", command=self.getbutton5)
        self.button5.grid(row=4, column=1, pady=7)

        canvas6 = Canvas(self.fram_glob, height=190, width=210, bg="#bfbfbf")
        img6 = Image.open("car.png")
        canvas6.image = ImageTk.PhotoImage(img6)
        canvas6.create_image(108, 99, image=canvas6.image)
        canvas6.grid(row=3, column=2, padx=20)

        self.button6 = Button(self.fram_glob, text="primo", command=self.getbutton6)
        self.button6.grid(row=4, column=2, pady=7)

    def back(self):
        self.new_frame.place_forget()
        self.new_label.place_forget()
        self.return_button.place_forget()
        self.valid_button.place_forget()

        self.Title.place(relx=0.5, rely=0.065, anchor=CENTER)
        self.fram_glob.place(relx=0.5, rely=0.56, anchor=CENTER)
        self.new_label.grid_remove()

    # variable pour get le nom de chaque figure
    def getbutton1(self):
        self.figur = self.button1.cget("text")
        self.variable()

    def getbutton2(self):
        self.figur = self.button2.cget("text")
        self.variable()

    def getbutton3(self):
        self.figur = self.button3.cget("text")
        self.variable()

    def getbutton4(self):
        self.figur = self.button4.cget("text")
        self.variable()

    def getbutton5(self):
        self.figur = self.button5.cget("text")
        self.variable()

    def getbutton6(self):
        self.figur = self.button6.cget("text")
        self.variable()

    def variable(self):
        self.Title.place_forget()
        self.fram_glob.place_forget()

        self.new_label = Label(self.root, text="Merci de choisir les parametres pour votre figure :",
                               font=("Arial Black", 19), bg="#bfbfbf", fg="black")
        self.new_label.place(relx=0.5, rely=0.07, anchor=CENTER)

        self.new_frame = Frame(self.root, bg="#bfbfbf")

        self.bg_color = Label(self.new_frame, text="background color :",
                              font=("Arial Black", 12), bg="#bfbfbf", fg="black")
        self.bg_color.grid(row=0, column=0, pady=5)

        self.backgrounf_color1 = Entry(self.new_frame)
        self.backgrounf_color1.grid(row=0, column=1)

        self.color = Label(self.new_frame, text="pen color :",
                           font=("Arial Black", 12), bg="#bfbfbf", fg="black")
        self.color.grid(row=1, column=0, pady=5)

        self.color_crayon = Entry(self.new_frame)
        self.color_crayon.grid(row=1, column=1)

        if self.figur == "triangle":
            self.cote_tri1 = Label(self.new_frame, text="taille du triangle :",
                                  font=("Arial Black", 12), bg="#bfbfbf", fg="black")
            self.cote_tri1.grid(row=2, column=0, pady=5)

            self.cote_tri = Entry(self.new_frame)
            self.cote_tri.grid(row=2, column=1)

        if self.figur == "cercle":
            self.rayon1 = Label(self.new_frame, text="taille du rayon :",
                                  font=("Arial Black", 12), bg="#bfbfbf", fg="black")
            self.rayon1.grid(row=2, column=0, pady=5)

            self.rayon = Entry(self.new_frame)
            self.rayon.grid(row=2, column=1)

        if self.figur == "carre" :
            self.longeur1 = Label(self.new_frame, text="quel longeur :",
                                font=("Arial Black", 12), bg="#bfbfbf", fg="black")
            self.longeur1.grid(row=2, column=0, pady=5)

            self.longeur = Entry(self.new_frame)
            self.longeur.grid(row=2, column=1)

            self.largeur1 = Label(self.new_frame, text="quel largeur :",
                                  font=("Arial Black", 12), bg="#bfbfbf", fg="black")
            self.largeur1.grid(row=3, column=0, pady=5)

            self.largeur = Entry(self.new_frame)
            self.largeur.grid(row=3, column=1)

        if self.figur == "penta" :
            self.penta1 = Label(self.new_frame, text="taille du penta :",
                                  font=("Arial Black", 12), bg="#bfbfbf", fg="black")
            self.penta1.grid(row=2, column=0, pady=5)

            self.penta = Entry(self.new_frame)
            self.penta.grid(row=2, column=1)

        if self.figur == "étoile":
            self.etoile1 = Label(self.new_frame, text="taille de l'étoile :",
                                font=("Arial Black", 12), bg="#bfbfbf", fg="black")
            self.etoile1.grid(row=2, column=0, pady=5)
            self.etoile = Entry(self.new_frame)
            self.etoile.grid(row=2, column=1)


        self.new_frame.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.valid_button = Button(self.root, text="construire la figure :", command=self.construction)
        self.valid_button.place(relx=0.5, rely=0.95, anchor=CENTER)

        self.return_button = Button(self.root, text="BACK", fg="red", command=self.back)
        self.return_button.place(relx=0.9, rely=0.95, anchor=CENTER)

    # construire la figure demander
    def construction(self):
        self.return_button.place_forget()
        self.valid_button.place_forget()
        self.return_button1 = Button(self.root, text="BACK", fg="red", command=self.back1)
        self.return_button1.place(relx=0.9, rely=0.95, anchor=CENTER)

        color_bg = str(self.backgrounf_color1.get())
        color = str(self.color_crayon.get())
        print(color_bg)

        if color == "":
            color = "black"

        try :
            self.can = Canvas(self.root, height=400, width=500)
            self.can.place(relx=0.5, rely=0.5, anchor=CENTER)

        except:
            self.can = Canvas(self.root, height=400, width=500)
            self.can.place(relx=0.5, rely=0.5, anchor=CENTER)

        if self.figur == "triangle":
            try:
                cotetri = int(self.cote_tri.get())
            except:
                cotetri = 100

            if cotetri > 360 :
                cotetri = 100
                self.too_big = Label(self.root, text="la taille est trop grande, une valeur par default a été mise",
                                  font=("Arial Black", 8), bg="#bfbfbf", fg="red")
                self.too_big.place(relx=0.5, rely=0.8, anchor=CENTER)

            draw = RawPen(self.can)
            draw.color(color)

            draw.up()
            draw.left(180)
            draw.forward(cotetri/2)
            draw.left(90)
            draw.forward(cotetri/2)
            draw.left(90)
            draw.down()
            draw.forward(cotetri)
            draw.left(120)
            draw.forward(cotetri)
            draw.left(120)
            draw.forward(cotetri)

        if self.figur == "cercle":
            try:
                rayon = int(self.rayon.get())
            except:
                rayon = 100

            if rayon > 190 :
                rayon = 75
                self.too_big = Label(self.root, text="la taille est trop grande, une valeur par default a été mise",
                                     font=("Arial Black", 8), bg="#bfbfbf", fg="red")
                self.too_big.place(relx=0.5, rely=0.8, anchor=CENTER)

            draw = RawPen(self.can)
            draw.color(color)

            draw.up()
            draw.right(90)
            draw.forward(rayon)
            draw.left(90)
            draw.down()

            draw.circle(rayon)

        if self.figur == "carre":
            try:
                longeur = int(self.longeur.get())
            except:
                longeur = 100

            try:
                largeur = int(self.largeur.get())
            except:
                largeur = 100


            if longeur > 380:
                longeur = 150
                largeur = 150
                self.too_big = Label(self.root, text="la taille est trop grande, une valeur par default a été mise",
                                     font=("Arial Black", 8), bg="#bfbfbf", fg="red")
                self.too_big.place(relx=0.5, rely=0.8, anchor=CENTER)

            if largeur > 380:
                longeur = 150
                largeur = 150
                self.too_big = Label(self.root, text="la taille est trop grande, une valeur par default a été mise",
                                     font=("Arial Black", 8), bg="#bfbfbf", fg="red")
                self.too_big.place(relx=0.5, rely=0.8, anchor=CENTER)

            draw = RawPen(self.can)
            draw.color(color)

            draw.up()
            draw.left(180)
            draw.forward(longeur / 2)
            draw.left(90)
            draw.forward(largeur / 2)
            draw.left(90)
            draw.down()

            draw.forward(longeur)
            draw.left(90)
            draw.forward(largeur)
            draw.left(90)
            draw.forward(longeur)
            draw.left(90)
            draw.forward(largeur)
            draw.left(90)

        if self.figur == "penta":
            try:
                taille_penta = int(self.penta.get())
            except:
                taille_penta = 150

            if taille_penta > 225:
                taille_penta = 150
                self.too_big = Label(self.root, text="la taille est trop grande, une valeur par default a été mise",
                                     font=("Arial Black", 8), bg="#bfbfbf", fg="red")
                self.too_big.place(relx=0.5, rely=0.8, anchor=CENTER)

            draw = RawPen(self.can)
            draw.color(color)

            draw.up()
            draw.right(90)
            draw.forward(taille_penta - 50)
            draw.right(90)
            draw.forward(taille_penta / 2)
            draw.right(180)
            draw.down()

            draw.forward(taille_penta)
            draw.left(72)
            draw.forward(taille_penta)
            draw.left(72)
            draw.forward(taille_penta)
            draw.left(72)
            draw.forward(taille_penta)
            draw.left(72)
            draw.forward(taille_penta)

        if self.figur == "étoile":
            try:
                etoile = int(self.etoile.get())
            except:
                etoile = 75

            if etoile > 150:
                etoile = 75
                self.too_big = Label(self.root, text="la taille est trop grande, une valeur par default a été mise",
                                     font=("Arial Black", 8), bg="#bfbfbf", fg="red")
                self.too_big.place(relx=0.5, rely=0.8, anchor=CENTER)

            draw = RawPen(self.can)
            draw.color(color)

            draw.up()
            draw.left(90)
            draw.forward(etoile / 4)
            draw.left(90)
            draw.forward(etoile + etoile/5)
            draw.left(180)
            draw.down()


            draw.forward(etoile)
            draw.left(180-108)
            draw.forward(etoile)
            draw.right(180-36)
            draw.forward(etoile)

            draw.left(180-108)
            draw.forward(etoile)
            draw.right(180-36)
            draw.forward(etoile)

            draw.left(180 - 108)
            draw.forward(etoile)
            draw.right(180 - 36)
            draw.forward(etoile)

            draw.left(180 - 108)
            draw.forward(etoile)
            draw.right(180 - 36)
            draw.forward(etoile)

            draw.left(180 - 108)
            draw.forward(etoile)




    #definir la focntion qui retir la canvas
    def back1(self):
        try :
            self.can.place_forget()
            self.return_button1.place_forget()
            self.too_big.place_forget()
            self.return_button = Button(self.root, text="BACK", fg="red", command=self.back)
            self.return_button.place(relx=0.9, rely=0.95, anchor=CENTER)
            self.valid_button = Button(self.root, text="construire la figure :", command=self.construction)
            self.valid_button.place(relx=0.5, rely=0.95, anchor=CENTER)
        except :
            self.can.place_forget()
            self.return_button1.place_forget()
            self.return_button = Button(self.root, text="BACK", fg="red", command=self.back)
            self.return_button.place(relx=0.9, rely=0.95, anchor=CENTER)
            self.valid_button = Button(self.root, text="construire la figure :", command=self.construction)
            self.valid_button.place(relx=0.5, rely=0.95, anchor=CENTER)


app = Application()
