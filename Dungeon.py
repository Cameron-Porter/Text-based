from sys import exit

# Variables

space_worm = True
millennium_falcon = False

# Functions

# Room 1


def room1():
    print("You are in a small room with unicorns all over the walls.")
    print("It is blindingly bright, but you can somewhat make out 3 doors.")
    print("They lead east, north, and west. Which do you open?")

    choice = input("> ")
    if "east" in choice.lower():
        room2()
    if "north" in choice.lower():
        room3()
    if "west" in choice.lower():
        game_over("""You carefully go through the horny passage heading west. 
After walking for 5 minutes, you see a dead end with a unicorn mural painted on it. 
When you turn around to backtrack, the unicorn becomes animated and craps toxic rainbows on you. 
You slowly die in this gay hallway, never to be seen again.""")
    else:
        room1()

# Room 2


def room2():

    global millennium_falcon

    print("Upon entering the room, you find your shoes have vanished.")
    print("Scattered on the floor is a 10,000 piece lego set for the Millennium Falcon.")
    print("Again, you find 2 more doors in this spacey place. The first leading east, the second leading North.")
    print("The first door has a mysterious mist emanating from beneath it.")
    print("The second door is adorned with bloody viking skulls.")
    print("The door to the west heads back to the first room.")
    print("What do you do?")

    choice = input("> ")
    if "east" in choice.lower():
        game_over(""""You open the door and mist suddenly engulfs your body.
You begin hallucinating that you are married to the most beautiful woman you've ever laid eyes on.
While you think you have it made, the most wretched woman you've ever seen begins to eat you alive.
Although you are slowly dying, at least you believe it is a dream come true.""")
    elif "north" in choice.lower():
        room3()
    elif "west" in choice.lower():
        room1()
    elif "millennium" in choice.lower() or "falcon" in choice.lower():
        print("""You build the Millennium Falcon and it now flies behind you as a protective familiar.
You then proceed through the north door.""")
        millennium_falcon = True
        room3()
    else:
        room2()

# Room 3


def room3():

    global space_worm

    print("You burst through the room and suddenly are confronted by a flying space worm!!!")

    if millennium_falcon:
        print("""Thank goodness you built that Millennium Falcon. It just flew into the worm's 
mouth and self destructed, saving you from utter death. You then proceed through the final door to safety""")
        game_over("Congratulations, you win PTSD for life.")
    else:
        print("WHAT ARE YOU GOING TO DO???")
        input("> ")
        game_over("""Your attempt at survival failed and you have been devoured by the space worm.""")

# Start


def start():
    room1()

# Game Over


def game_over(s):

    global space_worm
    global millennium_falcon

    space_worm = True
    millennium_falcon = False

    print(s)
    choice = input("""Do you want to play again? ( y / n )
> """)
    if "y" in choice:
        start()
    elif "n" in choice:
        exit(0)

# Game


start()
