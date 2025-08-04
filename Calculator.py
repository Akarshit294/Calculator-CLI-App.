def validstr(s):
    for i in s:
        if not (i.isdigit() or i == "+" or i == "-" or i == "*" or i =="/") or not s[0].isdigit() or not s[len(s)-1].isdigit():
            return True
    return False

def makelist(s):
    l =[]
    q = ""
    for i in range(len(s)):
        if s[i].isdigit():
            q += s[i]
        else: 
            l.append(q)
            l.append(s[i])
            q = ""
    l.append(q)
    return calc(l)

def calc(l):
    x = 1
    y = 0
    z = ['/','*','-','+']
    while(y < 4):
        if l[x] == z[y] and y == 0:
            l[x-1] = int(l[x-1])/int(l[x+1])
            del l[x]
            del l[x]
            x = 0
        elif l[x] == z[y] and y == 1:
            l[x-1] = int(l[x-1])*int(l[x+1])
            del l[x]
            del l[x]
            x = 0
        elif l[x] == z[y] and y == 2:
            l[x-1] = int(l[x-1])-int(l[x+1])
            del l[x]
            del l[x]
            x = 0
        elif l[x] == z[y] and y == 3:
            l[x-1] = int(l[x-1])+int(l[x+1])
            del l[x]
            del l[x]
            x = 0
        x += 1
        if x >= len(l):
            x = 0
            y += 1
    return l[0]


print("\n----------This is a Simple Expression Calculator----------")
print("Enter a mathematical expression consisting of integers and symbols( +, -, *, /). If you wish to Quit, then enter q. ")

while(1):
    s = input("Enter the expression: ")
    s.lower()

    if s == 'q':
        print("----------Good Bye!----------\n")
        break

    if validstr(s):
        print("Please enter valid string containing only intergers and '+', '-', '*', '/' or 'q'.")

    print(f"The solution to the given expression is: {makelist(s)}\n")
