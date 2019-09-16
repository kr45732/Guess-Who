from tkinter import Button, Label, Entry, Tk, Canvas, NW, StringVar
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import random as r

refresh_ref = []
img_ref_dict = {}
char_cords_dict = {
    "Jean-claude": [0, 0],
    "Pierre": [110, 0],
    "Jean": [225, 0],
    "Amelie": [350, 0],
    "Mirabelle": [460, 0],
    "Isabelle": [580, 0],
    "Antonin": [697, 0],
    "Bernard": [797, 0],
    "Owen": [0, 200],
    "Dylan": [120, 200],
    "Herbert": [240, 200],
    "Christine": [350, 200],
    "Luc": [455, 200],
    "Cecilian": [565, 200],
    "Lionel": [675, 200],
    "Benoit": [790, 200],
    "Robert": [-10, 380],
    "Charline": [105, 380],
    "Renaud": [215, 380],
    "Michel": [330, 380],
    "Pierre-louis": [440, 380],
    "Etienne": [562, 380],
    "Henri": [676, 380],
    "Damien": [793, 380],
}
characteristic = [
    [
        "Jean-claude",
        [
            "Male",
            "Glasses",
            "Brown eyes",
            "Bald",
            "White hair",
            "Small mouth",
            "Small nose",
        ],
    ],
    [
        "Pierre",
        ["Male", "Mustache", "Brown eyes", "Brown hair", "Big mouth", "Small nose"],
    ],
    ["Jean", ["Male", "White hair", "Big nose", "Big mouth", "Blue eyes"]],
    [
        "Amelie",
        [
            "Female",
            "Hat",
            "Brown hair",
            "Small mouth",
            "Long hair",
            "Ear rings",
            "Brown eyes",
            "Small nose",
        ],
    ],
    [
        "Mirabelle",
        ["Female", "Black hair", "Earrings", "Small mouth", "Brown eyes", "Big nose"],
    ],
    [
        "Isabelle",
        [
            "Female",
            "Blonde hair",
            "Glasses",
            "Hat",
            "Small mouth",
            "Small nose",
            "Brown eyes",
        ],
    ],
    ["Antonin", ["Male", "Brown eyes", "Black hair", "Small nose", "Big mouth"]],
    ["Bernard", ["Male", "Brown eyes", "Brown hair", "Small nose", "Hat"]],
    [
        "Owen",
        ["Male", "Mustache", "Blue eyes", "Blonde hair", "Small nose", "Small mouth"],
    ],
    [
        "Dylan",
        [
            "Male",
            "Brown eyes",
            "Blonde hair",
            "Small nose",
            "Small mouth",
            "Bald",
            "Beard",
        ],
    ],
    [
        "Herbert",
        ["Male", "Brown eyes", "Blonde hair", "Big nose", "Small mouth", "Bald"],
    ],
    [
        "Christine",
        [
            "Female",
            "Blue eyes",
            "Blonde hair",
            "Small nose",
            "Small mouth",
            "Long hair",
        ],
    ],
    [
        "Luc",
        ["Male", "Brown eyes", "White hair", "Small nose", "Small mouth", "Glasses"],
    ],
    ["Cecilian", ["Male", "Brown eyes", "Ginger hair", "Small nose", "Small mouth"]],
    [
        "Lionel",
        ["Male", "Brown eyes", "Brown hair", "Big nose", "Big mouth", "Mustache"],
    ],
    [
        "Benoit",
        [
            "Male",
            "Brown eyes",
            "Brown hair",
            "Small mouth",
            "Small nose",
            "Bald",
            "Mustache",
            "Beard",
        ],
    ],
    ["Robert", ["Male", "Blue eyes", "Brown hair", "Big nose", "Big mouth"]],
    ["Charline", ["Female", "White hair", "Small nose", "Big mouth"]],
    [
        "Renaud",
        ["Male", "Brown eyes", "Blonde hair", "Small nose", "Big mouth", "Mustache"],
    ],
    [
        "Michel",
        ["Male", "Brown eyes", "Blonde hair", "Small nose", "Big mouth", "Beard"],
    ],
    [
        "Pierre-louis",
        [
            "Male",
            "Blue eyes",
            "Brown hair",
            "Small nose",
            "Small mouth",
            "Bald",
            "Glasses",
        ],
    ],
    [
        "Etienne",
        ["Male", "Brown eyes", "Blonde hair", "Small nose", "Small mouth", "Glasses"],
    ],
    ["Henri", ["Male", "Brown eyes", "White hair", "Small nose", "Big mouth", "Hat"]],
    ["Damien", ["Male", "Brown eyes", "Blonde hair", "Small nose", "Big mouth", "Hat"]],
]
x_add_list = []
turn_number = 0
comp_char_list = [
        "Jean-claude",
        "Pierre",
        "Jean",
        "Amelie",
        "Mirabelle",
        "Isabelle",
        "Antonin",
        "Bernard",
        "Owen",
        "Dylan",
        "Herbert",
        "Christine",
        "Luc",
        "Cecilian",
        "Lionel",
        "Benoit",
        "Robert",
        "Charline",
        "Renaud",
        "Michel",
        "Pierre-louis",
        "Etienne",
        "Henri",
        "Damien",
    ]
