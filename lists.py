#lists
words = ["apples","love","people","K"]
print (words[0])
print (words[1])
print (words)


#lists can store any data types
dat = ['a',"k","too",'5','4',"hey"]
print (dat)


#nested lists
m = [
    [5,6,7],
    [8,9,1]
    ]
print (m)


# strings can also be indexed as lists
str = "hello class"
print (str[5])
print(str[6])
print(str[7-3])


#strings can not be readdressed like lists
strg = ["hello","class","123","51","abc","hey",'b','a']
print (strg)
print (strg[5])
print(strg[6])
print(strg[7-3])
strg [0] = strg [7-2]
print(strg)


# lists indexes can be re addressed
subjects = ["math","science","religious"]
subjects[2] = "mechanics"
print (subjects)