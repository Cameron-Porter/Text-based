from sys import exit
import random

# ____________________ Variables ____________________


# Weapons


sword = False
bow = False
magic = False
inferno = False
snow_storm = False

# Enemies


black_eagle = True
eagle_HP = 100
fire_serpent = True
snake_HP = 100
goblin = True
goblin_HP = 100
yeti = True
yeti_HP = 100

# Dictionary Stats

stats = {
	'sword': {'Class': 'Warrior', 'HP': 120, 'MP': 25, 'ATK': 35, 'DEF': 35, 'LCK': 10},
	'bow': {'Class': 'Ranger', 'HP': 100, 'MP': 50, 'ATK': 25, 'DEF': 25, 'LCK': 25}
}

warrior = False
ranger = False

# ____________________ Functions (Rooms) ____________________


def beginning():
	print("""Welcome to the Labyrinth. Home of many monstrous creatures.
Are you ready to get started on your adventure?""")
	choice = input("> ")
	if "no" in choice:
		exit()
	else:
		weapon_choice()


def weapon_choice():

	global sword
	global bow

	print("""Would you like the bow or sword?""")
	choice = input("> ")
	if "sword" in choice and "bow" in choice:
		print("Stop being greedy, you may only choose one weapon at this time.")
		weapon_choice()
	elif "sword" in choice:
		sword = True
		ready()
	elif "bow" in choice:
		bow = True
		ready()
	else:
		print("Please select one of the following weapons:")
		weapon_choice()


def ready():

	global sword
	global warrior
	global bow
	global ranger

	if sword:
		print("""Are you sure you want the sword? You are
about to embark on your dangerous adventure.""")
		choice = input("> ")
		if "yes" in choice:
			warrior = True
			split()
		elif "no" in choice:
			sword = False
			weapon_choice()
		else:
			print("It's a yes or no question bro...")
			ready()
	else:
		print("""Are you sure you want the bow? You are
about to embark on your dangerous adventure.""")
		choice = input("> ")
		if "yes" in choice:
			ranger = True
			split()
		elif "no" in choice:
			bow = False
			weapon_choice()
		else:
			print("It's a yes or no question bro...")
			ready()


def split():

	global warrior
	print("Below are your stats:")
	if warrior:
		print(stats["sword"])
	else:
		print(stats["bow"])
	print("""
A ways down the road you see an old ferryman sleeping in
his boat. Off in the distance you see the red glow of magma
highlighting the distant island peak. But with the cool fog
coming in, you are unable to see any more details. Do you 
you wish to wake the ferryman or continue down the current path?""")
	choice = input("> ")
	if "wake" in choice or "ferryman" in choice:
		boat()
	else:
		path()

# ____________________ Boat/Island ____________________


def boat():
	print("""You wake the ferryman and request he take you
across the way to the island. He warns you of the dangers 
that lurk within the fog, and how men have vanished from his
ferry never to be heard of again.""")
	choice = input("""Would you like to take the ferry or turn back?
> """)
	if "ferry" in choice or "take" in choice:
		boat2()
	elif "back" in choice:
		split()
	else:
		print("Psh, why you making this hard...now we have to do this scene over again.")
		boat()


def boat2():
	global black_eagle
	global eagle_HP
	global sword

	if black_eagle:
		print("""As you make your way to the island, you hear a deafening
screeching sound. You look all around but cannot see
due to the fog. Suddenly a Great Black Eagle dismisses
the fog with its wings and begins to attack the ferry.
Eagle HP = """ + str(eagle_HP))
		choice = input("""No turning back now. Will you attack? Or puss out?
> """)
		if "attack" in choice:
			if sword:
				while black_eagle:
					if eagle_HP <= 0:
						print("The eagle has been vanquished.")
						black_eagle = False
					else:
						while eagle_HP > 0:
							for x in range(1):
								if random.randint(1, 2) == 2:
									stats["sword"]["HP"] -= 25
									print("You were bit! Your HP is now: ", stats["sword"]["HP"])
								else:
									eagle_HP -= stats["sword"]["ATK"]
									print("Your attack was successful, Eagle HP = " + str(eagle_HP))
							if eagle_HP > 0:
								if stats["sword"]["HP"] <= 0:
									game_over("Increase your training and try again.")
								else:
									choice = input("Attack again? > ")
									if "no" in choice:
										game_over("Your lack of commitment killed you, you deserved it.")
							else:
								black_eagle = False
					print("""You use your sword to cut out the Great Black
Eagle's eyes. With it blindly flailing about, it crashes into
the sea. The ferryman goes full speed ahead and pins the Eagle
under the water to perish.
""")
					boat3()
			else:
				while eagle_HP > 0:
					for x in range(1):
						if random.randint(1, 4) == 2:
							stats["bow"]["HP"] -= 25
							print("You were bit! Your HP is now: ", stats["bow"]["HP"])
						else:
							eagle_HP -= stats["bow"]["ATK"]
							print("Your attack was successful, Eagle HP = " + str(eagle_HP))
					if eagle_HP > 0:
						if stats["bow"]["HP"] == 0:
							game_over("Increase your training and try again.")
						else:
							choice = input("Attack again? > ")
							if "no" in choice:
								game_over("Your lack of commitment killed you, you deserved it.")
					else:
						black_eagle = False
				print("""You use your bow to shoot out the Great Black
Eagle's eyes. With it blindly flailing about, it crashes into
the sea. The ferryman goes full speed ahead and pins the Eagle
under the water to perish.
""")
				boat3()
		else:
			game_over("Your lack of balls has become your demise.")


