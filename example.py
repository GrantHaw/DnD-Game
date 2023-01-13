# author: Jeremy Holley
# CSC119 Spring 2021

import time		# used to add wait time during printing
import sys		# used to exit the program
import os		# used to clear the console
from termcolor import cprint 	# print in different colors


# The first room
def room1(inventory):
	user_pick = None

	# describe the room
	print("You enter room1.\n")

	# let the user continue to make choices in the room
	while user_pick != "4":
		# wait for 1.5 seconds
		time.sleep(1.5)
		
		print("\nYou are in room1. (describe the room)\n")
		cprint("Inventory:" + str(inventory), "blue", "on_white")
		print("\nWhat would you like to do?\n1. Go left\n2. Go right\n3. Look around\n4. Quit\n")

		# allow the user to enter a choice
		user_pick = input()

		# one of these conditions executes based on what the user chose
		if user_pick == "1":
			# go left
			room2(inventory)
		elif user_pick == "4":
			# quit the game
			sys.exit()
		else:
			cprint("\nThat is not a valid choice. Try again.", "red")


# The library room that has a skeleton key item for solving a puzzle
def room2(inventory):
	user_pick = None

	# describe the room
	print("You the Library. It reeks of old, musky books and has a half-inch of dust covering everything. You notice a spot on one of the bookshelves where the dust has been disturbed.")

	# let the user continue to make choices in the room
	while user_pick != "4":
		# wait for 1.5 seconds
		time.sleep(1.5)

		cprint("\nInventory: " + str(inventory), "yellow",)
		print("\nWhat would you like to do?\n1. Go forward\n2. Go back\n3. Look around\n4. Quit\n")

		# wait for the user's choice
		user_pick = input()

		if user_pick == "3" and "skeleton key" not in inventory:
			print("\nYou look around and find a key.\n")
			cprint("SKELETON KEY ADDED TO INVENTORY\n", "green")
			inventory.append("skeleton key")
		elif user_pick == "3" and "skeleton key" in inventory:
			print()
			cprint(" YOU FIND NOTHING OF INTEREST ", "grey", "on_white", attrs = ['bold'])


# clears the console when called
def clear():
	os.system("clr" if os.name == "nt" else "clear")


# The main method starts the game by defining variables and calling the first_room function
def main():

	inventory = ["shovel"]
	room1(inventory)


main()