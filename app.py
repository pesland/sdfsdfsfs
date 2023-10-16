from skpy import Skype

slogin = Skype ("part_01_1@hotmail.com", "0544302909739A")

contact = slogin.contacts

for i in contact :
print(i)
