import subprocess
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



def autocorrector_page():
    subprocess.call(["python", "Spelling_Autocorrector.py"])

def translator_page():
    subprocess.call(["python", "Language_Translator.py"])

def dictionary_page():
    subprocess.call(["python", "Talking_Dictionary.py"])

def text_to_speech_page():
    subprocess.call(["python", "Text_To_Speech.py"])

def word_game_page():
    subprocess.call(["python", "index.py"])

class Language_Solutions:
    def __init__(self,root):
        
        image = Image.open('ls.png')
        photo = ImageTk.PhotoImage(image)
        self.root=root
        self.root.geometry("1190x680+80+10")
        self.root.title("Language Solutions")
        self.root.wm_iconphoto(True, photo)

        title_lb1=Label(text="LANGUAGE SOLUTIONS",font=("times new roman",30,"bold"),bg="snow",fg="blue")
        title_lb1.place(x=400,y=10)

        #Load background image
        image = Image.open("bg3.png")
        self.background_image = ImageTk.PhotoImage(image)
        background_label = Label(self.root, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_lb1=Label(text="LANGUAGE SOLUTIONS",font=("times new roman",30,"bold"),fg="blue")
        title_lb1.place(x=350,y=30)

        # Spelling autocorrect button
        img = Image.open(r"img.png")
        img = img.resize((250, 250), resample=Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        b1 = Button(image=self.photoimg, cursor="hand2", command=autocorrector_page)
        b1.place(x=10, y=10, width=250,height=250)

        b1_1 = Button(text="SPELLING CORRECTOR", cursor="hand2", font=("times new roman", 13, "bold"), bg="white", fg="brown", command=autocorrector_page)
        b1_1.place(x=10, y=260, width=250, height=40)

        # Language translator button
        img1 = Image.open(r"img1.png")
        img1 = img1.resize((250, 250), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b2 = Button(image=self.photoimg1, cursor="hand2", command=translator_page)
        b2.place(x=930, y=10, width=250, height=250)

        b2_1 = Button(text="LANGUAGE TRANSLATOR", cursor="hand2", font=("times new roman", 13, "bold"), bg="white", fg="brown", command=translator_page )
        b2_1.place(x=930, y=260, width=250, height=40)

        # Talking dictionary button
        img2 = Image.open(r"img2.png")
        img2 = img2.resize((250, 250), resample=Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b3 = Button(image=self.photoimg2, cursor="hand2", command=dictionary_page)
        b3.place(x=10, y=380, width=250, height=250)

        b3_1 = Button(text="TALKING DICTIONARY", cursor="hand2", font=("times new roman", 13, "bold"), bg="white", fg="brown", command=dictionary_page)
        b3_1.place(x=10, y=630, width=250, height=40)
        # Text to speech button
        img3 = Image.open(r"img3.png")
        img3 = img3.resize((250, 250), resample=Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b4 = Button(image=self.photoimg3, cursor="hand2", command=text_to_speech_page)
        b4.place(x=930, y=380, width=250, height=250)

        b4_1 = Button(text="TEXT TO SPEECH", cursor="hand2", font=("times new roman", 13, "bold"), bg="white", fg="brown", command=text_to_speech_page)
        b4_1.place(x=930, y=630, width=250, height=40)

        # Word game button
        img4 = Image.open(r"img4.png")
        img4 = img4.resize((250, 250), resample=Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b5 = Button(image=self.photoimg4, cursor="hand2", command=word_game_page)
        b5.place(x=475, y=250, width=250, height=250)

        b5_1 = Button(text="WORD GAME", cursor="hand2", font=("times new roman", 13, "bold"), bg="white", fg="brown", command=word_game_page)
        b5_1.place(x=475, y=500, width=250, height=40)

        
if __name__ == "__main__":
    root = Tk()
    obj = Language_Solutions(root)
    root.mainloop()
