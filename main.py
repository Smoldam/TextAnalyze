"""
main.py: první projekt do Engeto Online Python Akademie

author: Martin Smola
email: smoldaboss@seznam.cz
"""


# Text to be analyzed (can be changed)
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''',
    '''Ten ta to i u nás.''',
    '''a bc cde''',
    '''a bc ef cde 123 ghi nmh''',
]

# Users database
USERS_BASE = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

LINE_SEP = "\x1b[31m-" * 43 + "\x1b[0m"
COL_SEP = "\x1b[31m|\x1b[0m"
STAR_CHAR = "\x1b[92m*\x1b[0m"
TEXTS_SUM = len(TEXTS)


# results variables
w_count = 0
w_upper = 0
w_lower = 0
w_title = 0
w_numeric = 0
w_num_sum = 0
w_graph = dict()

# login process
print("\033c", LINE_SEP, sep = "")
input_name = input(" Input username: ")
input_pass = input(" Input password: ")
if input_name.lower() in USERS_BASE and input_pass == USERS_BASE[input_name.lower()]:

    # wellcome message
    print(LINE_SEP,
        f"\n Welcome to the app, {input_name.title()}.",
        f"\n We have {TEXTS_SUM} texts to be analyzed.\n",
        LINE_SEP,
        sep= "")

    # text selection
    for _ in range(1000):
        user_choice = input(f" Enter a number btw. 1 and {TEXTS_SUM} to select: ")
        if not user_choice.isnumeric():
            print(" Input is not a number, please try again.")
        else:
            if 1 <= int(user_choice) <= TEXTS_SUM:
                break
            else:
                print(" Input is not in range, please try again.")
        print(LINE_SEP)
    text = TEXTS[int(user_choice) - 1]

    # text analysis
    for word in text.split():
        word = word.strip(",.:;!?()[]{}\"'<>#")
        if word.isalpha():
            w_count += 1
            if word.isupper():
                w_upper += 1
            elif word.islower():
                w_lower += 1
            elif word.istitle():
                w_title += 1
        elif word.isnumeric():
            w_numeric += 1
            w_num_sum += int(word)
        word_len = len(word)
        if word_len not in w_graph.keys():
            w_graph[word_len] = 1
        else:
            w_graph[word_len] += 1


    # print results - text
    word_maxval = sorted(w_graph.values(), reverse=True)[0]
    
    print(LINE_SEP,
        f"\n There are {w_count + w_numeric} strings in the selected text.",
        f"\n There are {w_title} titlecase words.",
        f"\n There are {w_upper} uppercase words.",
        f"\n There are {w_lower} lowercase words.",
        f"\n There are {w_numeric} numeric strings.",
        f"\n The sum of all the numbers is {w_num_sum}.\n",
        LINE_SEP, 
        sep = "")
    
    # print results - graph
    print(f" LEN {COL_SEP} OCCURENCES ",
        f" " * (word_maxval - 6),
        f"{COL_SEP} NR.\n",
        LINE_SEP,
        sep = "")
    for key in sorted(w_graph.keys()):
        space_sep_star = (word_maxval - w_graph[key]) + 5
        if word_maxval < 7:
            space_sep_star = 18 - (7 + w_graph[key])
        #space_sep_title = 4 - len(str(key)) + str(key)
        print(f" " * (4 - len(str(key))) + str(key) + f" {COL_SEP} ",
              f"{STAR_CHAR}" * w_graph[key],
              f" " * space_sep_star,
              f"{COL_SEP} {w_graph[key]}",
              sep = "")
    print(LINE_SEP)

# unsuccessful login
elif input_name not in USERS_BASE:
    print(" Not registered user, terminating the program.")
else:
    print(" Wrong password, terminating the program.")
    
