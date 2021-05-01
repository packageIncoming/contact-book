import datamanager as dm
import os

if not os.path.exists("contacts.db"):
  dm.initialize()


print("You have booted up the contacts program. Here are your availiable actions: \n1: Show all contacts. \n2: Add in a contact. \n3: Remove a contact.\nAdding in a contact that already exists will update that previous contact.")

def get_input():
  string = "\nPlease enter in a valid input. For help, please type 'HELP'. To stop the program, type 'STOP'.\n"
  return input(string)

def make_contact():
  firstname = input("Please enter a first name for this contact: ")
  print('')
  lastname = input("Please enter a last name for this contact: ")
  print('')
  number = input("Please enter a number for this contact XXX-XXX-XXXX format: ")
  print('')
  return firstname,lastname,number

def remove_contact():
  idx = input("Please enter the index of the contact you wish to remove: ")
  idx = int(idx)
  dm.delete_one(idx)
  print("Deleted contact at index {} successfully.".format(idx))


#1: Show all contents
#2: Add in contact
#3: Remove contact

uinput = get_input()

while uinput.lower() != "stop":
  if uinput == '1':
    print("Your current contacts are as follows:")
    dm.show_all()
  elif uinput == '2':
    firstname,lastname,number = make_contact()
    dm.add_one(firstname,lastname,number)
  elif uinput == '3':
    remove_contact()
  elif uinput.lower() == "help":
    print("\n1: Show all contacts. \n2: Add in a contact. \n3: Remove a contact.\nAdding in a contact that already exists will update that previous contact.")
  uinput = get_input()
