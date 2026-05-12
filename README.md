# helloworld
my first project on github
# 🚢 Hello World Terminal Art

A simple Python terminal art project featuring colorful ANSI output and ASCII ship art.

---

## ✨ Preview

```text
============================================================
               🚢 HELLO WORLD TERMINAL ART 🚢
============================================================

                           |    |    |
                          \|/  \|/  \|/
                         )_)  )_)  )_)
                        )___))___))___)\
                       )____)____)_____)\\
                     _____|____|____|____\\\__
------------\_______________________________/---------
     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
```

---

## 📦 Requirements

- Python 3.x

---

## ▶️ Run

```bash
python main.py
```

---

## 🧠 Source Code

```python
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(CYAN + "=" * 60)
print(YELLOW + "        🚢 HELLO WORLD TERMINAL ART 🚢")
print(CYAN + "=" * 60 + RESET)

ship = rf"""{BLUE}

                           |    |    |
                          \|/  \|/  \|/
                         )_)  )_)  )_)
                        )___))___))___)\
                       )____)____)_____)\\
                     _____|____|____|____\\\__
------------\_______________________________/---------
     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

{RESET}
"""

print(ship)
```

---

## 🎨 Features

- ANSI terminal colors
- ASCII art ship
- Styled terminal output
- Beginner-friendly Python project

---

## 📄 License

Free to use and modify.