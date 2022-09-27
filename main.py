print("The static at my door...")

looked_around = False
smelled = False
walking = False

print(
    "You wake up in your bed and realize that you cannot move, what do you do? "
)
print("1. Look around")
print("2. Try to sit up")
print("3. What is that noise?")

choice = input("> ")

if choice == "1":
    print("You can see that your tv is left into static.")
    print("You look at the door. you could've sworn that you locked the door.")
    looked_around = True
elif choice == "2":
    print("You try to sit up... but it failed...")
    print(
        "You keep trying and then pass out from failure... it got you while you was asleep..."
    )

#I've already discussed this with Isaac. He would be a good person to talk to.
    quit()
else:
    print("Apparently, it's coming from the door...")
    print(
        "The door that you locked before you fell asleep, turned out to be opened!"
    )
    smelled = True

input("Press Enter to continue...")

print(
    "A static shape hand grabs the door frame and a static head was shown, it seems to be staring at you, what do you do? "
)
if not looked_around:
    print("1. stare at it")
else:
    print("1. taunt it")
print("2. try to get up and find the bible")
if not smelled:
    print("3. Try to scream")

choice = input("> ")

if choice == "1" and not looked_around:
    print("You stare at it...")
    print("Why am i staring at it, you ask yourself.  is it getting closer?")
    looked_around = True
elif choice == "1" and looked_around:
    walking = True
elif choice == "2":
    print(
        "You try to get up and grab your bible on your nightstand, but you was still stuck there..."
    )
    print(
        "You just exhaust yourself and fall to sleep, not knowing that it got you!"
    )

    quit()
elif choice == "3" and not smelled:
    print("Apparently, you can't scream, or talk...")
    print("You ask yourself, is it getting closer?")
    smelled = True

if not walking:
    input("Press Enter to continue...")

    print("You're in the bed with something at your door, what do you do? ")
    print("1. taunt it")
    print("2. stare at it again")

    choice = input("> ")

    if choice == "1":
        walking = True
    elif choice == "2":
        print("You stare at it again...")
        print(
            "You finally blink and there it is, standing in front of your face. Then everything turns black. You hear a voice."
        )
        print("***: Gotcha")
        print("It got you...")

        quit()

print(
    "You try to taunt it because your a very brave person, but, YOU CAN'T MOVE! When you look back at the door, the static humanoid thin stands in the door way. What do you do? "
)
print("1. wait and stare at it again")
print("2. look away and pray that it disappears")
direction = input("> ")

if direction == "1":
    print("You stare at him, then silence filled the room...")
    print("The thing run towards you...")
    print("Loud static noises filled your ears...")
    input("Press Enter to continue...")
    print(
        "Before it reached your bed, you noticed that you could move your arms again..."
    )
    print("You grab the blankets, out of habit, and cover your face...")
    input("Press Enter to continue...")
    print("After you uncovered your face, it was gone, and the tv was off...")
    print("You ran to the door and shut it, also cutting the lights on...")
    print(
        "You then ran to your bed and grabbed your flashlight from the nightstand..."
    )
    print("You kept guard")
    print("You survived the demon that you called Mr. Static to this day.")
    print("THE GOOD ENDING")

else:
    print(
        "You look towards the wall beside your bed, praying that the thing would go away..."
    )
    print("It did not work...")
    print("You hear the static grew louder and then quiet...")
    print("In your ear, you hear a gentle voice say...")
    print("***: No god can help you now...")
    input("Press Enter to continue...")
    print(
        "You see a static hand reach around you and grab you. All that can see is darkness..."
    )
    print("***: You eternity punishment is about to begin...")
    print("THE BAD ENDING")

print()
print()
print()
print("part two: Mr. Static comes once again - coming in 2666")