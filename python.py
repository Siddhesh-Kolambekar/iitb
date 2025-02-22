string="siddhesh"
def reverse(string):
    n=len(string)
    for i in range(n-1,-1,-1):
        print(string[i],end="")
reverse(string)