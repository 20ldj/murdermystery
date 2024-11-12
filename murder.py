clues = []

suspects = ("Bob Von baron", "Sgt Peter", "Dr Andrew", "Profeser Litwick")

bob = input("you wake up to sirens and you look at your clock it is 3 AM   type (A)\n if you want to look out the window   type (B)\n if you want to get dressed  type (C)\n if you want to knock on your neighbors doors and ask them what happend: ")


while True:
    if bob == "A":
        open = input("Do you want to open the window(Y or N):")
        if open == "Y":
            print("you hear the screams of people a blast of sirens and the yelling of law inforcement\n and police cars and baricades around whats seems to be a dead person")
            scream = input("do you want to go down stairs(Y or N)")
            if open == "Y":
                print("As you through on your cloths and your coat and slip on your badge you rush out the door as you head down stairs you bump in to a cloaked figure")
                cloak = input("if you want to yell a swear word at the person type 1 if you want to continue without caussing a problem type 2:")
                if cloak == "1":
                    print("the figure turns around and in a flash you see him throw somthing at you and then you feel a slow trikle of blood coming from your forhead\n womp womp you died ")
                    break
                if cloak == "2":
                    print("as you rush down the stair you see a news repoter van and police officers enforcing the baricade")
                    police = input("do you want to push your way to the front(Y or N)")
                    if police == "Y":
                        print("as you push your way to the front a police officer opens the baricad for you he say ditective we have a homicied come to the sation with us")
                        death = input("do you want to go the police station with the cops(Y or N)")
                        if death =="N":
                            print("you go back up stairs and got to sleep in your bed")
                        if death =="Y":
                            print("as you get in the police car you see the body get loaded in to a abulace once you arive at the police station the police chief tells you that the victum was stabed and in the morning you and a squad of cop will go with you to the morgue")





        if open == "N":
            print("you see the flashs of police sirens")
            flash = input("if you want to go to sleep type 1 if you want to go on your conputer type 2:")
            if flash == "1":
                print("you fall asleep")
            if flash == "2":
                flash = input("if you want to check your email type 1 if you want to open up roblox and start playing roblox type 2:")
                if flash == "1":
                    print("you have no mail")
                if flash == "2":
                    print ("you start gaming TDS on roblox you get so sucked in to the game you never leave")
                    break

    elif open == "B":
        print("as you slip your shirt on you hear some comotion in the hallway as you look through the peep hole you see a cloaked figure sprint down the hall holding a knife and then you see some thing a gold tie with a dimond padern on it")

        figure = input("do you want to open the door(Y or N)")
        if figure == "Y":
            print("you see the figure run up the fire exit")
        if figure == "N":
            ("you over hear from your radio that Sgt peter is looking for the detective then you hear\ndetective are you there detective?")
            radio = input("if you want to reson on the radio type (1)\nif you want to chase after the cloaked figure type(2)")
            fire = input("do you want to chase after them(Y or N)")
            if fire == "N":
                print("why not...")
            if fire == "Y":
                print("as you chase after the figure you see that the person chase you throws a knife at you...ask bennett to roll a dice for you any thing but 19 and you die")

    elif bob == "C":
        bob = input("which neighbors door do you want to knock on Type 1 for the first door type 2 for the second door Type 3 for the third door")
        if bob == "1":
            print("no one respons...")
        if bob == "2":
            print("no one respons...")
        if bob == "3":
            print("a man opens the door and shoots you with a shot gun")
    if bob == "BENNETT":
        print("sudenly your room fades away and you see a door way and as you enter a room with a window and see your room with you geting out of bed....:)  ")
        break