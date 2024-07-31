import random

def new_line():
    print()

def game_boot():
    setup_player()
    choose_occupation()
    choose_stats()

def setup_player():
    player_name = input("What is your name? ")

def choose_occupation():
    # occupation
    occupation_options = ["Farmer"]
    print(f"Please select your occupation from the following list: ")
    
    for occupation in occupation_options:
        print(occupation)
        
    chosen_occupation = input()

    if chosen_occupation in occupation_options:
            
        while True:
            occupation_confirmation = input(f"You have selected {chosen_occupation}. Would you like to continue (yes/no)? ")
        
            if occupation_confirmation == "yes" or occupation_confirmation == "no":          
                if occupation_confirmation == "yes":
                    print(f"Continuing with the selected occupation {chosen_occupation}...")
                    break
                
                elif occupation_confirmation == "no":
                    print("Returning to occupation selection...")
                    choose_occupation()
                    break
            else: 
                print("Please respond with 'yes' or 'no'")
                
    else:
        choose_occupation()
    
def choose_stats():
    stat_points = 10
    stats = ["Strength","Charm","Wisdom"]
    print(f"You have {stat_points} allotted stat points. You may distribute these points between the following categories:")
    
    for stat in stats:
        print(stat)
        
    player_strength = 0
    player_charm = 0
    player_wisdom = 0
    
    # for stat in stats optimization loop eventually
    
    while stat_points > 0:
        try: 
            strength = int(input(f"How many points would you like to distribute to {stats[0]}? "))
            if strength <= stat_points:
                player_strength += strength
                stat_points -= strength
                print(f"Remaining stat points: {stat_points}")
                break
            else:
                print(f"You do not have {strength} stat points available")
        except ValueError:
            print("Please enter a numerical value")
 
    while stat_points > 0:
        try: 
            charm = int(input(f"How many points would you like to distribute to {stats[1]}? "))
            if charm <= stat_points:
                player_charm += charm
                stat_points -= charm
                print(f"Remaining stat points: {stat_points}")
                break
            else:
                print(f"You do not have {charm} stat points available")
        except ValueError:
            print("Please enter a numerical value")
        
    while stat_points > 0:
        try: 
            wisdom = int(input(f"How many points would you like to distribute to {stats[2]}? "))
            if wisdom <= stat_points:
                player_wisdom += wisdom
                stat_points -= wisdom
                print(f"Remaining stat points: {stat_points}")
                break
            else:
                print(f"You do not have {wisdom} stat points available")
        except ValueError:
            print("Please enter a numerical value")   
    
    while True:
        print(f"Your stat distribution is: \nStrength: {player_strength} \nCharm: {player_charm} \nWisdom: {player_wisdom}")
        stat_confirmation = input("Are you satisfied with this distribution (yes/no)? ")
        
        if stat_confirmation == "yes" or stat_confirmation == "no":          
            if stat_confirmation == "yes":
                print(f"Continuing with the selected stats...")
                break
            
            elif stat_confirmation == "no":
                print("Returning to stat selection...")
                choose_stats()
                break
        else: 
            print("Please respond with 'yes' or 'no'")

def main():
    game_boot()

if __name__ == '__main__':
    main()