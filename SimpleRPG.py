
currentRoom = "Gang"
RoomDesign = {"Gang": "Du befinder dig i en lang, mørk gang. For enden af den gang er der en dør.",
              "RumA": """Du skubber langsomt den tunge træ dør op og går ind i et svagt oplyst rum.
               Du har svært ved at se noget som helst, men du kan fornemme at det er et meget stort rum.
                Da dine øjne først har vendt sig til mørket ser du at der er andre levende væsener i rummet end dig. 
                DET ER EN DRAGE!!!!! Og døren bag dig er låst!"""}
RoomOptions = {"Gang": "Vil du gå ind ad døren, og starte dit vilde liv som eventyrer (Tast 1) eller vil du blive stående - som en kylling(Tast 2)",
               "RumA": """Døren bag dig er låst, så der er kun en vej - og det er fremad! Du kan enten anrgibe dragen (Tast 1) 
               eller prøve på at løbe forbi dragen, og håbe på at der er en dør for enden af rummet(Tast 2)"""}
while True:
    #print("Du befinder dig i en lang, mørk gang. For enden af den gang er der en dør.")
    print(RoomDesign[currentRoom])
    print(RoomOptions[currentRoom])
    svar = input(">>")

    if currentRoom == "Gang":
        if svar == "1":
            #Evaluering af input
            print("Du er sej!")
            currentRoom="RumA"
        elif svar == "2":
            #Evaluering af input
            print("Du er en kylling!")
        else:
            print("Pardon mig?")
    elif currentRoom == "RumA":
        if svar == "1":
            #Evaluering af input
            print("Du er sej og slår dragen ihjel! Du går ud på gangen igen.")
            currentRoom="Gang"
        elif svar == "2":
            #Evaluering af input
            print("Du er en kylling og dragen spiser dig! GAME OVER!")
        else:
            print("Pardon mig?")
