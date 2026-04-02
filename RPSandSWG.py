import random as raom #Random Module

print('\t\tWelcome to the game of pro\'s.\t\t\n') #Subtitle 

ask_play = input('What do you wnat to play snake,water,gun or rock,paper,scissor? (Give SWG for snake,water,gun and RPS for rock,paper,scissor):') #Asking user to choose the game

def rps(): #The first game
    print('''\nYou are playing RPS which is rock,paper and scissor\n
The Rules are:
You will get 1 point for each win and lose 1 point if you lose and get no point if its a tie!\n''')

    ask_user = input("Will you able to beat me in rock,paper,scissor (Yes/No):")

    if ask_user.lower() == 'yes':
        option = ("rock","paper","scissor")       
        score = 0 
        round = input("\nHow many rounds you wanna play:") 
        if round.isnumeric():
            round = int(round)   
            count_round = 0
        
            while count_round < round:
                computer = raom.choice(option) 
                user_input = input('\nPlease give your input:').lower()
                if computer == 'rock' and user_input == 'rock':
                    print(f'Its a tie! SCORE = {score}') 
                elif computer == 'rock' and user_input == 'paper':
                    score += 1
                    print('Its a win for you!','+1 added to score.')
                elif computer == 'rock' and user_input == 'scissor':
                    score -= 1
                    print('I win!','-1 from score.')    
                
                elif computer == 'paper' and user_input == 'paper':
                    print(f'Its a tie! SCORE = {score}')
                elif computer == 'paper' and user_input == 'scissor':
                    score += 1
                    print('Its a win for you!','+1 added to score.')    
                elif computer == 'paper' and user_input == 'rock':
                    score -= 1
                    print('I win!','-1 from score.')    

                elif computer == 'scissor' and user_input == 'scissor':
                    print(f'Its a tie! SCORE = {score}')
                elif computer == 'scissor' and user_input == 'rock':
                    score += 1
                    print('Its a win for you!','+1 added to score.')    
                elif computer == 'scissor' and user_input == 'paper':
                    score -= 1
                    print('I win!','-1 from score.') 
                
                else:
                    print("Invalid Input! Give option from rock,paper,scissor")
                
                print(f"\nMy choice was {computer} and your was {user_input}.")
                print(f"Your Total score is {score}.")

                count_round += 1
                            
        else:
            print('Invalid Input!')

    elif ask_user.lower() == 'no':
        print('\nOkay! Come on just try once!\n')
        ask_user2 = input('Do you want to continue playing? (Yes/No):')
        if ask_user2.lower() == 'yes':
            print('\n|You are the pro who doen\'t want to show your levels.|')
            rps()
        elif ask_user2.lower() == 'no':
            print('\n|You are the person who will become the greatest noob of the world.|')
        else:
            print('Invalid Input!')    

    else:
        print('Invalid Input!')

def swg(): #The second game
    print('''\nYou are playing SWG which is snake,water and gun\n
The Rules are:
You will get 1 point for each win and lose 1 point if you lose and get no point if its a tie!\n''')

    ask_user3 = input("Will you able to beat me in snake,water,gun (Yes/No):")

    if ask_user3.lower() == 'yes':
        option2 = ("snake","water","gun")       
        score2 = 0 
        round2 = input("\nHow many rounds you wanna play:") 
        if round2.isnumeric():
            round2 = int(round2)   
            count_round2 = 0
        
            while count_round2 < round2:
                computer2 = raom.choice(option2) 
                user_input2 = input('\nPlease give your input:').lower()
                if computer2 == 'snake' and user_input2 == 'snake':
                    print(f'Its a tie! SCORE = {score2}') 
                elif computer2 == 'snake' and user_input2 == 'gun':
                    score2 += 1
                    print('Its a win for you!','+1 added to score.')
                elif computer2 == 'snake' and user_input2 == 'water':
                    score2 -= 1
                    print('I win!','-1 from score.')    
                
                elif computer2 == 'water' and user_input2 == 'water':
                    print(f'Its a tie! SCORE = {score2}')
                elif computer2 == 'water' and user_input2 == 'snake':
                    score2 += 1
                    print('Its a win for you!','+1 added to score.')    
                elif computer2 == 'water' and user_input2 == 'gun':
                    score2 -= 1
                    print('I win!','-1 from score.')    

                elif computer2 == 'gun' and user_input2 == 'gun':
                    print(f'Its a tie! SCORE = {score2}')
                elif computer2 == 'gun' and user_input2 == 'water':
                    score2 += 1
                    print('Its a win for you!','+1 added to score.')    
                elif computer2 == 'gun' and user_input2 == 'snake':
                    score2 -= 1
                    print('I win!','-1 from score.') 
                
                else:
                    print("Invalid Input! Give option from snake,water,gun")
                
                print(f"\nMy choice was {computer2} and your was {user_input2}.")
                print(f"Your Total score is {score2}.")

                count_round2 += 1
                            
        else:
            print('Invalid Input!')

    elif ask_user3.lower() == 'no':
        print('\nOkay! Come on just try once!\n')
        ask_user4 = input('Do you want to continue playing? (Yes/No):')
        if ask_user4.lower() == 'yes':
            print('\n|You are the pro who doen\'t want to show your levels.|')
            swg()
        elif ask_user4.lower() == 'no':
            print('\n|You are the person who will become the greatest noob of the world.|')
        else:
            print('Invalid Input!')    

    else:
        print('Invalid Input!')

if ask_play.lower() == 'rps':
    rps()
elif ask_play.lower() == 'swg':
    swg()
else:
    print('Invalid Input!')