player_person_choice = ""
def submit_player():
    global player_person_choice
    player_person_choice = str(input_box1.get()).strip().capitalize()
    if player_person_choice in char_list:
        messagebox.showinfo(
            "Game info", "You chose " + player_person_choice + "\nStarting Game!"
        )
        window.destroy()
    else:
        messagebox.showerror("Game info", "Invalid person")

def options_page():
    root2 = Tk()
    root2.title("All Possible Guesses")
    root2.geometry("550x200")
    root2.resizable(False, False)
    possible_guesses_list = "Male, Female, Glasses, Brown eyes,\nBald, White hair, Small mouth, Mustache,\nBrown hair, Big mouth, Small nose, Blue eyes,\nHat, Long hair, Black hair, Earrings, Blonde hair,\nGinger hair, Beard, Big nose"
    possible_guesses_text = Label(root2, text=possible_guesses_list, font=("arial", 25))
    possible_guesses_title = Label(
        root2, text="All Possible Guesses Are Listed Below", font=("arial", 25, "bold")
    )
    possible_guesses_text.place(x=0, y=50)
    possible_guesses_title.place(x=35, y=0)

    root2.mainloop()

def play_game():
    guess = str(player_guess.get()).strip().capitalize()
    if guess in player_choices:
        player_choices.remove(guess)
        for i in characteristic:
            if i[0] == computer_person_choice:
                for x in i[1]:
                    if x == guess:
                        if guess in ["Male", "Female"]:
                            messagebox.showinfo(
                                "Game info", "The person is a " + guess.lower() + "!"
                            )
                        elif guess == "Bald":
                            messagebox.showinfo(
                                "Game info", "The person is " + guess.lower() + "!"
                            )
                        elif guess in [
                            "Small mouth",
                            "Big mouth",
                            "Mustache",
                            "Hat",
                            "Beard",
                            "Small nose",
                            "Big nose",
                        ]:
                            messagebox.showinfo(
                                "Game info", "The person has a " + guess.lower() + "!"
                            )
                        else:
                            messagebox.showinfo(
                                "Game info", "The person has " + guess.lower() + "!"
                            )
                if guess not in i[1]:
                    if guess in ["Male", "Female"]:
                        messagebox.showinfo(
                            "Game info", "The person is not a " + guess.lower() + "!"
                        )
                    elif guess == "Bald":
                            messagebox.showinfo(
                                "Game info", "The person is not " + guess.lower() + "!"
                            )
                    elif guess in [
                        "Small mouth",
                        "Big mouth",
                        "Mustache",
                        "Hat",
                        "Beard",
                        "Small nose",
                        "Big nose",
                    ]:
                        messagebox.showinfo(
                            "Game info",
                            "The person doesn't have a " + guess.lower() + "!",
                        )
                    else:
                        messagebox.showinfo(
                            "Game info",
                            "The person doesn't have " + guess.lower() + "!",
                        )
        place_x_plr(guess)
        for m in x_add_list:
            create_x(m)
        computer_guess()
    else:
        messagebox.showerror(
            "Game Info",
            "Invalid Choice. Refer to the possible guesses for a possible choice.",
        )

