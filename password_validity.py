#initialising valid variable to false and pswd is taken from the user
valid,pswd= False, input("enter the password")
length = len(pswd)

#Checking whether the password length is in the required range 
if(8<=length<=32):
    #checking whether starting character is an alphabet
    if 'a' <= pswd[0] <= 'z' or 'A' <=pswd[0] <= 'Z':
      #checking all the special characters which should not be present in the password as per the program
        if not ('/' in pswd or '\\' in pswd or '=' in pswd or ' ' in pswd or '"' in pswd or "'" in pswd):
            valid= True
print(valid)
        
    
