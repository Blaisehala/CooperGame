from random import randint

# create_ a list of options

options = ['scissors', 'papers', 'rock', 'spock', 'lizard']


play = True 

while play == True:

    computer_option = options[randint(0,4)]


    print('>'*20)
    print('Please select: Rock, Paper, Scissors, Lizard or Spock')

    player_input = input ('Your choice: ').lower()


    print (f'Computer choice: {computer_option}')


    # for a Tie

    if player_input == computer_option:
        print ('Tie')


  
    elif player_input == 'rock':

        if computer_option == "Paper":
            print(f"You lose😕")

        elif computer_option== "Scissors":
            print("You win🎉")

        elif computer_option == "Lizard":
            print("You win🎉")

        elif computer_option == "Spock":
            print("You lose😕")



  #paper
    elif player_input == "Paper":

        if computer_option == "Scissors":
             print("You lose😕")

        elif computer_option =="Rock":
            print("You win🎉")

        elif computer_option == "Lizard":
            print("You lose😕")

        elif computer_option == "Spock":
            print("You win🎉")



  #scissor 

    elif player_input == "Scissors":

        if computer_option == "Paper":
            print("You win🎉")


        elif computer_option == "Rock":
            print("You lose😕")


        elif computer_option =="Lizard":
            print("You win🎉")


        elif computer_option == "Spock":
            print("You lose😕")




  #Lizard
    elif player_input == "Lizard":

        if computer_option =="Rock":
            print("You lose😕")

        elif computer_option =="Paper":
            print("You win🎉")

        elif computer_option == "Scissors":
            print("You lose😕")

        elif computer_option == "Spock":
            print("You win🎉")



    

    ##Spock
    elif player_input == "Spock":

        if computer_option == "Rock":
            print("You win🎉")

        elif computer_option == "Paper":
            print("You lose😕")

        elif computer_option == "Scissors":
            print("You win🎉")

        elif computer_option == "Lizard":
            print("You lose😕") 

    

    print("Would you like to play again🤗? y\n")
    answer =input('Your choice: ').lower()
    

    if answer =="y" or answer =="yes":
        play == True


    else:
        break


  




 










  





