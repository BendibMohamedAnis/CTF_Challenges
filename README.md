# CTF_Challenges
 My scripts made for CTF challenges including techniques used and methodology


# ROT.py : 
Script used for CTF: MOD 26  on picoCTF , the code takes string of the flag and adapt it to ROT16 methodology , there for getting the real flag.


# Recipe.py : 
Script used for GDG Algiers CTF challenge : the challenge gives a recipe of pancake that Bob gave to his friend , whenyou download the files you get pictures of ingredients used for the pancake and a picture for the flag , obviously we use steganography , i used OpenCV library to subtract first pictures ( egg from shell ) , use AND bitwise of open CV to make AND logic between bits of the picture for addind ingredients , on last mixing all withthe flag to get a pancake , so since A xor B xor C = D , is same as B = A xor D xor C , so we extrac the flag by xoring ingredients with secret_flavour and flag, the result gives a picture of the FLAG.  ( i might've made a mistake in the code since the flag is so hard to read correct me if you find it please) 

