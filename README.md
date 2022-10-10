# CTF_Challenges
 My scripts made for CTF challenges including techniques used and methodology
 
<p align="center" width="100%"><img src="https://i0.wp.com/securitydaily.net/wp-content/uploads/2014/05/ctf1.jpg" /></p>


# ROT.py : 
Script used for CTF: MOD 26  on picoCTF , the code takes string of the flag and adapt it to ROT16 methodology , there for getting the real flag.


# Recipe.py : 
Script used for GDG Algiers CTF challenge : the challenge gives a recipe of pancake that Bob gave to his friend , when you download the files you get pictures of ingredients used for the pancake and a picture for the flag , obviously we use steganography , i used OpenCV library to subtract first pictures ( egg from shell ) , use AND bitwise of open CV to make AND logic between bits of the picture for adding ingredients , on last mixing all with the flag to get a pancake , so since A xor B xor C = D , is same as B = A xor D xor C , so we extrac the flag by xoring ingredients with secret_flavour and flag, the result gives a picture of the FLAG.  ( i might've made a mistake in the code since the flag is so hard to read correct me if you find it please) 

![lol321 %](https://user-images.githubusercontent.com/46926963/194893299-e4fbf9d0-90a0-4403-b738-dc6071e87488.png)


