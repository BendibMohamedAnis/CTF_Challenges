
import re
from turtle import bgcolor 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def searchLetterPos(letter):
    tmp="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(tmp)):
        if letter==tmp[i]:
            #print("found: ",tmp[i] ,"in pos: ",i+1)
            return i 
        else:
            i=i+1
        
def decypher(pos):

    tmp="abcdefghijklmnopqrstuvwxyz"
    if len(tmp)-pos<=13:
        return tmp[(pos+12)-(len(tmp)-1)]
    else:
        return tmp[pos+13]



t =input("Give ROT13 code : ")
t=t.lower()   
regex = re.compile("[@_!#$%^&*()<>?1234567890/\|}{~:']") 
flag=[]
for i in range(len(t)):
    if regex.search(t[i]) == None:
        pos=int(searchLetterPos(t[i]))
        dec=str(decypher(pos))
        flag.append(str(dec))
    else:
        flag.append(t[i])
    i=i+1

print(bcolors.OKGREEN +''.join(flag) + bcolors.ENDC)



