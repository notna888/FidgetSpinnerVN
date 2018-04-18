# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f1 = Character("Tsundere") #It's not like I like you or anything
define f2 = Character("Deredere") #LOVE ME LOVE ME LOVE ME
define f3 = Character("Himedere") #Worship me peasant
define f4 = Character("Bazza") #Bazza is best character

$ gender = "male"
$ money = 0
$ f1Like = 0
$ f2Like = 0
$ f3Like = 0
$ f4Like = 0
$ havepills = False


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    menu:
        "I am a boy":
            $ she_he = "he"
            $ him_her = "him"

        "I am a girl":
            $ she_he = "she"
            $ him_her = "him"

        #"I am neither":


    scene bg main


    call dayOne()


    # This ends the game.

    return


label dayOne():
    "Well, today is my first day at my new job at the fidget spinner shop"
    "I've done a bunch of retail work before, so I'm not expecting it to be any different"

    # These display lines of dialogue.

    "Voice 1" "Hey~!"
    "Wait, what?"
    "Voice 2" "What are you doing Deredere? We can't talk to the humans"
    f2 "Awww, but %(she_he)s's so cute"
    "I'm sorry but who's talking?"
    f2 "Over here~!"

    show fidget1 normal

    "It sounds like the voice is coming from over on a shelf of products"

    f2 "Hey! You're looking at me"

    "Is this some sort of prank?"

    f2 "Nope, you know those kid shows where when the child would leave the room and the toys would come to life?"
    f2 "Well, they were a lot closer to reality than what they thought, toys are sentient"

    menu:
        "Decide your going to go to the doctors after work today":
            #some explanitory text
            pass

        "Ignore the spinners":
            #
            pass

        "Entertain the idea that toys are sentient":
            #
            pass

    return


label dayTwo():
    pass

label dayThree():
    pass

label gotodoctors():
    pass
