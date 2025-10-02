def Hello() :
    print ("You input: ", var_user, "Good!")
var_1 = 6
var_user = int( input( f"input number less than : {var_1}\n"))
if var_1 > var_user :
   Hello()
else:
    print("You input: ", var_user, "Incorrect")

