# Name: David Burke
# Evergreen Login: burdav22
# 
#
## Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done. When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test

n = hw2_test
sum = 0
i = 1


while i <= n:
    sum = sum + i
    i = i + 1
print sum


    
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"


for i in range(1, 10): # loop numbers from 1-10
    i = i/1.0 #is there a better way to turn i into a floating point?
    print 1/i

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
tri = 0
for i in range (n+1):
    tri = tri+i
print "Triangular number", n, "via loop:", tri
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n=10
m=1
for i in range(n):
    m= m*(i+1) #makes multi equal the previous multi times the running count
if n == 0: # if the factorial is 0! print multi-1 or else just print multi
    print m-1
else:
    print m
    

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n=10
f=1
for i in range(n):
    x=1 #resets f after it has gone through second for loop
    x= n
    x = n-i # makes the range smaller 
    for j in range(x):
         f= f*(j+1) #creates the factorial
    print f

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
ftwo=1
add=1

for i in range(n):
    add = add+(1/f) #adds the two factorals together
    factor=1
    x = n
    x = n-i
    for j in range(x):
         ftwo= ftwo*(j+1)/1.0
print add

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###
### Took maybe 3-4 hours total...worked with Jake. All in all, not terribly difficult, but I still learned some cool tricks. 

