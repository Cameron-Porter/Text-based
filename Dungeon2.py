from sys import exit
import random

# Variables -----------------------------------------------

viper = True
goblin = True
dragon = True
sword = False
bow = False
magic = False

# Functions -----------------------------------------------


# Sequence 1 -----------------------------------------------


def beginning():
    print("""Welcome to Morrowind, the land of monsters and mystics.
We have a very important adventure for you, if you choose to accept it.
What say you adventurer? Do you accept this daunting task?""")
    choice = input("> ")
    if "yes" in choice or "accept" in choice:
        weapon_choice()
    else:
        print("I'm sorry to hear that you're a cotton headed ninny muggin, who doesn't like to have fun.")
        exit()

# Sequence 2 -----------------------------------------------


def weapon_choice():

    global sword
    global bow

    print("""Thank you for accepting this adventure! You will not regret it.
Please select one of the following as your starting weapon: sword or bow.""")
    choice = input("> ")
    if "sword" in choice and "bow" in choice:
        print("You may only select one weapon at this time. Which do you choose?")
        choice = input("> ")
        if "sword" in choice:
            print("""As I predicted, the sword looks like it was made with you in mind.
I wish you the best as you begin your adventure. I pray you good fortune.""")
            sword = True
        elif "bow" in choice:
            print("""Ah, the bow is a wise choice. You must have a keen eye.
I wish you the best as you begin your adventure. I pray you good fortune.""")
            bow = True
    elif "sword" in choice:
        print("""As I predicted, the sword looks like it was made with you in mind.
I wish you the best as you begin your adventure. I pray you good fortune.""")
        sword = True
    elif "bow" in choice:
        print("""Ah, the bow is a wise choice. You must have a keen eye.
I wish you the best as you begin your adventure. I pray you good fortune.""")
        bow = True
    room_1()

# Room_1 -----------------------------------------------


def room_1():
    print("""
As you leave the main post, you journey down a long winding path.
The sun is just beginning to rise above the red kissed trees,
wildlife is all around, and you suddenly come to a fork in the road.
Do you wish to go left or proceed right?""")
    choice = input("> ")
    if "left" in choice:
        left()
    else:
        right()

# Left Side of fork -----------------------------------------------


def left():

    global viper

    if viper:
        print("""As you head down the left path you see a poisonous viper blocking the path.
The viper has wicked fast reflexes and can spit it's poison into your eyes if you get too close.
What do you want to do? Attack or turn back?""")
        choice = input("> ")
        if bow:
            if "attack" in choice:
                print("""You unsheathe an arrow and slowly draw back your bow string.
You take aim and with a deep inhale and exhale, you release.
The arrow flies true and you kill the viper!""")
                viper = False
                left_2()
            elif "back" in choice:
                print("You turn back to the fork and take the other path.")
                right()
        elif sword:
            if "attack" in choice:
                game_over("""You unsheathe your sword and sprint toward the viper.
You come with fire in your eyes, ready to tackle this beast.
Only to have the viper extinguish that fire with it's poison, 
rendering you blind. You sword drops to the ground as you grasp your face and scream.
You know the end is near, the viper slowly encircles you before it lashes out for the kill.""")
            elif "back" in choice:
                print("You turn back to the fork and take the other path.")
                right()
    else:
        print("""As you head down the left path, you see the dead viper rotting away.
Thankful you previously came out victorious, you charge ahead to see what adventures await!""")
        left_2()


def left_2():

    global sword
    global magic

    print("""
Just a bit further up you notice a man lying against a tree.
You call out to him, "Hey man!", yet no response.
As you approach, you see it is a skeleton beneath the clothes.
Do you search the dead man's body or leave him to rest in peace?""")
    choice = input("> ")
    if sword is False:
        if "search" in choice:
            print("""You search the body to find a sword. You now can attack at short and long ranges.""")
            sword = True
        elif "leave" in choice or "rest" in choice or "peace" in choice:
            print("You leave the man to rest in peace and continue your journey.")
        left_3()
    else:
        if "search" in choice:
            print("""You search the body to find a fire ball tome.
As you begin to read it, you become enlightened and now know the 
mystical ways of the fire clan. You have been granted the fire ball skill.""")
            magic = True
        elif "leave" in choice or "rest" in choice or "peace" in choice:
            print("You leave the man to rest in peace and continue your journey.")
        left_3()


