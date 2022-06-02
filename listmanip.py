#for loop in python
mangoes = "Book"
for k in mangoes:
    print ("Taken one")  
print ("Done")

#for loops with lists
words = ["I","DID","A"]
for word in words:
    print (word + "!")

# counting letters in string
str = "Hello guys welcome back to my class"
count = 0
for x in str :
    if (x == "o"):
        count += 1
print ("The number of o's is :", count)

# withought L's
str = "Hello guys welcome back to my class"
count = 0
for x in str :
    if (x == "l"):
        continue
    else:
       print (x)