import emoji , random
def ran():
    rand=random.randint(1,20)
    return rand
def main():
    x=input("\n press 1 to play\n press 2 to exit\n")
    while int(x)!=1 or int(x)!=2:
        if int(x)==1:
            y=input("\n Enter a number between 1 to 20 to see can you think like computer\n")
            z=ran()
            if int(y)==int(z):
                print("wow '\U0001F60D''\U0001F60D' you guess the nember :",int(z))
                ag=input("want to play again press 1 or any key to exit\n")
                if int(ag)==1:
                    x=input("\n press 1 to play\n press 2 to exit\n")
                else:
                    exit()
            else:
                print("boow '\U0001F624''\U0001F44E' you failed to guess\n don't worry you can play again\n")
                print("the number was:", int(z))
                ag=input("\nwant to play again press 1 or any key to exit\n")
                if int(ag)==1:
                    x=input("\n press 1 to play\n press 2 to exit\n")
                else: 
                    exit()    
        else:
            exit()
main()                