def left_3():
    print("""
You trudge on, and see the path starting to widen. You begin to hear strange
growling sounds in the distance, but cannot quick make out what the cause is.
Do you continue to investigate, or backtrack to the other side of the fork to
see what more is over there?""")
    choice = input("> ")
    if "continue" in choice or "investigate" in choice:
        boss()
    else:
        right()

# Right Side of fork -----------------------------------------------


def right():

    global goblin

    print("""
As you head down the right path, you smell a horrid stench.
Out of the bushed jumps an armed goblin with shield in hand.
What will you do? Attack or retreat to the other side of 
the fork for safety?""")
    choice = input("> ")
    if sword:
        if "attack" in choice:
            print("""You unsheathe your sword and parry the goblin's first attack.
You quickly regain your bearing and drive the goblin back to his
campsite. He lunges at you with all his might. You side step with
your sword tucked close, only to thrust it deep within his chest.
The goblin gasps for air but only blood comes pouring out his mouth.""")
            goblin = False
            right_2()
        elif "retreat" in choice:
            print("You turn back to the fork and take the other path.")
            left()
    elif sword is False:
        if "attack" in choice:
            game_over("""You unsheathe an arrow and draw back your bow string.
You take aim and with a swift release, your arrow goes flying.
The goblin quickly blocks with his shield and cuts off your head!
...Sucks to Suck...""")
        elif "retreat" in choice:
            print("You turn back to the fork and take the other path.")
            left()


def right_2():

    global bow
    global magic

    print("""
You look up from the dying goblin to see a sparkle in the bushes.
Do you investigate or continue on?""")
    choice = input("> ")
    if bow:
        if "investigate" in choice:
            print("""You search the treasure to find a lightning bolt tome.
As you begin to read it, you become enlightened and now know the 
mystical ways of the thunder clan. You have been granted the lightning bolt skill.""")
            magic = True
            right_3()
        elif "continue" in choice:
            print("You leave the mysterious sparkle and push onward.")
            right_3()
    else:
        if "investigate" in choice:
            print("""You investigate the sparkle to find the goblin's hidden treasure.
Among the treasure is a golden bow and quiver of arrows, which you equip.""")
            bow = True
            right_3()
        else:
            print("You leave the mysterious sparkle and push onward.")
            right_3()


def right_3():
    print("""
You trudge on, and see the path starting to widen. You begin to hear strange
growling sounds in the distance, but cannot quick make out what the cause is.
Do you continue forward, or backtrack to the other side of the fork to
see what more is over there?""")
    choice = input("> ")
    if "continue" in choice or "forward" in choice:
        boss()
    else:
        left()

# Boss -----------------------------------------------


def boss():

    global dragon
    global magic
    global sword
    global bow

    print("""
You have finally made it to where the two paths meet once again.
Sleeping where they converge is a monstrous dragon. What weapon
could even work against such a horrific being?!""")
    choice = input("> ")
    if magic:
        if "sword" in choice:
            game_over("""
You draw your sword and charge with all your might,
The dragon sneezes a small fire ball that engulfs you in 
flames. You die a snotty death.""")
        elif "bow" in choice:
            game_over("""
You pull an arrow from your quiver, draw your bow string back
and upon releasing your arrow you cause a minor itch for the dragon.
In it's attempt to relieve the itch with it's tail, it ends up crushing
your thoracic cavity as it swings it's tail. Causing you to die a torturous death.""")
        else:
            print("""
You use your magic like a ninja Merlin and fry up that dragon for supper.""")
    else:
        if "sword" in choice:
            game_over("""
You draw your sword and charge with all your might,
The dragon sneezes a small fire ball that engulfs you in 
flames. You die a snotty death.""")
        elif "bow" in choice:
            game_over("""
You pull an arrow from your quiver, draw your bow string back
and upon releasing your arrow you cause a minor itch for the 
dragon. In it's attempt to relieve the itch with it's tail, it 
ends up crushing your thoracic cavity as it swings it's tail.
Causing you to die a torturous death.""")

# Start


def start():
    beginning()

# Game Over


def game_over(s):

    global viper
    global goblin
    global dragon
    global sword
    global bow
    global magic

    viper = True
    goblin = True
    dragon = True
    sword = False
    bow = False
    magic = False

    print(s)
    choice = input("""Do you want to play again? ( y / n )
> """)
    if "y" in choice:
        start()
    elif "n" in choice:
        exit(0)

# Game


start()