def computer_guess():
    global turn_number
    
    if len(comp_char_list) > 0:
        if turn_number == 0:
            messagebox.askquestion("Computer Guess", "Is your person a male?")
            comp_guess("Male")
            turn_number += 1
        elif turn_number == 1:
            messagebox.askquestion("Computer Guess", "Does your person have a small mouth?")
            comp_guess("Small mouth")
            turn_number += 1
        elif turn_number == 2:
            messagebox.askquestion("Computer Guess", "Does your person have blonde hair?")
            if comp_guess("Blonde hair"):
                turn_number += 1
            else:
                turn_number += 0.5  
        elif turn_number == 2.5:
            messagebox.askquestion("Computer Guess", "Does your person have brown hair?")
            if comp_guess("Brown hair"):
                turn_number = 3
            else:
                turn_number += 0.25
        elif turn_number == 2.75:
            messagebox.askquestion("Computer Guess", "Does your person have white hair?")
            comp_guess("White hair")
            turn_number = 3
        elif turn_number == 3:
            messagebox.askquestion("Computer Guess", "Does your person have a small nose?")
            comp_guess("Small nose")   
            turn_number += 1 
        elif turn_number == 4:
            messagebox.askquestion("Computer Guess", "Does your person have a mustache")
            comp_guess("Mustache")    
            turn_number += 1   
        elif turn_number == 5:
            messagebox.askquestion("Computer Guess", "Does your person have brown eyes?")
            comp_guess("Brown eyes") 
            turn_number += 1  
        elif turn_number == 6:
            messagebox.askquestion("Computer Guess", "Does your person have glasses?")
            comp_guess("Glasses") 
            turn_number += 1
        elif turn_number == 7:
            messagebox.askquestion("Computer Guess", "Is your person bald?")
            comp_guess("Bald") 
            turn_number += 1
        elif turn_number == 7:
            messagebox.askquestion("Computer Guess", "Does your person have a hat?")
            comp_guess("Hat") 
            turn_number += 1          
    if len(comp_char_list) == 1:
        messagebox.askyesno("Computer Guess", "The computer guesses " + comp_char_list[0] + "!\nIs the computer right?")
        if comp_char_list[0] == player_person_choice:
            messagebox.showinfo("Game over!", "The computer wins!")
            quit()
    else:
        messagebox.showinfo("Game info", "Players turn!")
    
def comp_guess(guess):
    global comp_char_list
    if len(comp_char_list) > 1:
        for i in characteristic:
            if i[0] == player_person_choice:
                for x in i[1]:
                    if x == guess:
                        comp_guess_true = True
                        break
                    else:
                        comp_guess_true = False
                break
        
        for i in characteristic:
            if comp_guess_true:
                for x in i[1]:
                    if x != guess:
                        not_in = False
                    else:
                        not_in = True
                        break
                if not not_in:
                    try:
                        comp_char_list.remove(i[0])
                    except:
                        pass
            else:
                for x in i[1]:
                    if x == guess:
                        not_in = False
                        break
                    else:
                        not_in = True
                if not not_in:
                    try:
                        comp_char_list.remove(i[0])
                    except:
                        pass  
        return comp_guess_true

def place_x_plr(guess):
    global x_add_list
    for i in characteristic:
        if i[0] == computer_person_choice:
            for x in i[1]:
                if x == guess:
                    plr_guess_true = True
                    break
                else:
                    plr_guess_true = False
            break
    
    for i in characteristic:
        if plr_guess_true:
            for x in i[1]:
                if x != guess:
                    plr_not_in = False
                else:
                    plr_not_in = True
                    break
            if not plr_not_in:
                try:
                    x_add_list.append(i[0])
                except:
                    pass
        else:
            for x in i[1]:
                if x == guess:
                    plr_not_in = False
                    break
                else:
                    plr_not_in = True
            if not plr_not_in:
                try:
                    x_add_list.append(i[0])
                except:
                    pass  

def create_x(name):
    global char_cords_dict
    cords = char_cords_dict[name]
    x = cords[0]
    y = cords[1]
    img1 = ImageTk.PhotoImage(Image.open("X_image.png"))
    canvas.create_image(x, y, anchor=NW, image=img1)
    canvas.image = img1
    img_ref_dict[name] = img1

def guess_person_plr():
    player_guess_c = str(player_guess_comp.get()).strip().capitalize()
    if computer_person_choice == player_guess_c:
        messagebox.showinfo(
            "Game info",
            "You won! The computers person was " + computer_person_choice + "!",
        )
        quit()
    else:
        messagebox.showinfo("Game info", "You got it wrong!")
        computer_guess()

def show_rules():
    root3 = Tk()
    root3.title("Rules")
    root3.geometry("800x550")
    root3.resizable(False, False)
    r_text_1 = "Guess Who is a two player game where players use\ndifferential yes or no questions to isolate a hidden character.\nThe first player to guess the other players or computers hidden\ncharacter wins.\nGame Setup:\nEach player chooses a person. This person represents the character\nyour opponent has to guess.\nThe player goes first, beginning by guessing a characteristic. \nExample: “ Does your character have brown hair?”\nIf they say, “yes,” the asking player presses the button for all of\nthe characters without brown hair. If they say, “no,”the asking player\npresses the button for the characters that have brown hair.\nThrough the process of elimination, players will eventually be able to\n“guess” the name of the opponents character.\nWinning the game:\nEach player gets one yes or no question per turn and if a player\nsuccessfully guesses their opponents hidden character then they win!"
    rules_text = Label(root3, text=r_text_1, font=("arial", 25))
    rules_title = Label(
        root3, text="Rules", width=15, relief="solid", font=("arial", 40, "bold")
    )
    rules_text.place(x=0, y=50)
    rules_title.place(x=230, y=0)

    root3.mainloop()

