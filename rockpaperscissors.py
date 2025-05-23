"""This is a game of rock paper scissors written in Python, without using objects and separate functions. 
Here are the requirements of the game
    Ask each player for their name. Print their name during game prompts.
    Ask each player to choose rock, paper, or scissors. Confirm it's a valid choice.
    Apply game rules: rock beats scissors, scissors beats paper, paper beats rock, ties.
    Ask if players would like to play again.
    Track game results.
    Display the result to the players
All code is original and was made to enhance my skill integration."""

#track who is playing the game
print("*** Welcome to Rock - Paper - Scissors! ***\n\n")
player_one_name = input("Player 1, what is your name? (maximum of 10 characters):")
player_two_name = input("Player 2, what is your name? (maximum of 10 characters):")

#keep a maximum of 10 characters and remove white space from the ends
player_one_name = player_one_name[:10].strip()
player_two_name = player_two_name[:10].strip()

#track game stats
player_one_games=0
player_two_games=0
player_one_game_wins=0
player_two_game_wins=0
player_one_game_ties=0
player_two_game_ties=0


#start the first game or if the players would like to play again, start a another game
print(f"\n\nAlright {player_one_name} and {player_two_name}, let's start the game! \n\n")
play_again = True
while play_again:
        #retrieve player one's move
        player_one_move=input(f"{player_one_name}, choose your option: \n 1. Rock \n 2. Paper \n 3. Scissors \n Select [1-3]:")
        
        #validate the move and continue to ask for a valid move
        while int(player_one_move) < 1 or int(player_one_move)>3:
            print(f"{player_one_move} is an invalid selection. Enter a 1, 2 or 3.")
            player_one_move=input(f"{player_one_name}, choose your option: \n 1. Rock \n 2. Paper \n 3. Scissors \n Select [1-3]:")
        
        #retrieve player two's move
        player_two_move=input(f"\n \n{player_two_name}, choose your option: \n 1. Rock \n 2. Paper \n 3. Scissors \n Select [1-3]:")

        #validate the move and continue to ask for a valid move
        while int(player_two_move) < 1 or int(player_two_move)>3:
            print(f"{player_two_move} is an invalid selection. . Enter a 1, 2 or 3.")
            player_two_move=input(f"{player_two_name}, choose your option: \n 1. Rock \n 2. Paper \n 3. Scissors \n Select [1-3]:")

        #add some whitespace
        print("\n\n")

        #apply the rules of the game to determine the winner
        match int(player_one_move) + int(player_two_move):
                case 2:
                    #both selected rock, game is a tie
                    player_one_games +=1
                    player_two_games +=1

                    player_one_game_ties +=1
                    player_two_game_ties +=1
                    
                    print("It's a tie!")
                
                case 4:
                    player_one_games +=1
                    player_two_games +=1
                    
                    #one selected rock, the other player selected scissors
                    #rock beats scissors
                    if int(player_one_move) == 1:
                        player_one_game_wins +=1
                        print(f"{player_one_name} wins!")
                    elif int(player_two_move) == 1:
                        player_two_game_wins +=1
                        print(f"{player_two_name} wins!")
                    else:
                        #both selected paper, game is a tie
                        player_one_game_ties +=1
                        player_two_game_ties +=1
                        print("It's a tie!")

                case 6:
                    #both selected scissors, game is a tie
                    player_one_games +=1
                    player_two_games +=1

                    player_one_game_ties +=1
                    player_two_game_ties +=1
                    print("It's a tie!")

                case 3:
                    #one player selected rock, the other player selected paper
                    player_one_games +=1
                    player_two_games +=1
                    
                    #paper beats rock
                    if player_one_move == 2:
                        player_one_game_wins +=1
                        print(f"{player_one_name} wins!")
                    else:
                        player_two_game_wins +=1
                        print(f"{player_two_name} wins!")

                case 5:
                    #one player selected scissors, the other player selected paper
                    player_one_games +=1
                    player_two_games +=1
                    
                    #scissors beats paper
                    if player_one_move == 2:
                        player_one_game_wins +=1
                        print(f"{player_one_name} wins!")
                    else:
                        player_two_game_wins +=1
                        print(f"{player_two_name} wins!")        

                case _ :
                    #an error occured
                    player_one_games +=1
                    player_two_games +=1
                    print("Uh oh, this game ends in error.")
                   

        #check to see if another game
        play_again_temp=input(f"\n \nWould you like to play another game, {player_one_name} and {player_two_name}?\nType Y or N:").strip().upper()
        while not(play_again_temp == "Y") and not(play_again_temp == "N"):
            print(f"\n\n{play_again_temp} is an invalid option. Enter a Y for 'Yes' or N for 'No'.")
            play_again_temp=input(f"Would you like to play another game, {player_one_name} and {player_two_name}?\nType Y or N:")    

        if play_again_temp=="Y":
            play_again=True
            print(f"Ok! Let's play game #{player_one_games +1}")
            print("\n\n")
        else:
            play_again=False
    
#finished playing games
print("\n\nThat's it folks! Thanks for playing! \n\nHere are the statistics:")
print("-" * 53 )
print(f"|{"Player Name":<12}|{"Wins":<12}|{"Ties":<12}|{"Total":<12}|")
print("-" * 53 )
print(f"|{player_one_name:<12}|{player_one_game_wins:>12}|{player_one_game_ties:>12}|{player_one_games:>12}|")
print("-" * 53 )
print(f"|{player_two_name:<12}|{player_two_game_wins:>12}|{player_two_game_ties:>12}|{player_two_games:>12}|")
print("-" * 53 )
    

        