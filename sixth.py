"""how to print this using recursion "The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following:12345 Note that "" represents the consecutive values in between."""

def number(n):
    if(n==0):
        return
    else:
        number(n-1)
        print(n,end="") # end is used stay on same line
n=int(input())
number(n)