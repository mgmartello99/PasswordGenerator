# 🔐 Password Generator

Un’app desktop per generare password sicure con GUI, storico e strumenti avanzati.

Supporta:
- 🪟 Windows
- 🍎 macOS
- 🐧 Linux

---

## 🚀 Funzionalità

- Generazione password sicura (crypto-grade con `secrets`)
- Controllo caratteri:
  - Maiuscole
  - Minuscole
  - Numeri
  - Simboli
- Lunghezza personalizzabile (4–64)
- Valutazione forza password
- Copia automatica negli appunti
- Storico delle password
- Esportazione storico
- Pulizia storico
- Shortcut da tastiera

---

## 🧰 Requisiti

- Python 3.9+
- pip

Librerie usate (già incluse in Python):
- `tkinter`
- `secrets`
- `string`
- `os`
- `datetime`

---

## ▶️ Avvio in modalità sviluppo

Clona il repository:

```bash
git clone https://github.com/tuo-username/password-generator-ultra.git
cd password-generator-ultra
```

Avvia l’app:

```bash
python app.py
```

oppure:

```bash
python3 app.py
```

---

## 📦 Creare un eseguibile (TUTTI i sistemi operativi)

### 🔧 Installa PyInstaller

```bash
pip install pyinstaller
```

---

# 🪟 Windows (EXE)

```bash
pyinstaller --onefile --windowed app.py
```

Output:
```
dist/app.exe
```

---

# 🍎 macOS (APP)

```bash
pyinstaller --onefile --windowed app.py
```

Output:
```
dist/app
```

Opzionale con icona:

```bash
pyinstaller --onefile --windowed --icon=icon.icns app.py
```

---

# 🐧 Linux (binario)

```bash
pyinstaller --onefile app.py
```

Output:
```
dist/app
```

Rendi eseguibile:

```bash
chmod +x dist/app
```

---

## ⚠️ Note importanti per PyInstaller

### ❌ Problemi comuni

Se PyInstaller non viene riconosciuto:

```bash
python -m PyInstaller app.py
```

---

### 🍎 macOS blocca l’app

```bash
xattr -cr dist/app
```

Oppure:
- Impostazioni → Privacy e sicurezza → “Apri comunque”

---

## 📁 Struttura progetto

```
password-generator-ultra/
│
├── app.py
├── README.md
├── icon.icns (opzionale macOS)
└── dist/ (generato)
```

---

## 🔐 Sicurezza

Le password sono generate con `secrets`, che è sicuro crittograficamente e migliore di `random`.

---

## 💡 Possibili upgrade

- Dark mode completa
- Auto-save cifrato (AES)
- QR code password
- Versione menu bar (macOS)
- Installer `.dmg` (macOS)
- Installer `.msi` (Windows)
- Flatpak / AppImage (Linux)
- Cloud sync storico

---

## 🧪 Build avanzata (opzionale)

### 🍎 macOS .app + firma

```bash
pyinstaller --onefile --windowed --icon=icon.icns app.py
```

---

## 📜 Licenza

MIT License
