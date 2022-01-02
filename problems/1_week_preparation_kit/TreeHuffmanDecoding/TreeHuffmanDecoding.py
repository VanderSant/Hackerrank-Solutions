"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def printChar(root, s):
    if(root.data == '\0'):
        if(s[0]=='1'):
            s = s[1::]
            return printChar(root.right, s)
        elif(s[0]=='0'):
            s = s[1::]
            return printChar(root.left, s)
        else:
            print("ERROR")
    else:
        print(root.data,end='')
        return s

def decodeHuff(root, s):
    while(s != ''):
        s = printChar(root, s)
                        

