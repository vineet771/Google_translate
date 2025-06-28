
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Convert language names to codes
lang_dict = {v.title(): k for k, v in LANGUAGES.items()}

def change(text="type", src="English", dest="Hindi"):
    src_code = lang_dict.get(src, "en")
    dest_code = lang_dict.get(dest, "hi")
    
    trans = Translator()
    result = trans.translate(text, src=src_code, dest=dest_code)
    return result.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_text.get(1.0, END).strip()

    try:
        translated_text = change(text=masg, src=s, dest=d)
        dest_text.delete(1.0, END)
        dest_text.insert(END, translated_text)
    except Exception as e:
        dest_text.delete(1.0, END)
        dest_text.insert(END, f"Error: {e}")

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='skyblue')

# Heading
lab_text = Label(root, text="Translator", font=("Times New Roman", 40, "bold"))
lab_text.place(x=100, y=40, height=50, width=300)

# Source Text Label
lab_text = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="black", bg="skyblue")
lab_text.place(x=100, y=100, height=30, width=300)

# Source Text Box
sor_text = Text(root, font=("Times New Roman", 20), wrap=WORD)
sor_text.place(x=10, y=140, height=150, width=480)

# Language Dropdowns
list_text = list(lang_dict.keys())

comb_sor = ttk.Combobox(root, value=list_text, state="readonly")
comb_sor.place(x=10, y=310, height=40, width=150)
comb_sor.set("English")

comb_dest = ttk.Combobox(root, value=list_text, state="readonly")
comb_dest.place(x=330, y=310, height=40, width=150)
comb_dest.set("Hindi")

# Translate Button
button_change = Button(root, text="Translate", relief=RAISED, command   =data)
button_change.place(x=170, y=310, height=40, width=150)

# Destination Label
lab_text = Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg="black", bg="skyblue")
lab_text.place(x=100, y=370, height=30, width=300)

# Destination Text Box
dest_text = Text(root, font=("Times New Roman", 20), wrap=WORD)
dest_text.place(x=10, y=410, height=150, width=480)

root.mainloop()
