# Generating 3 digit non-neative random number using rnadom module
import random 
random_number = random.randint(100,999)
random_number_hundreds,random_number_tens, random_number_ones, User_Selected_Number_hundreds,User_Selected_Number_tens,User_Selected_Number_ones =0,0,0,0,0,0
no_of_chances = 0
cow_count=0
Bull_count=0
#Ask the User for 3 digit non-negative number
User_Name = input("Hi, Please Enter your Name :")
User_Selected_Number = int(input("Please guess the numberan[Number should be 3-digit and non-negative] :"))
#print(random_number)

def getdigitValues(num1,num2):
    global random_number_hundreds,random_number_tens, random_number_ones, User_Selected_Number_hundreds,User_Selected_Number_tens,User_Selected_Number_ones
    #getting HUndreds, Tens and Ones Value from random number
    random_number_hundreds = num1 // 100
    random_number_tens = (num1 // 10) % 10
    random_number_ones = num1 % 10
    #Getting Hundreds, Tens and Ones Values from User given number
    User_Selected_Number_hundreds = num2 // 100
    User_Selected_Number_tens = (num2 // 10) % 10
    User_Selected_Number_ones = num2 % 10

getdigitValues(random_number,User_Selected_Number)

# Checking the user entered number is in range or not
if User_Selected_Number in range(100,999):
    #Cheking if user given and random number are equal or not
    if random_number == User_Selected_Number:
            print("Bang,it's a BIG BULL. \nYou are guessed the number in first chance") 
    no_of_chances += 1
    Remaining_chances = 7
    #Check the number or indices matching or not 
    while(no_of_chances<=8):
        no_of_chances+=1
        if random_number == User_Selected_Number:
            print("Bang,it's a BIG BULL. \nYou are guessed the number in {} chances :".format(no_of_chances)) 
        
        #Checking the Random number hundreds value with all values of user given number
        if random_number_hundreds == User_Selected_Number_hundreds:
            Bull_count+=1 
        elif random_number_hundreds == User_Selected_Number_tens :
            cow_count+=1
        elif random_number_hundreds==User_Selected_Number_ones:
            cow_count+=1
            
        #Checking the Random number Tens value with all values of user given number    
        if random_number_tens == User_Selected_Number_tens:
            Bull_count+=1
        elif random_number_tens == User_Selected_Number_hundreds :
            cow_count+=1
        elif random_number_tens==User_Selected_Number_ones:
            cow_count+-1
            
        #Checking the Random number Ones value with all values of user given number
        if random_number_ones == User_Selected_Number_ones:
            Bull_count+=1
        elif random_number_ones == User_Selected_Number_hundreds :
            cow_count+=1
        elif random_number_ones==User_Selected_Number_tens:
            cow_count+-1

        if Bull_count !=0 and cow_count !=0 and Remaining_chances!=0:
            print("It's a Bull with count {} and Cow with count {} you have {} chanses".format(Bull_count,cow_count,Remaining_chances))
            User_Selected_Number = int(input("It's close, Guess another number"))
            getdigitValues(random_number,User_Selected_Number)
            Bull_count=0
            cow_count=0
            Remaining_chances-=1
        elif Bull_count != 0 and Remaining_chances!=0:
            print("It's a Bull with count {} and you have {} chanses".format(Bull_count,Remaining_chances))
            User_Selected_Number = int(input("It's close, Guess another number"))
            getdigitValues(random_number,User_Selected_Number)
            Bull_count=0
            Remaining_chances-=1
        elif cow_count != 0 and  Remaining_chances!=0:
            print("It's a Cow with count {} you have {} chanses".format(cow_count,Remaining_chances))
            User_Selected_Number = int(input())
            getdigitValues(random_number,User_Selected_Number)
            cow_count=0
            Remaining_chances-=1
        elif Remaining_chances == 0:
            print("Oops, You are unable to guess the number in 8 chances:")
            selected_option = int(input("1.Exit\t 2.Play Again"))
            if selected_option == 1:
                exit
            else:
                pass                        
        else:
            print("Oops, No numbers were matched Try with another number you have in {} chances :".format(Remaining_chances))
            User_Selected_Number = int(input())
            getdigitValues(random_number,User_Selected_Number)
            Remaining_chances-=1   
else:
    print('Please, Enter a valid number[number should be 3 digit(between 100 to 999) and non-neative]. Thanks!')
    User_Selected_Number = int(input())
    getdigitValues(random_number,User_Selected_Number)
    pass
