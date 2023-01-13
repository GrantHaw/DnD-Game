# author: Grant Hawerlander
# CSC119 Spring 2021
#note: yes i know this isnt efficent. yes i know it's 1000+ lines long. i made this at 2 am and the only thing saving me is my documentation

import time		# used to add wait time during printing
import sys		# used to exit the program
import os		# used to clear the console
from termcolor import colored, cprint 	# print in different colors
import random # randomizer




#defining flags that nitpick and ensure there are no "continuity" glitches. These are events that can only happen once.
#LOOK AROUND COINS- GH
lachflag = 0
#CANDLE BOUGHT
canflag = 0
#LAVA CASTLE COMPLETED
lcflag = 0
#TRAINING GROUNDS COMPLETED
trflag = 0
#BAD SWORD BOUGHT
bsflag = 0
#STRENGTH POT BOUGHT
spflag = 0
#STEEL SWORD BOUGHT
ssflag = 0
#BEAT IN OLENGUARD REGION
oBeat = False
#BEAT IN LESTO REGION
lBeat = False
#LIGHT ARMOR BOUGHT
laflag = 0
#GRAVEYARD COMPLETED
gyflag = 0
#SHOVEL BOUGHT
sflag = 0
#HEAVY ARMOR BOUGHT
haflag = 0
#DELIVERY FINISHED
delivfin = False
#CAN QUEST FINISHED
canq = False
#DELIVERY PACKAGE GIVEN
deliv = False
#BEAT IN TRENSTINIA
tBeat = False
#---/\/\/\BACK END/\/\/\---
#---\/\/\/FRONT END\/\/\/---
#INVENTORY
inven = []
#GOLD
gold = 5
#MODIFIERS
atkmod = 0
defmod = 0
#QUESTS
quests = ["GRAB ALL 3 KEYS AND OPEN THE VAULT"]
#HEALTH
health = 10

# clears the console when called
def clear():
  os.system("clr" if os.name == "nt" else "clear")
  #shows "ui" (just basic info)
  cprint("QUESTS: "+ str(quests),"blue","on_grey")
  cprint("Inventory: " + str(inven),"magenta","on_grey")
  cprint("Health: "+ str(health), "green","on_grey")
  cprint("Gold: " + str(gold), "yellow","on_grey")
  cprint("ATK: " + str(atkmod), "yellow","on_grey")
  cprint("DEF: " + str(defmod), "yellow","on_grey")
  #makes a line to show "game screen"
  cprint(" "*40,"red",attrs=["underline"])
	


#sets up game and instructions
def intro():
  print("Welcome, Traveler. This is a game that will test your strategy, skill and intelligence.")
  time.sleep(1)
  print("Instead of a normal dungeon crawler, this game is set up to be more of a DND game. Instead of different rooms, there will be towns and shops for you to explore.")
  time.sleep(4)
  print("Your goal is to escape via the vault. But first you must find the vault and grab the keys required to open it.")
  time.sleep(5)
  print("You will navigate towns via the Carriage Hub. Passage is free, but you may have to determine which town is which direction first.")
  time.sleep(5)
  print("You have 5 gold to spend as you wish in the towns and shops you discover. Having armor or a weapon before going into battle is STRONGLY RECOMMENDED. These items will provide you with a modifer, which will add to your attack rolls or take away from enemy's hits to do less damage.")
  time.sleep(6)
  input("Press enter to begin the game...")
  clear()

def trestinia():
  clear()
  print("You see a medieval lava town filled with a castle and a few shops. Everything is suspended above a lava lake. You see 4 locations...")
  cprint("where do you go? \n>General Store\n>Lava Castle\n>Talk to the girl\n>The Cave\n>Look Around\n>Return","cyan")
  flag = 0
  while flag == 0:
    #DIRECTORY FUNCTIONS TO SEND PLAYER TO ROOMS
    flag = 1
    wt = input('>')
    if wt.lower() in ["general store","gen","store","general","gs"]:
      generalstore()
    elif wt.lower() in ["castle","lava","lc","lava castle"]:
      lavacastle()
    elif wt.lower() in ["girl","talk to the girl","talk","tg"]:
      kaydelivery()
    elif wt.lower() in ["cave","the cave","c","tc"]:
      cave()
    elif wt.lower() in ["return","go back","carriage hub","r","gb"]:
      grandhub()
    elif wt.lower() in ["l","look","look around"]:
      #ensures prgm doesnt stop
      flag = 0 
      print("You are in a lava town, where almost everyone is descendants of the Magma Family. Nearly everyone is superhuman and made of stones and lava.")
      input("Press enter to continue.\n")
      trestinia()
    else:
      flag = 0
      #checks if you messed up
      cprint("incorrect answer, please input a new answer.","red")
      print("Where next?")