char_list = [
    "Jean-claude",
    "Pierre",
    "Jean",
    "Amelie",
    "Mirabelle",
    "Isabelle",
    "Antonin",
    "Bernard",
    "Owen",
    "Dylan",
    "Herbert",
    "Christine",
    "Luc",
    "Cecilian",
    "Lionel",
    "Benoit",
    "Robert",
    "Charline",
    "Renaud",
    "Michel",
    "Pierre-louis",
    "Etienne",
    "Henri",
    "Damien",
]
player_choices = [
    "Male",
    "Female",
    "Glasses",
    "Brown eyes",
    "Bald",
    "White hair",
    "Small mouth",
    "Mustache",
    "Brown hair",
    "Big mouth",
    "Small nose",
    "Blue eyes",
    "Hat",
    "Long hair",
    "Black hair",
    "Earrings",
    "Blonde hair",
    "Ginger hair",
    "Beard",
    "Big nose",
]
computer_person_choice = r.choice(char_list)


window = Tk()
window.title("Guess Who")
window.geometry("920x800")
window.resizable(False, False)
canvas = Canvas(window, width=920, height=800)
canvas.pack()
img3 = ImageTk.PhotoImage(Image.open("characters2.png"))
canvas.create_image(0, 0, anchor=NW, image=img3)
player_choice_char = StringVar()
input_box1 = Entry(window, textvar=player_choice_char)
choose_person = Label(window, text="Choose a person:", font=("arial", 25, "bold"))
canvas.create_window(530, 650, window=input_box1)
canvas.create_window(320, 650, window=choose_person)
choose_person_button = Button(
    window,
    text="Choose person",
    fg="black",
    bg="white",
    relief="groove",
    font=("arial", 30, "bold"),
    command=submit_player,
)
canvas.create_window(400, 700, window=choose_person_button)

window.mainloop()


root = Tk()
root.title("Guess Who")
root.geometry("920x800")
root.resizable(False, False)
canvas = Canvas(root, width=920, height=800)
canvas.pack()

player_guess = StringVar()

img = ImageTk.PhotoImage(Image.open("characters.png"))
input_box = Entry(root, textvar=player_guess)
guess_who_text = Label(root, text="Your guess:", width=10, font=("arial", 25, "bold"))
line = Label(root, text="_" * 200, font=("arial", 10, "bold"))
options_button = Button(
    root,
    text="Show all possible guesses",
    width=22,
    fg="black",
    bg="white",
    relief="groove",
    font=("arial", 20, "bold"),
    command=options_page,
)
guess_button = Button(
    root,
    text="Guess!",
    width=10,
    fg="black",
    bg="white",
    relief="groove",
    font=("arial", 30, "bold"),
    command=play_game,
)
rules_button = Button(
    root,
    text="Rules",
    fg="black",
    bg="white",
    relief="groove",
    font=("arial", 30, "bold"),
    command=show_rules,
)
player_guess_comp = StringVar()
input_box_name = Entry(root, textvar=player_guess_comp)
guess_who_text_1 = Label(root, text="Guess a person:", font=("arial", 25, "bold"))
guess_button1 = Button(
    root,
    text="Guess!",
    width=10,
    fg="black",
    bg="white",
    relief="groove",
    font=("arial", 30, "bold"),
    command=guess_person_plr,
)
player_choice_text = Label(
    root, text="Your person choice is "+player_person_choice, fg="red", relief="solid", font=("arial", 20, "bold")
)

canvas.create_window(700, 745, window=player_choice_text)
canvas.create_window(400, 650, window=input_box)
canvas.create_window(690, 690, window=rules_button)
canvas.create_window(225, 650, window=guess_who_text)
canvas.create_window(400, 615, window=line)
canvas.create_window(680, 650, window=options_button)
canvas.create_window(400, 690, window=guess_button)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.create_window(400, 730, window=input_box_name)
canvas.create_window(200, 730, window=guess_who_text_1)
canvas.create_window(400, 770, window=guess_button1)

input_box.focus()

root.mainloop()

