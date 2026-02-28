#Basic Syntax -> print(\*Objects, sep='', end='\n', file=sty.stdout, flush=False)

print("Hello World")

print(4+9)

#Multiple objects printing
print("Hello All", 5+8, "How are you", sep='\n',end=' ')

#printing to a file
print("print this to a file", file=open("output.txt","w"))

# Without flush=True
import time

print("Loading...", end=" ",)
time.sleep(2)
print("Done!")


