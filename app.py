import secrets
import string
import tkinter as tk
from tkinter import messagebox, filedialog
import os
from datetime import datetime

# ----------------------------
# CONFIG
# ----------------------------
HISTORY_FILE = os.path.join(os.path.expanduser("~"), "password_history.txt")

# ----------------------------
# PASSWORD LOGIC
# ----------------------------

def genera_password(lunghezza=16, maiuscole=True, minuscole=True, numeri=True, simboli=True):
    charset = ""

    if maiuscole:
        charset += string.ascii_uppercase
    if minuscole:
        charset += string.ascii_lowercase
    if numeri:
        charset += string.digits
    if simboli:
        charset += "!@#$%^&*()-_=+[]{};:,.?/<>"

    if not charset:
        return ""

    return ''.join(secrets.choice(charset) for _ in range(lunghezza))


def valuta_forza(pw):
    score = 0

    if len(pw) >= 12:
        score += 1
    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in string.punctuation for c in pw):
        score += 1

    return ["Debole", "Media", "Forte", "Molto forte", "Eccellente"][max(0, min(score-1, 4))]

# ----------------------------
# HISTORY
# ----------------------------

def salva_storico(password):
    try:
        with open(HISTORY_FILE, "a") as f:
            f.write(f"{datetime.now()} - {password}\n")
    except Exception:
        pass


def carica_storico():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return f.readlines()[-20:]
    return []

# ----------------------------
# ACTIONS
# ----------------------------

def genera():
    try:
        lunghezza = int(slider.get())
    except ValueError:
        messagebox.showerror("Errore", "Lunghezza non valida")
        return

    pw = genera_password(
        lunghezza,
        var_upper.get(),
        var_lower.get(),
        var_digits.get(),
        var_symbols.get()
    )

    if not pw:
        messagebox.showerror("Errore", "Seleziona almeno un tipo di carattere")
        return

    output_var.set(pw)
    strength_var.set(f"Sicurezza: {valuta_forza(pw)}")

    salva_storico(pw)
    aggiorna_storico()

    root.clipboard_clear()
    root.clipboard_append(pw)
    root.update()
    status_var.set("Password generata e copiata")


def aggiorna_storico():
    listbox.delete(0, tk.END)
    for line in carica_storico():
        listbox.insert(tk.END, line.strip())


def copia():
    pw = output_var.get()
    if not pw:
        return
    root.clipboard_clear()
    root.clipboard_append(pw)
    root.update()
    status_var.set("Copiata negli appunti")


def pulisci_storico():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    aggiorna_storico()
    status_var.set("Storico cancellato")


def esporta_storico():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.writelines(carica_storico())
        status_var.set("Storico esportato")

# ----------------------------
# UI
# ----------------------------

root = tk.Tk()
root.title("Password Generator ULTRA")
root.geometry("520x520")
root.resizable(False, False)

# MENU
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Esporta storico", command=esporta_storico)
file_menu.add_command(label="Cancella storico", command=pulisci_storico)
file_menu.add_separator()
file_menu.add_command(label="Esci", command=root.quit)

# TITLE
label = tk.Label(root, text="PASSWORD GENERATOR ULTRA", font=("Helvetica", 16, "bold"))
label.pack(pady=10)

# SLIDER
slider = tk.Scale(root, from_=4, to=64, orient="horizontal")
slider.set(16)
slider.pack()

# OPTIONS
frame = tk.Frame(root)
frame.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Maiuscole", variable=var_upper).grid(row=0, column=0)
tk.Checkbutton(frame, text="Minuscole", variable=var_lower).grid(row=0, column=1)
tk.Checkbutton(frame, text="Numeri", variable=var_digits).grid(row=1, column=0)
tk.Checkbutton(frame, text="Simboli", variable=var_symbols).grid(row=1, column=1)

# BUTTON
btn = tk.Button(root, text="Genera", command=genera)
btn.pack(pady=10)

# OUTPUT
output_var = tk.StringVar()
tk.Label(root, textvariable=output_var, font=("Helvetica", 12, "bold")).pack()

strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var).pack()

# COPY
btn_copy = tk.Button(root, text="Copia", command=copia)
btn_copy.pack(pady=5)

# HISTORY
tk.Label(root, text="Storico").pack(pady=5)

listbox = tk.Listbox(root, height=8, width=60)
listbox.pack()

btn_refresh = tk.Button(root, text="Aggiorna storico", command=aggiorna_storico)
btn_refresh.pack(pady=5)

# STATUS
status_var = tk.StringVar()
tk.Label(root, textvariable=status_var, fg="green").pack(pady=5)

# SHORTCUT
root.bind("<Command-g>", lambda e: genera())
root.bind("<Control-g>", lambda e: genera())

# INIT
aggiorna_storico()

root.mainloop()

# NOTE:
# Per icona Mac (.icns) usare PyInstaller:
# pyinstaller --onefile --windowed --icon=icon.icns app.py
