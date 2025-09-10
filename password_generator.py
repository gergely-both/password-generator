import random
import string


INTRO_GRAPHICS = """
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
"""


print(INTRO_GRAPHICS)
app_running = True


ALNUMS = "".join(item_1 for item_1 in string.printable if item_1.isalnum())
SYMBOLS = "".join(
    item_2
    for item_2 in string.printable
    if (not item_2.isalnum() and not item_2 in string.whitespace)
)
MIN_CHARS, MAX_CHARS = 5, 128


def password_generate():
    password_alnums = random.choices(ALNUMS, k=total_count - symbols_count)
    password_symbols = random.choices(SYMBOLS, k=symbols_count)
    password_elements = password_alnums + password_symbols
    random.shuffle(password_elements)
    password = "".join(password_elements)
    print(f"\n\tYour generated password is:\n\t{password}")


total_count = None
symbols_count = None
while not (isinstance(total_count, int) and isinstance(symbols_count, int)):
    try:
        if not isinstance(total_count, int):
            totcount_reply = int(input("\nEnter length of password: "))
            total_count = (
                totcount_reply if MIN_CHARS <= totcount_reply <= MAX_CHARS else None
            )
            # user choice failure explanation for total_count
            if total_count is None:
                if 0 < totcount_reply < MIN_CHARS:
                    print("\tThat value is too low.")
                elif totcount_reply > MAX_CHARS:
                    print("\tThat value is too high.")
                elif totcount_reply <= 0:
                    raise ValueError()

        elif not isinstance(symbols_count, int):
            symcount_reply = int(
                input("\nHow many special characters should be present? ")
            )
            symbols_count = (
                symcount_reply if 0 <= symcount_reply <= total_count else None
            )
            # user choice failure explanation for symbols_count:
            if symbols_count is None:
                if symcount_reply < 0:
                    raise ValueError()
                elif symcount_reply > total_count:
                    print("\tThat value is too high.")
    except ValueError:
        print("\tThat is an invalid value.")


password_generate()


while app_running:
    repeat_reply = input("\nTry another? ([Y]/n): ").strip().lower()
    if repeat_reply in {"y", ""}:
        password_generate()
    elif repeat_reply == "n":
        print("\nHave a nice day! 😊\n")
        break