def boat3():

	global snow_storm

	print("""You look over the edge of the ferry into the water and notice
ice forming from where the carcass rests. The ice is eminating
a bright blue aura.
""")
	choice = input("""Will you reach out and touch the ice?
> """)
	if "yes" in choice:
		snow_storm = True
		print("""You touch the ice and feel an internal chill rush through your veins. 
As you pull your hand back into the boat, you see the cool fog encircle your arm. 
You have now acquired the skill: Snow Storm. Allowing you to defeat fire monsters.""")
	elif "no" in choice:
		print("You decide to play it safe and not touch the ice.")
	else:
		print("Remember the K.I.S.S. method...keep it simple stupid, it's a yes or no question.")
		boat3()

	choice = input("""Do you wish to continue on this path? 
> """)
	if "no" in choice:
		path()
	else:
		island()


def island():
	print("""Finally, you have made it to the island. You can now tell it was glowing red 
for good reason, with magma all around, the heat is almost unbearable. Upon walking up a nearby trail 
you see large statues of serpents scattered about the path.""")
	
	choice = input("""Continue or turn back?
> """)
	if "continue" in choice:
		island2()
	elif "turn" in choice:
		path()
	else:
		print("Please type either 'continue' or 'turn back'.")
		choice = input("> ")
		if "continue" in choice:
			island2()
		elif "turn" in choice:
			path()
		else:
			game_over("""You fail at following directions, typing, or in life general...you've 
died of the plague of incompetence. May you rest in peace.""")


