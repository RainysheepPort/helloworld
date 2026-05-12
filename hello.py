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