def generalstore():
  #globals to ensure uniformity
  global gold
  global canflag
  global sflag
  print("The general store is very run down, and only offers two sole items, a shovel and a candle.")
  cprint("You see two items for sale:\n>Shovel (2G)\n[Purpose: ???.]\n>Candle (2G)\n[Purpose: ???.]\nWhat do you buy? (Press enter to leave)","cyan")
  ans = input(">")
  #detects if u want a shovel
  if ans.lower() in ["shovel","s"]:
    if sflag == 0:
      if gold >= 2:
        #ensures you cant get a buttload of shovels
        sflag = 1
        #aestetic pieces 
        print("You buy a shovel!")
        cprint("-2 Gold", "red")
        cprint("+1 Shovel", "green")
        #adds to inventory
        inven.append("Shovel")
        cprint("Current inventory: " + str(inven),"magenta")
        gold = gold -2
        cprint("Current Gold: " + str(gold),"yellow")
        input("Press enter to continue.\n")
        #sends back to store
        generalstore()
      else:
        #haha poor check
        cprint("You don't have enough money to buy the shovel.","red")
        cprint("Current Gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        #sends back to store
        generalstore()
    else:
      #yeah you aren't getting more than one shovel buckaroo
      cprint("You already bought the shovel.","red")
      input("Press enter to continue.")
      generalstore()
  #checks for candle
  if ans.lower() in ["candle","c"]:
    #makes sure you havnt bought a candle
    if canflag == 0:
      #makes sure you have gold
      if gold >= 2:
        canflag = 1
        #aestetic
        print("You buy a candle!")
        cprint("-2 Gold", "red")
        cprint("+1 Candle", "green")
        #adds to inventory
        inven.append("Candle")
        cprint("Current inventory: " + str(inven),"magenta")
        #removes gold
        gold = gold -2
        cprint("Current Gold: " + str(gold),"yellow")
        input("Press enter to continue.\n")
        generalstore()
      else:
        #if poor:
        cprint("You don't have enough money to buy the candle.","red")
        cprint("Current Gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        #back to shop
        generalstore()
    else:
      #if you already bought it
      cprint("You already bought the candle.","red")
      input("Press enter to continue.")
      generalstore()
  else:
      cprint("You leave the store.","red")
      input("Press enter to continue. ")
      trestinia()

def lavacastle():
  global gold
  global lcflag
  #sets correct to false
  correct = False
  if lcflag == 0:
    print("You are approached by a lava jester. He has a puzzle for you!!")
    print("Fill in the blanks, all together they will make a sentence. You may enter the answer with spaces or not.")
    print("AHOx Hint: Pirate\nTxOL Hint: Hammer\nxNDO Hint: Go Back\nDOx Hint: Pet\nENTxR Hint: Go in\nxALK Hint: Speak\n5,6,7,8,9,x,11,12 Hint: Counting\nxAME Hint: Playing one right now\nxLD Hint: My Grandma and Grandpa\nGOAx Hint: Yours is to win the game\nFRIENx Hint: You have some of these! (hopefully)")
    while correct == False:
      scribe= input("Answer:\n")
      #checks for answer (i put debug in bc im lazy)
      if scribe.lower() in ["youget10gold", "you get 10 gold","debug"]:
        #quit looking at the answer!
        correct = True
        lcflag = 1
        print("Congragulations! You get 10 gold!!")
        cprint("+10 Gold","green")
        #updates gold
        gold = gold+10
        cprint("Current Gold: " + str(gold), "yellow")
        input("Press enter to continue.")
        trestinia()
      else:
        #wrong
        cprint("Incorrect. Remember, the 'x' tells you what you need to fill in.","red")
  else:
    #cant do it twice
    print("you completed this puzzle. you return to town square.")
    input("Press enter to continue.")
    trestinia()


def kaydelivery():
  global deliv
  global quests
  #checks if deliv has been made
  if deliv == False:
    deliv = True
    print("You walk up to the girl. She says to you: 'Can you please deliver this to my friend Dakota in Etzor? I'm too busy right now to get it. She's a shopkeeper there and she needs this package. Thank you! I'll make it worth your while.'")
    cprint("+ Package", "green")
    #you get the package
    inven.append("Package")
    cprint("Current Inventory: " + str(inven) , "magenta")
    #sees if it's a repeat
    if "DELIVER PACKAGE TO DAKOTA IN ETZOR" not in quests:
      quests.append("DELIVER PACKAGE TO DAKOTA IN ETZOR")
      cprint("NEW QUEST: DELIVER PACKAGE TO DAKOTA IN ETZOR", "blue")
    else:
      #if you know dakota you alr have the quest, this is just a hint
      cprint("Hmm, maybe this package goes with somebody you've already met...","green")
    input("Press enter to continue.")
    trestinia()
  else:
    #if you already got the package then she wont give you another
    cprint("You already recieved this package.", "red")
    input("Press enter to continue. ")
    trestinia()


def cave():
  #globals to ensure uniformity
  global health
  global tBeat
  global inven
  #checks if monster is alive
  if tBeat == False:
    print("You approach the cave. Inside you hear a deep growling sound.")
    #one last chance to save yourself
    cprint("Do you go in?", "red", attrs=["bold","underline"])
    if input(">").lower() in ["y","yes",'yep','ye']:
      #oh girl good luck
      clear()
      cprint("You find a lava monster!!! Entering combat....", "grey")
      input("Press enter to continue.")
      #health setup
      mHealth = 20
      alive = True
      quests.append("KILL THE LAVA MONSTER")
      while alive == True:
        #COMBAT CYCLE BEGINS--------------------------
        clear()
        #clearing dodge mod
        dMod = 0
        cprint("What do you do?\n>Hit (highest weapon tier will be auto-added)\n>Dodge (Negate Next Hit's Damage)\n>Recover (Recover Health)", "cyan")
        #checking for heal pot (you're gonna need it)
        if "Heal Potion" in inven:
          cprint(">Use Healing Potion","cyan")
        act = input(">")
        #IF HIT ACTION
        if act.lower() in ["sword","hit","punch","attack","h"]:
          #determining hit+ atkmod added by weapons
          hit = (random.randint(1,5) + atkmod)
          #monster takin the hit
          mHealth = mHealth - hit
          cprint("You hit it! You did " + str(hit) + " damage (" + str(atkmod)+" added through modifiers).", "green")
          #check if you #slayed
          if mHealth <= 0:
            tBeat = True
            cprint("You killed the monster!!","green")
            cprint("You find the LAVA KEY and return to town.", "green", attrs = ["bold"])
            #woo u got the key
            inven.append("LAVA KEY")
            cprint("Current Inventory: " + str(inven),"magenta")
            input("Press enter to continue.")
            quests.remove("KILL THE LAVA MONSTER")
            #returns to town
            trestinia()
        #IF DODGE ACTION
        elif act.lower() in ["dodge","d"]:
          #determining dodge mod
          dMod = random.randint(1,5)
          cprint("You dodge the next attack. You negate " + str(dMod) +" off the next hit!","green")
        #IF RECO ACTION
        elif act.lower() in ["reco", "recover", "r"]:
          #determining reco
          heal = random.randint(1,4)
          health = health+heal
          cprint("You recover for "+ str(heal)+" health!","green")
          cprint("Current Health: "+ str(health),"grey")
        #IF HEAL (must have one in inventory)
        elif act.lower() in ["use healing potion", "heal","use potion","hp"] and "Heal Potion" in inven:
          cprint("You use a healing potion and heal 8 health!", "green")
          cprint("-1 Healing Potion","red")
          health =+8
          inven.remove("Heal Potion")
          cprint("Current Inventory: " + str(inven),"magenta")
        else:
          #if you mess up even though i give you so many chances you can die idc
          cprint("action not recognized. skipping turn!!", "red")
        cprint("The monster swings at you...","red")
        dam = random.randint(1,defmod+7)
        #determining damage-modifiers
        dam = dam - (dMod+defmod)
        cprint("You negated " + str((dMod+defmod)) +" damage!", "green")
        if dam <= 0:
          cprint("The monster misses you! (0 or less damage)", "green")
        else:
          cprint("You get hit for "+ str(dam)+" damage!","red")
        #you aint gettin more health buckaroo
        if dam >0:
          health = health-dam
        print("Monster Health: "+str(mHealth))
        #dead check!
        if health <= 0:
          cprint("YOU HAVE DIED.","red")
          #this is so true
          print("Tip! ALWAYS GO INTO COMBAT WITH A GOOD SWORD OR ARMOR OR A POTION. YOU CAN'T DO IT ALONE.")
          quit()
        cprint("Current Health: "+ str(health), "grey")
        input("Press enter to continue.")
    else:
      print("You return to town square.")
      input("Press enter to continue.")
      trestinia()

  else:
    cprint("You already defeated this monster. You return to town square.","red")
    input("Press enter to continue.")
    trestinia()
#END TRESTINIA FUNCTIONS________________________________________________

#START LESTO FUNCTIONS____________________________________________________
def lesto():
  clear()
  print("As you get off the carriage you are greeted with the fresh town of lesto. Lesto is a forest city, with everything being in treetops and made out of wood. Here, you see 4 locations...")
  cprint("where do you go? \n>Training Grounds\n>Apothecary\n>Pet Shop\n>The Forest\n>Look Around\n>Return","cyan")
  flag = 0
  while flag == 0:
    flag = 1
    wt = input('>')
    #sends player to rooms
    if wt.lower() in ["training grounds","tg","t","training","train"]:
      trainingGrounds()
    elif wt.lower() in ["apothecary","a","apo"]:
      apothecary()
    elif wt.lower() in ["pet shop","p","ps","pets"]:
      petshop()
    elif wt.lower() in ["forest","the forest","f","tf"]:
      forest()
    elif wt.lower() in ["return","go back","carriage hub","r","gb"]:
      grandhub()
    elif wt.lower() in ["l","look","look around"]:
      flag = 0 
      print("You are in a forest town, where many of the people idolize nature and treat it as another human. You don't see much else.")
      input("Press enter to continue.\n")
      lesto()
    else:
      flag = 0
      cprint("incorrect answer, please input a new answer.","red")
      print("Where next?")

def trainingGrounds():
  #sets up quiz variable
  correct = False
  global atkmod
  global defmod
  global trflag
  flag = 0
  #makes sure you aren't just grinding training
  if trflag == 0:
    print("You are greeted with a training area with two dummies, one that sets up attacks against you and one that can take hits against it.")
    cprint("What do you level up?\n>Defense\n>Attack","cyan")
    while flag == 0:
      ans = input('>')
      #checks which one you wanna level up 
      if ans.lower() in ["defense","def","d"]:
        print("In order to level up defense, solve this math equation.")
        print("(4*8-2)^2")
        while correct == False:
          answer= input("Answer:\n")
          #i see you looking for the answer...
          if answer == "900":
            #changes states
            correct = True
            trflag = 1
            print("Congragulations! You permanently leveled up your defense modifier by 1!!")
            cprint("+1 DEF","green")
            #ups modifier
            defmod = defmod + 1
            cprint("Current Def: " + str(defmod), "yellow")
            input("Press enter to continue.")
            #back to town
            lesto()
          else:
            #incorrect
            cprint("Incorrect. Remember, pemdas!","red")
      #checks if you want attack
      elif ans.lower() in ["attack", "atk", "a"]:
        print("In order to level up attack, solve this math equation.")
        print("(4*8-2)^2")
        while correct == False:
          answer= input("Answer:\n")
          if answer == "900":
            correct = True
            #flag to make sure you dont cheat
            trflag = 1
            print("Congragulations! You permanently leveled up your attack modifier by 1!!")
            cprint("+1 ATK","green")
            atkmod = atkmod+1
            cprint("Current Atk: " + str(atkmod), "yellow")
            input("Press enter to continue.")
            lesto()
          else:
            cprint("Incorrect. Remember, pemdas!","red")
      else:
        #try again, idk what you said
        cprint("Entry not recognized.","red")
        cprint("What do you level up?","cyan")
  else:
    #only once
    cprint("You already leveled something up here.","red")
    print("You return to town square.")
    input("Press enter to continue. ")
    lesto()
          
      
      


def apothecary():
  global gold
  global atkmod
  global spflag
  print("You walk into the apothecary. They only have one sole item, sitting on a desk. It's a red potion.")
  #makes sure you don't get 2
  if spflag == 0:
    print("You see one item for sale:\n>Strength Potion (5G)\n[Purpose: Permanently Adds +2 to ATK modifier upon purchase. Used immediately.]\nBuy it? (Any input not similar to 'yes' will qualify as a no.)")
    #checks if you want it
    if input(">").lower() in ["yes","y",'ye','yep']:
      if gold >= 5:
        spflag = 1
        print("You buy it!")
        cprint("-5 Gold", "red")
        cprint("+1 ATK", "green")
        #updates gold
        gold = gold -5
        atkmod = atkmod+1
        cprint("current gold: " + str(gold),"yellow")
        input("Press enter to continue.\n")
        lesto()
      else:
        #if poor:
        cprint("You don't have enough money to buy the potion.","red")
        print("You return to town square")
        input("Press enter to continue.")
        lesto()
    else:
      #if no:
      print("you decide not to buy it and return to town square.")
      input("Press enter to continue.\n")
      lesto()
  else:
    #if bought:
    print("The store is sold out. You return to town square.")
    input("Press enter to continue.\n")
    lesto()
def petshop():
  global gold
  global inven
  global defmod
  global atkmod
  print("The pet shop offers many dogs and cats, enough to build an army.")
  cprint("You see two items for sale:\n>Dog (6G)\n[Purpose: Defends you for 1 damage.]\n>Cat (5G)\n[Purpose: Attacks with you for 1 damage.]\nWhat do you buy? (Press enter to leave)","cyan")
  ans = input(">")
  #if dog
  if ans.lower() in ["dog","d"]:
    if gold >= 6:
      print("You buy a dog!")
      cprint("-5 Gold", "red")
      cprint("+1 Dog", "green")
      #+ Dog in inventory
      inven.append("Dog")
      cprint("Current inventory: " + str(inven),"magenta")
      #- gold
      gold = gold -6
      #+ def
      defmod= defmod+1
      cprint("current Gold: " + str(gold),"yellow")
      cprint("Current Def: " + str(defmod),"yellow")
      input("Press enter to continue.\n")
      petshop()
    else:
      #if poor:
      cprint("You don't have enough money to buy the dog.","red")
      cprint("current Gold: " + str(gold),"yellow")
      input("Press enter to continue.")
      petshop()
  if ans.lower() in ["cat","c"]:
    if gold >= 5:
      print("You buy a cat!")
      cprint("-3 Gold", "red")
      cprint("+1 Cat", "green")
      #+ cat
      inven.append("Cat")
      cprint("Current inventory: " + str(inven),"magenta")
      #updating gold
      gold = gold -5
      atkmod= atkmod+2
      cprint("current Gold: " + str(gold),"yellow")
      cprint("current Atk: " + str(atkmod),"yellow")
      input("Press enter to continue.\n")
      petshop()
    else:
      cprint("You don't have enough money to buy the cat.","red")
      cprint("current Gold: " + str(gold),"yellow")
      input("Press enter to continue.")
      petshop()
  else:
      cprint("You leave the store.","red")
      input("Press enter to continue. ")
      lesto()

def forest():
    #globals to ensure uniformity
  global health
  global lBeat
  global inven
  #checks if monster is alive
  if lBeat == False:
    print("You approach the forest. Inside you hear a guttoral shriek.")
    #one last chance to save yourself
    cprint("Do you go in?", "red", attrs=["bold","underline"])
    if input(">").lower() in ["y","yes",'yep','ye']:
      #oh girl good luck
      clear()
      cprint("You find a large forest monster!!! Entering combat....", "grey")
      input("Press enter to continue.")
      #health setup
      mHealth = 20
      alive = True
      quests.append("KILL THE LAVA MONSTER")
      while alive == True:
        #COMBAT CYCLE BEGINS--------------------------
        clear()
        #clearing dodge mod
        dMod = 0
        cprint("What do you do?\n>Hit (highest weapon tier will be auto-added)\n>Dodge (Negate Next Hit's Damage)\n>Recover (Recover Health)", "cyan")
        #checking for heal pot (you're gonna need it)
        if "Heal Potion" in inven:
          cprint(">Use Healing Potion","cyan")
        act = input(">")
        #IF HIT ACTION
        if act.lower() in ["sword","hit","punch","attack","h"]:
          #determining hit+ atkmod added by weapons
          hit = (random.randint(1,5) + atkmod)
          #monster takin the hit
          mHealth = mHealth - hit
          cprint("You hit it! You did " + str(hit) + " damage (" + str(atkmod)+" added through modifiers).", "green")
          #check if you #slayed
          if mHealth <= 0:
            lBeat = True
            cprint("You killed the monster!!","green")
            cprint("You find the FOREST KEY and return to town.", "green", attrs = ["bold"])
            #woo u got the key
            inven.append("FOREST KEY")
            quests.remove("KILL THE FOREST MONSTER")
            cprint("Current Inventory: " + str(inven),"magenta")
            input("Press enter to continue.")
            #returns to town
            lesto()
        #IF DODGE ACTION
        elif act.lower() in ["dodge","d"]:
          #determining dodge mod
          dMod = random.randint(1,5)
          cprint("You dodge the next attack. You negate " + str(dMod) +" off the next hit!","green")
        #IF RECO ACTION
        elif act.lower() in ["reco", "recover", "r"]:
          #determining reco
          heal = random.randint(1,4)
          health = health+heal
          cprint("You recover for "+ str(heal)+" health!","green")
          cprint("Current Health: "+ str(health),"grey")
        #IF HEAL (must have one in inventory)
        elif act.lower() in ["use healing potion", "heal","use potion","hp"] and "Heal Potion" in inven:
          cprint("You use a healing potion and heal 8 health!", "green")
          cprint("-1 Healing Potion","red")
          health =+8
          inven.remove("Heal Potion")
          cprint("Current Inventory: " + str(inven),"magenta")
        else:
          #if you mess up even though i give you so many chances you can die idc
          cprint("action not recognized. skipping turn!!", "red")
        cprint("The monster swings at you...","red")
        dam = random.randint(1,defmod+7)
        #determining damage-modifiers
        dam = dam - (dMod+defmod)
        cprint("You negated " + str((dMod+defmod)) +" damage!", "green")
        if dam <= 0:
          cprint("The monster misses you! (0 or less damage)", "green")
        else:
          cprint("You get hit for "+ str(dam)+" damage!","red")
        #you aint gettin more health buckaroo
        if dam >0:
          health = health-dam
        print("Monster Health: "+str(mHealth))
        #dead check!
        if health <= 0:
          cprint("YOU HAVE DIED.","red")
          print("Tip! ALWAYS GO INTO COMBAT WITH A GOOD SWORD OR ARMOR OR A POTION. YOU CAN'T DO IT ALONE.")
          quit()
        cprint("Current Health: "+ str(health), "grey")
        input("Press enter to continue.")
    else:
      print("You return to town square.")
      input("Press enter to continue.")
      lesto()

  else:
    cprint("You already defeated this monster. You return to town square.","red")
    input("Press enter to continue.")
    lesto()
#END LESTO FUNCTIONS________________________________________________

#START OLENGUARD FUNCTIONS____________________________________________________




def olenguard():
  clear()
  print("You arrive at Olenguard. Olenguard is an industrial city, where factories and buildings are everywhere. There is only one boy to be seen. You see four locations...")
  cprint("where do you go? \n>Blacksmith\n>Witch Doctor\n>Talk to the boy\n>The Complex\n>Look Around\n>Return","cyan")
  flag = 0
  while flag == 0:
    flag = 1
    wt = input('>')
    #directs the player
    if wt.lower() in ["blacksmith","bs","s","smith"]:
      blacksmith()
    elif wt.lower() in ["witch doctor","doc","wd","d"]:
      witchdoc()
    elif wt.lower() in ["boy","b","talk to the boy","talk"]:
      brandongrab()
    elif wt.lower() in ["complex","the complex","c","tc"]:
      complex()
    elif wt.lower() in ["return","go back","carriage hub","r","gb"]:
      grandhub()
    elif wt.lower() in ["l","look","look around"]:
      flag = 0 
      print("You are in an industrial town, where almost everyone seems to be working.")
      input("Press enter to continue.\n")
      olenguard()
    else:
      flag = 0
      cprint("incorrect answer, please input a new answer.","red")
      print("Where next?")

def blacksmith():
  global gold
  global inven
  global atkmod
  global bsflag
  global ssflag
  print("The blacksmith offers two swords to help you in your fights.")
  cprint("You see two items for sale:\n>Bad Sword (4G)\n[Purpose: Boosts ATK by 1.]\n>Steel Sword (10G)\n[Purpose: Boosts ATK by 3.]\nWhat do you buy? (Press enter to leave)","cyan")
  ans = input(">")
  #if bad sword:
  if ans.lower() in ["bad","b", "bad sword","bs"]:
    if bsflag == 0:
      #poor check
      if gold >= 4:
        print("You buy a bad sword!")
        #updates flag
        bsflag = 1
        cprint("-4 Gold", "red")
        cprint("+1 Bad Sword", "green")
        #adds to inventory
        inven.append("Bad Sword")
        cprint("Current inventory: " + str(inven),"magenta")
        #removes gold + adds attack
        gold = gold -4
        atkmod = atkmod + 1
        cprint("Current Gold: " + str(gold),"yellow")
        cprint("Current ATK: " + str(atkmod),"yellow")
        input("Press enter to continue.\n")
        blacksmith()
      else:
        #if poor:
        cprint("You don't have enough money to buy the sword.","red")
        cprint("current Gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        blacksmith()
    else:
      #if bought:
      cprint("You already bought the bad sword!","red")
      input("Press enter to continue.")
      blacksmith()
  if ans.lower() in ["steel","s", "steel sword","ss"]:
    if ssflag == 0:
      if gold >= 10:
        print("You buy a Steel Sword!")
        #updates flag
        ssflag = 1
        cprint("-10 Gold", "red")
        cprint("+1 Steel Sword", "green")
        #adds to inven
        inven.append("Steel Sword")
        cprint("Current inventory: " + str(inven),"magenta")
        #updates stats
        gold = gold -10
        atkmod = atkmod + 3
        cprint("Current Gold: " + str(gold),"yellow")
        cprint("Current ATK: " + str(atkmod),"yellow")
        input("Press enter to continue.\n")
        blacksmith()
      else:
        #if poor:
        cprint("You don't have enough money to buy the sword.","red")
        cprint("current Gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        blacksmith()
    else:
      #if bought:
      cprint("You already bought the steel sword!","red")
      input("Press enter to continue.")
      blacksmith()
  else:
    #if not recognized or not entered
    cprint("You leave the store.","red")
    input("Press enter to continue. ")
    olenguard()

def witchdoc():
  global gold
  print("You walk into the witch doc and you see health potions galore. Almost an endless supply.")
  print("You see one item for sale:\n>Health Potion (5G)\n[Purpose: Heals you for +8 hp. Used in combat.]\nBuy it? (Press enter to leave.)")
  if input(">").lower() in ["yes","y",'ye','yep']:
    if gold >= 5:
        print("You buy it!")
        cprint("-5 Gold", "red")
        cprint("+1 Health Potion!", "green")
      #updates gold
        gold = gold -5
        inven.append("Health Potion")
        cprint("Current inventory: " + str(inven),"magenta")
        cprint("current gold: " + str(gold),"yellow")
        input("Press enter to continue.\n")
        witchdoc()
    else:
      #if poor:
        cprint("You don't have enough money to buy the potion.","red")
        cprint("current gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        witchdoc()
  else:
    #non-response
      cprint("you exit the store.","red")
      input("Press enter to continue.\n")
      olenguard()
def brandongrab():
  global gold
  global inven
  global canq
  #if not completed
  if canq == False:
    print("You go up to the boy. He says: 'I need a candle for my next caving trip!'")
    if "Candle" in inven:
      print('"Thank you for getting me a candle!! Please take this as my gratitude!" He takes the candle from your hands and puts a pack of gold in its place.')
      #marks as done
      canq = True
      cprint("-1 Candle", "red")
      cprint("+10 Gold", "green")
      #adds gold
      gold = gold +10
      #removes stuff
      inven.remove("Candle")
      if "GET THE BOY A CANDLE" in quests:
        quests.remove("GET THE BOY A CANDLE")
      cprint("Current inventory: " + str(inven),"magenta")
      cprint("Current Gold: " + str(gold),"yellow")
      input("Press enter to continue.\n")
      olenguard()
    else:
      print("Can you please get me a candle? I'll make it worth your while!!")
      cprint("NEW QUEST: GET THE BOY A CANDLE", "blue")
      #adds to quests
      quests.append("GET THE BOY A CANDLE")
      input("Press enter to continue.\n")
      olenguard()
  else:
    #if already completed
    print(' The boy says: "Thank you for getting me a candle!!"')
    input("Press enter to continue.\n")
    olenguard()
def complex():
  #globals to ensure uniformity
  global health
  global oBeat
  global inven
  #checks if monster is alive
  if oBeat == False:
    print("You approach the industrial complex. Inside, you hear a piercing whistle sound.")
    #one last chance to save yourself
    cprint("Do you go in?", "red", attrs=["bold","underline"])
    if input(">").lower() in ["y","yes",'yep','ye']:
      #oh girl good luck
      clear()
      cprint("You find a steam monster!!! Entering combat....", "grey")
      input("Press enter to continue.")
      #health setup
      mHealth = 20
      alive = True
      quests.append("KILL THE STEEL MONSTER")
      while alive == True:
        #COMBAT CYCLE BEGINS--------------------------
        clear()
        #clearing dodge mod
        dMod = 0
        cprint("What do you do?\n>Hit (highest weapon tier will be auto-added)\n>Dodge (Negate Next Hit's Damage)\n>Recover (Recover Health)", "cyan")
        #checking for heal pot (you're gonna need it)
        if "Heal Potion" in inven:
          cprint(">Use Healing Potion","cyan")
        act = input(">")
        #IF HIT ACTION
        if act.lower() in ["sword","hit","punch","attack","h"]:
          #determining hit+ atkmod added by weapons
          hit = (random.randint(1,5) + atkmod)
          #monster takin the hit
          mHealth = mHealth - hit
          cprint("You hit it! You did " + str(hit) + " damage (" + str(atkmod)+" added through modifiers).", "green")
          #check if you #slayed
          if mHealth <= 0:
            oBeat = True
            cprint("You killed the monster!!","green")
            cprint("You find the STEEL KEY and return to town.", "green", attrs = ["bold"])
            #woo u got the key
            inven.append("STEEL KEY")
            quests.remove("KILL THE STEEL MONSTER")
            cprint("Current Inventory: " + str(inven),"magenta")
            input("Press enter to continue.")
            #returns to town
            olenguard()
        #IF DODGE ACTION
        elif act.lower() in ["dodge","d"]:
          #determining dodge mod
          dMod = random.randint(1,5)
          cprint("You dodge the next attack. You negate " + str(dMod) +" off the next hit!","green")
        #IF RECO ACTION
        elif act.lower() in ["reco", "recover", "r"]:
          #determining reco
          heal = random.randint(1,4)
          health = health+heal
          cprint("You recover for "+ str(heal)+" health!","green")
          cprint("Current Health: "+ str(health),"grey")
        #IF HEAL (must have one in inventory)
        elif act.lower() in ["use healing potion", "heal","use potion","hp"] and "Heal Potion" in inven:
          cprint("You use a healing potion and heal 8 health!", "green")
          cprint("-1 Healing Potion","red")
          health =+8
          inven.remove("Heal Potion")
          cprint("Current Inventory: " + str(inven),"magenta")
        else:
          #if you mess up even though i give you so many chances you can die idc
          cprint("action not recognized. skipping turn!!", "red")
        cprint("The monster swings at you...","red")
        dam = random.randint(1,defmod+7)
        #determining damage-modifiers
        dam = dam - (dMod+defmod)
        cprint("You negated " + str((dMod+defmod)) +" damage!", "green")
        if dam <= 0:
          cprint("The monster misses you! (0 or less damage)", "green")
        else:
          cprint("You get hit for "+ str(dam)+" damage!","red")
        #you aint gettin more health buckaroo
        if dam >0:
          health = health-dam
        print("Monster Health: "+str(mHealth))
        #dead check!
        if health <= 0:
          cprint("YOU HAVE DIED.","red")
          print("Tip! ALWAYS GO INTO COMBAT WITH A GOOD SWORD OR ARMOR OR A POTION. YOU CAN'T DO IT ALONE.")
          quit()
        cprint("Current Health: "+ str(health), "grey")
        input("Press enter to continue.")
    else:
      print("You return to town square.")
      input("Press enter to continue.")
      olenguard()

  else:
    #you aint gettin 2 keys
    cprint("You already defeated this monster. You return to town square.","red")
    input("Press enter to continue.")
    olenguard()

def etzor():
  clear()
  #starts etzor paths
  print("You arrive at Etzor. You step off your carriage to find a cold and snowy region. You also see 4 locations...")
  cprint("where do you go? \n>Leather Worker\n>Talk to the shopwoman\n>Graveyard\n>The Vault\n>Look Around\n>Return","cyan")
  flag = 0
  while flag == 0:
    flag = 1
    wt = input('>')
    #sends player to locations
    if wt.lower() in ["leather worker","lw","l","worker","w"]:
      leatherworker()
    elif wt.lower() in ["talk to the shopwoman","shopwoman","sw","s","ts"]:
      dakotadelivery()
    elif wt.lower() in ["graveyard","g","grave","gy"]:
      graveyard()
    elif wt.lower() in ["vault","the vault","v","tv"]:
      vault()
    elif wt.lower() in ["return","go back","carriage hub","r","gb"]:
      grandhub()
    elif wt.lower() in ["l","look","look around"]:
      flag = 0 
      print("You are in a winter based town, where many of the people are bundled up in jackets ready for snow.")
      input("Press enter to continue.\n")
      lesto()
    else:
      flag = 0
      #lets player enter again
      cprint("incorrect answer, please input a new answer.","red")
      print("Where next?")


def leatherworker():
  #globals for uniformity
  global gold
  global inven
  global defmod
  global laflag
  global haflag
  print("The blacksmith offers two swords to help you in your fights.")
  cprint("You see two items for sale:\n>Light Armor (4G)\n[Purpose: Boosts DEF by 1.]\n> Heavy Armor (10G)\n[Purpose: Boosts DEF by 3.]\nWhat do you buy? (Press enter to leave)","cyan")
  ans = input(">")
  #checks for light armor
  if ans.lower() in ["light","l", "light armor","la"]:
    if laflag == 0:
      #checks to see you're not poor
      if gold >= 4:
        print("You buy Light Armor!")
        laflag = 1
        #aestetic
        cprint("-4 Gold", "red")
        cprint("+1 Light Armor", "green")
        #adds to iventory
        inven.append("Light Armor")
        cprint("Current inventory: " + str(inven),"magenta")
        #updates gold
        gold = gold -4
        defmod = defmod + 1
        #aestetic 2: electric boogaloo
        cprint("Current Gold: " + str(gold),"yellow")
        cprint("Current DEF: " + str(defmod),"yellow")
        input("Press enter to continue.\n")
        #back to shop
        leatherworker()
      else:
        #poor
        cprint("You don't have enough money to buy the armor.","red")
        #shows u gold
        cprint("Current Gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        #back to shop
        leatherworker()
    else:
      #if bought:
      cprint("You already bought the light armor!","red")
      input("Press enter to continue.")
      leatherworker()
  if ans.lower() in ["heavy","h", "heavy armor","ha"]:
    if haflag == 0:
      if gold >= 10:
        print("You buy Heavy Armor!")
        #cant buy again flag
        haflag = 1
        cprint("-10 Gold", "red")
        cprint("+1 Heavy Armor", "green")
        inven.append("Heavy Armor")
        cprint("Current inventory: " + str(inven),"magenta")
        #updates stats
        gold = gold -10
        defmod = defmod + 3
        cprint("Current Gold: " + str(gold),"yellow")
        cprint("Current DEF: " + str(defmod),"yellow")
        input("Press enter to continue.\n")
        leatherworker()
      else:
        #if poor:
        cprint("You don't have enough money to buy the armor.","red")
        cprint("Current Gold: " + str(gold),"yellow")
        input("Press enter to continue.")
        leatherworker()
    else:
      #if bought:
      cprint("You already bought the heavy armor!","red")
      input("Press enter to continue.")
      leatherworker()
  else:
    #if non-responsive:
    cprint("You leave the store.","red")
    input("Press enter to continue. ")
    etzor()
def dakotadelivery():
  global gold
  global inven
  global delivfin
  if delivfin == False:
    print("She seems to be looking for something... As you get closer you can hear her muttering about a package.")
    if "Package" in inven:
      print('"Thank you for getting me my package!! Me and Kay are so thankful!" She takes it from your hands and puts a pack of gold in its place.')
      quests.remove("DELIVER PACKAGE TO DAKOTA IN ETZOR")
      delivfin = True
      cprint("-1 Package", "red")
      cprint("+10 Gold", "green")
      gold = gold +10
      inven.remove("Package")
      cprint("Current Inventory: " + str(inven),"magenta")
      cprint("Current Gold: " + str(gold),"yellow")
      input("Press enter to continue.\n")
      etzor()
    else:
      print("Do you have something for me?")
      cprint("NEW QUEST: DELIVER THE WOMAN HER PACKAGE", "blue")
      quests.append("DELIVER PACKAGE TO DAKOTA IN ETZOR")
      input("Press enter to continue.\n")
      etzor()
  else:
    print(' The boy says: "Thanks for delivering my package!!"')
    input("Press enter to continue.\n")
    etzor()

def graveyard():
  #sets up correct check
  correct = False
  global gold
  global inven
  global gyflag
  global health
  #if not used already
  if gyflag == 0:
    print("You see the graveyard! Here, you must have a shovel to get in and dig up a grave.")
    #makes sure of shovel
    if "Shovel" in inven:
      print("In order to get the graveyard, solve this riddle that corresponds to a grave.")
      print("A boy blows 18 bubbles,\nThen pops 6 eats 7,\nAnd then he pops 5 and blows 1.\nHow many are left?")
      while correct == False:
        answer= input("Answer:\n")
        if answer == "1":
          correct = True
          cprint("Correct! You dig up the first grave and find 8 gold.")
          gyflag = 1
          cprint("-1 Shovel", "red")
          cprint("+8 Gold", "green")
          gold = gold +8
          inven.remove("Shovel")
          if "GET A SHOVEL AND GO TO THE GRAVEYARD" in quests:
            quests.remove("GET A SHOVEL AND GO TO THE GRAVEYARD")
          cprint("Current Inventory: " + str(inven),"magenta")
          cprint("Current Gold: " + str(gold),"yellow")
          input("Press enter to continue.\n")
          etzor()
        else:
          #if wrong:
          cprint("Incorrect! A Zombie Bats at you and you lose 2 health!","red")
          health = health-2
          #if dead:
          if health <= 0:
            cprint("YOU DIED TO A GRAVEYARD ZOMBIE.","red")
            quit()
          else:
            cprint("Current Health: "+str(health),"green")
            graveyard()
    else:
      #informing player
      print("You must enter the graveyard with a shovel.")
      cprint("NEW QUEST: GET A SHOVEL TO ENTER THE GRAVEYARD", "blue")
      quests.append("GET A SHOVEL AND GO TO THE GRAVEYARD")
      input("Press enter to continue.\n")
      etzor()
  else:
    #if already done:
    cprint('You already dug up the grave.','red')
    input("Press enter to continue.\n")
    etzor()
def vault():
  print("You arrive at the vault in the center of town.")
  print("You see three spaces for keys.")
  #checks for keys
  if "LAVA KEY" in inven and "FOREST KEY" in inven and "STEEL KEY" in inven:
    cprint("You found all the keys. Would you like to open the vault? (THIS WILL END THE GAME.)","green",attrs=["bold"])
    if input(">").lower() in ["y","yes","yep"]:
      cprint("You open the vault and take the crown of oblivion. You ascend to a higher power and escape the town.")
      cprint("YOU WIN!","green")
      quit()
    else:
      #if no
      cprint("You decide to finish things up first.")
      input("Press enter to continue.")
      etzor()
  else:
    #if no keys
    cprint("You don't have all the keys yet. Come back when you do.")
    input("Press enter to continue.")
    etzor()
      
    

  #sets up the main area to transport user to new places

def grandhub():
  clear()
  #global look around flag so people cant leave and come back to get more and more gold
  global lachflag
  global gold
  print("You arrive at the carriage hub. It's a bustling area full of carriages ready to take you anywhere you need.")
  print("Where would you like to go?")
  cprint(">North\n>South\n>East\n>West\n>Look Around","cyan")
  #sets up the where next answer and the flag that ensures answer is in range
  flag = 0
  while flag == 0:
    flag = 1
    wn = input(">" )
    if wn.lower() in ["n","north"]:
      trestinia()
    elif wn.lower() in ["s","south"]:
      lesto()
    elif wn.lower() in ["e","east"]:
      olenguard()
    elif wn.lower() in ["w","west"]:
      etzor()
    elif wn.lower() in ["l","look","look around"]:
      lachflag = lachflag+1
      print("You look around to a space similar to a train station. There are 4 carraiges that move back and forth between the towns, and every time someone uses one, another appears.")
      if lachflag == 1:
        print("You find 5 gold pieces underneath a tire!")
        gold = gold+5
      input("Press enter to continue.\n")
      grandhub()
    else:
      flag = 0
      print("incorrect answer, please input a new answer.")
      print("Where next?")

cprint("Would you like to see the tutorial?")
if input(">") in ["y",'yes','yep']:
  intro()
grandhub()
    






