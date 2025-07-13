# Termux PHP Web Server Manager

A lightweight Python-based CLI tool to manage a local PHP server in Termux.  
It allows you to easily start the server, change configuration, and update the tool via Git.

---

## 📦 Features

- 🛰 Start a PHP development server using a custom directory
- ⚙️ Change server path and port via CLI
- 🔄 Auto-generate a default web directory with an `index.php` page if none is set
- ⬆️ Update the tool with `git pull origin main`
- 🧠 Simple config management using `config.ini`

---

## 🖥 Requirements

- Python 3.x
- PHP
- Termux (or any Linux-like environment)
- Git

---

## 🛠 Installation

```bash
git clone https://github.com/huntersourasis/Termux-Server-Setup.git
cd Termux-Server-Setup
python3 main.py
```

---

## 🚀 Usage

After running the script, you'll see a simple menu:

```
[1] Start Server
[2] Update Tool
[3] Change Server Path
[4] Change Server Port
[5] Exit
```

Select an option by typing the number and pressing Enter.

---

## ⚙ Configuration

The tool stores its configuration in `config.ini`.  
On first run, it sets default values like:

```ini
[server]
path = ~/termux-server/
port = 8000
```

You can change these values using options 3 and 4 in the menu.

---

## 🧪 Default Web Folder

If the configured server path doesn't exist, the tool will:
- Automatically create `~/termux-server/`
- Copy a default `index.php` from `./web/index.php`

Make sure you have a default file at `./web/index.php` in your repo.

---

## 🔄 Updating the Tool

The tool includes a self-updating option:

```
[2] Update Tool
```

This runs:

```bash
git pull origin main
```

to pull the latest changes from your GitHub repository.

---

## 📁 Project Structure

```
├── main.py
├── TurmuxWebServer.py
├── config.ini
├── web/
│   └── index.php
└── README.md
```

---

## 📌 License

MIT License

---

## ✨ Author

**Sourasis Maity**  
[GitHub Profile](https://github.com/huntersourasis)
