import tkinter as tk
from PIL import ImageTk, Image
from textblob import TextBlob, Word

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("1000x626+160+50")

# Load background image
image = Image.open("bg2.png")
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define font styles
LARGE_FONT = ("Times new roman", 24)
MEDIUM_FONT = ("Times new roman", 16)

# Load list of words from text file
with open("words.csv", "r") as file:
    words = [line.strip() for line in file]
    
def check_spelling():
    word = enter_text.get()

    if word.lower() in words:
        spell.config(text="Correct spelling!")
    else:
        correction = TextBlob(word).correct()
        best_suggestion = correction.string
        suggestions = Word(word).spellcheck()
        related_words = ", ".join([suggestion[0] for suggestion in suggestions])
        spell.config(text=f"Did you mean '{best_suggestion}'? \n\n\n Related words: {related_words}")

def exit_app():
    root.destroy()

    
# Create heading label
heading = tk.Label(root, text="Spelling Checker", font=LARGE_FONT, bg="white", fg="#364971")
heading.pack(pady=50)

# Create input field
enter_text = tk.Entry(root, justify="center", width=50, font=MEDIUM_FONT, bg="white", bd=2)
enter_text.pack(pady=30)
enter_text.focus()

# Create check button
button = tk.Button(root, text="Check", font=MEDIUM_FONT, fg="white", bg="#8f00ff", command=check_spelling)
button.pack(pady=30)

# Create label to display spelling status
spell = tk.Label(root, font=MEDIUM_FONT, bg="white", fg="#364971")
spell.pack(pady=30)

# Create exit button
exit_button = tk.Button(root, text="Exit", font=MEDIUM_FONT, fg="white", bg="#8f00ff", command=exit_app)
exit_button.pack(pady=30)

root.mainloop()
