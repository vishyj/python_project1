my_num=8+-8
tries=int(input("How many chances would you like to have to guess the number? "))
sup=int(input("Enter a number: "))
for i in range (1,tries):
    if sup==my_num:
        print "You got it!"
        break
    else:
        print "Sorry that is the wrong number!"
        sup = int(input("Enter a new number: "))