import time
import random
out = []
element = ""


def prt_list(list):
    for j in list:
        print(j, flush=True)
        if len(j) < 70:
            time.sleep(2)
        else:
            time.sleep(3)


def prt_single(sentence, num):
    print(sentence, flush=True)
    time.sleep(num)


# The initial story.
def intro():
    global element
    element = random.choice(["gorgon", "troll", "wicked fairies", "pirates"])
    story = [
        "You find yourself in an open field, filled with grass and yellow"
        " wild flowers.", f"Rumor has it that a {element} is somewhere "
        "around here and has been terrifying the nearby villages.",
        "Infront of you is a house.",
        "To your right is a dark cave.",
        "In your hand you hold your trusty (but not very effective) dagger.\n"
    ]
    prt_list(story)


# The player decides whether choose to knock the door or move towards the cave.
def choose_1():
    act = [
        "Enter 1 to knock on the door of the house.",
        "Enter 2 to peer into the cave.", "What would you do?"
        ]
    prt_list(act)
    response = str(input("(Please enter 1 or 2.)\n"))
    return response


# Related to the case player chose number 1, knocking on the door of the
# house, in choose_1.
def choose_11():
    act11 = [
        "You approach the door of the house.",
        f"You are about to knock when the door opens and out steps "
        f"a {element}.", f"The {element} attacks you!"
        ]
    act1 = [
        "You approach the door of the house.",
        f"You are about to knock when the door opens and out steps "
        f"a {element}.", f"Eep! This is the {element}'s house!",
        f"The {element} attacks you!", "You feel a bit under_prepared for "
        "this, what with only having a tiny dagger."]
    if "sword" in out:
        prt_list(act11)
    else:
        prt_list(act1)
    response1 = str(input("Would you like to (1) fight or (2) run away?\n"))
    return response1


# Related to the answer for the choose_11, either fight or run away.
def choose_111():
    response1 = choose_11()
    if response1 == "1":
        act3 = [
            "You do your best...", f"But your dagger is no match for "
            f"the {element}.", "You have been defeated!\n"
            ]
        act4 = [
            f"As the {element} moves to attack, you unsheath your new sword.",
            "The Sword of Ogroth shines brightly in your hand as you brace "
            "yourself for the attack.", f"But the {element} takes one look "
            "at your shiny new toy and runs away!",
            f"You have rid the town of the {element}. You are victorious!\n"
            ]
        if "sword" in out:
            prt_list(act4)
            play_again()
        else:
            prt_list(act3)
            play_again()
    elif response1 == "2":
        prt_single(
            "You run back to into the field. Luckily, "
            "you don't seem to have been followed.\n", 2
            )
    else:
        prt_single("No, pay more attention!", 2)
        choose_111()


# Related to the case when player chose number 2, moving towards the cave,
# in choose_1.
def choose_12():
    prt_single("You peer cautiously into the cave.", 2)
    act2 = [
        "It turn out to be only a very small cave.",
        "Your eye catches a glint of metal behind a rock.",
        "You have found the magical Sword of Ogoroth!",
        "You discard your silly old dagger and take the sword with you.",
        "You walk back into the field.\n"
        ]
    if "sword" in out:
        prt_single(
            "You have been here before, and gotten all the good stuff. "
            "It's just an empty cave now.", 2
            )
        prt_single("You walk back out to the field.", 2)
    else:
        prt_list(act2)
        out.append("sword")


def game():
    response = choose_1()
    if response == "1":
        choose_111()
    elif response == "2":
        choose_12()
    else:
        game()
    game()


# Adventure's Game.
def Adventure():
    intro()
    game()
    play_again()


# Playing again.
def play_again():
    global out
    prt_single("Would you like to play again?", 2)
    response2 = str(input("Please enter y for yes and n for no.\n").lower())
    if response2 == "y":
        out = []
        Adventure()
    elif response2 == "n":
        exit()
    else:
        play_again()


Adventure()