def island2():

	global fire_serpent
	global snake_HP
	global snow_storm
	global inferno
	global sword
	
	print("""You crest the top of the island to a raging fire. As you inspect the flames,
they begin to move across the ground. In a flash, you see the fire is engulfing a huge serpent
yet is not consuming it. The serpent turns toward you ready to attack!
""")
	print("The following is what you have to attack with:")
	if sword:
		print("Sword")
	else:
		print("Bow")
	if snow_storm:
		print("""Snow Storm
""")
	choice = input("""What will you attack with?!
> """)
	if snow_storm:
		if "snow" in choice:
			print("""You suddenly remember you just received the Snow Storm skill. You quickly cast
the storm over the serpent and extinguish the flames.
""")
			fire_serpent = False
			inferno = True
			island3()
		elif sword:
			while fire_serpent:
				if snake_HP <= 0:
					print("The serpent has been vanquished.")
					fire_serpent = False
					island3()
				else:
					while snake_HP > 0:
						for x in range(1):
							if random.randint(1, 4) == 2:
								stats["sword"]["HP"] -= 25
								print("You were burned! Your HP is now: ", stats["sword"]["HP"])
							else:
								snake_HP -= stats["sword"]["ATK"]
								print("Your attack was successful, Serpent HP = " + str(snake_HP))
						if snake_HP > 0:
							if stats["sword"]["HP"] <= 0:
								game_over("Increase your training and try again.")
							else:
								choice = input("Attack again? > ")
								if "no" in choice:
									game_over("Your lack of commitment killed you, you deserved it.")
					else:
						fire_serpent = False
				print("""You use your sword to cut out the Fire Serpent's heart. You stand in amazement 
		as it's power of fire transfers to you. You now have the fire ball ability!
		""")
				fire_serpent = False
				inferno = True
				island3()
		else:
			while fire_serpent:
				if snake_HP <= 0:
					print("The serpent has been vanquished.")
					fire_serpent = False
					island3()
				else:
					while snake_HP > 0:
						for x in range(1):
							if random.randint(1, 4) == 2:
								stats["bow"]["HP"] -= 25
								print("You were burned! Your HP is now: ", stats["bow"]["HP"])
							else:
								snake_HP -= stats["bow"]["ATK"]
								print("Your attack was successful, Serpent HP = " + str(snake_HP))
						if snake_HP > 0:
							if stats["bow"]["HP"] <= 0:
								game_over("Increase your training and try again.")
							else:
								choice = input("Attack again? > ")
								if "no" in choice:
									game_over("Your lack of commitment killed you, you deserved it.")
						else:
							fire_serpent = False
				print("""You use your bow to shoot out the Fire Serpent's heart. You stand in amazement 
as it's power of fire transfers to you. You now have the fire ball ability!
""")
				fire_serpent = False
				inferno = True
				island3()
	elif sword:
		while fire_serpent:
			if snake_HP <= 0:
				print("The serpent has been vanquished.")
				fire_serpent = False
				island3()
			else:
				while snake_HP > 0:
					for x in range(1):
						if random.randint(1, 4) == 2:
							stats["sword"]["HP"] -= 25
							print("You were burned! Your HP is now: ", stats["sword"]["HP"])
						else:
							snake_HP -= stats["sword"]["ATK"]
							print("Your attack was successful, Serpent HP = " + str(snake_HP))
					if snake_HP > 0:
						if stats["sword"]["HP"] <= 0:
							game_over("Increase your training and try again.")
						else:
							choice = input("Attack again? > ")
							if "no" in choice:
								game_over("Your lack of commitment killed you, you deserved it.")
				else:
					fire_serpent = False
			print("""You use your sword to cut out the Fire Serpent's heart. You stand in amazement 
as it's power of fire transfers to you. You now have the fire ball ability!
""")
			fire_serpent = False
			inferno = True
			island3()
	else:
		while fire_serpent:
			if snake_HP <= 0:
				print("The serpent has been vanquished.")
				fire_serpent = False
				island3()
			else:
				while snake_HP > 0:
					for x in range(1):
						if random.randint(1, 4) == 2:
							stats["bow"]["HP"] -= 25
							print("You were burned! Your HP is now: ", stats["bow"]["HP"])
						else:
							snake_HP -= stats["bow"]["ATK"]
							print("Your attack was successful, Serpent HP = " + str(snake_HP))
					if snake_HP > 0:
						if stats["bow"]["HP"] <= 0:
							game_over("Increase your training and try again.")
						else:
							choice = input("Attack again? > ")
							if "no" in choice:
								game_over("Your lack of commitment killed you, you deserved it.")
				else:
					fire_serpent = False
			print("""You use your bow to shoot out the Fire Serpent's heart. You stand in amazement 
as it's power of fire transfers to you. You now have the fire ball ability!
""")
			fire_serpent = False
			inferno = True
			island3()


def island3():
	print("This is as far as I've coded...be patient.")

# ____________________ Path/Cave/Mountain ____________________


def path():
	print("""Sorry, haven't created this path yet...rerouting to the ferry:
""")
	boat()


def cave():
	print()


def cave2():
	print()


def cave3():
	print()


def path2():
	print()


def path3():
	print()


def mountain():
	print()


def mountain2():
	print()


def mountain3():
	print()
# ____________________ Start ____________________


def start():
	beginning()

# ____________________ Game Over ____________________


def game_over(s):

    global black_eagle
    global fire_serpent
    global goblin
    global yeti
    global sword
    global bow
    global magic
    global inferno
    global snow_storm
    global eagle_HP

    black_eagle = True
    fire_serpent = True
    goblin = True
    yeti = True

    sword = False
    bow = False
    magic = False
    inferno = False
    snow_storm = False

    eagle_HP = 100

    global stats
    stats["sword"]["HP"] = 120
    stats["bow"]["HP"] = 100

    print(s)
    choice = input("""Do you want to play again? ( y / n )
> """)
    if "y" in choice:
        start()
    elif "n" in choice:
        exit(0)

# ____________________ The Game ____________________


start()
