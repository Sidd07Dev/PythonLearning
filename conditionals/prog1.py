userAge = int(input("Provide me your age : "))

if(userAge < 13):
    print("User is child")
elif(userAge < 20):
    print("User is teenager")
elif(userAge < 60):
    print("User is adult")
else:
    print("Useer is senior")