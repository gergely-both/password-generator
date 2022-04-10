import random
import string

CHARS = string.ascii_letters + string.digits
SYMBOLS = """!"#$%&'()*+,-./:;<=>?@[\]^_{}~"""
MIN_CHARS = 5
MAX_CHARS = 128


def generate_password():
    password_chars = random.choices(CHARS, k=total_count-sym_count)
    password_syms = random.choices(SYMBOLS, k=sym_count)
    password_elements = password_chars + password_syms
    random.shuffle(password_elements)
    password = "".join(password_elements)
    print(f"\n\n\tYour generated password is: {password}")


print("""
.-. .-')    ('-.          .-')     ('-.                  ('-.  ,---. 
\  ( OO ) _(  OO)        ( OO ).  ( OO ).-.            _(  OO) |   | 
 ;-----.\(,------.      (_)---\_) / . --. /   ,------.(,------.|   | 
 | .-.  | |  .---'      /    _ |  | \-.  \ ('-| _.---' |  .---'|   | 
 | '-' /_)|  |          \  :` `..-'-'  |  |(OO|(_\     |  |    |   | 
 | .-. `.(|  '--.        '..`''.)\| |_.'  |/  |  '--. (|  '--. |  .' 
 | |  \  ||  .--'       .-._)   \ |  .-.  |\_)|  .--'  |  .--' `--'  
 | '--'  /|  `---.      \       / |  | |  |  \|  |_)   |  `---..--.  
 `------' `------'       `-----'  `--' `--'   `--'     `------''--'  

Welcome to the password generator!
""")

total_count = None
sym_count = None
while not isinstance(total_count, int) or not isinstance(sym_count, int):
    try:
        if not isinstance(total_count, int):
            answer_total = int(input("\nEnter character count of password: "))
            total_count = answer_total if MIN_CHARS <= answer_total <= MAX_CHARS else None
            if 0 < answer_total < MIN_CHARS:
                print("\tThat value is too low.")
            elif answer_total > MAX_CHARS:
                print("\tThat value is too high.")
            elif answer_total <= 0:
                raise ValueError()
        elif not isinstance(sym_count, int):
            answer_sym = int(input("\nHow many special characters should be present? "))
            sym_count = answer_sym if 0 <= answer_sym <= total_count else None
            if answer_sym > total_count:
                print("\tThat value is too high.")
            elif answer_sym < 0:
                raise ValueError()
    except ValueError:
        print("\tThat is an invalid value.")

generate_password()

while True:
    repeat = input("\n\t\tTry again? ([Y]/n): ").lower()
    if repeat == "n":
        print("\n\nHave a great day! 😊\n\n")
        break
    elif repeat.strip() in {"", "y"}:
        generate_password()
