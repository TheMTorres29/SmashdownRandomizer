import sys
import random

def main():
    # Fighter List
    smashFighters = [
        'Mario', 'DK', 'Link', 'Samus', 'DarkSamus', 'Yoshi', 'Kirby', 'Fox', 'Pikachu', 'Luigi', 'Ness', 'CFalcon', 'Jigglypuff',
        'Peach', 'Daisy', 'Bowser', 'IceClimbers', 'Sheik', 'Zelda', 'DrMario', 'Pichu', 'Falco', 'Marth', 'Lucina', 'YoungLink', 'Ganon',
        'Mewtwo', 'Roy', 'Chrom', 'MrGame', 'MetaKnight', 'Pit', 'DarkPit', 'ZeroSuitSamus', 'Wario', 'Snake', 'Ike', 'PkmTrainer', 'Diddy',
        'Lucas', 'Sonic', 'DDD', 'Olimar', 'Lucario', 'ROB', 'ToonLink', 'Wolf', 'Villager', 'Megaman', 'WiiFit', 'Rosalina', 'LilMac', 'Greninja',
        'Palutena', 'Pacman', 'Robin', 'Shulk', 'BowserJr', 'DuckHunt', 'Ryu', 'Ken', 'Cloud', 'Corrin', 'Bayo', 'Inkling', 'Ridley', 'Simon', 'Richter',
        'KRool', 'Isabelle', 'Incineroar', 'Plant', 'Joker', 'Hero', 'Banjo', 'Terry', 'Byleth', 'Minmin', 'Steve', 'Seph', 'Aegis', 'Kazuya', 'Sora'
    ]

    # Title
    print('[ SmashDown Randomizer ]')
    
    while True:
        player1 = random.choice(smashFighters)
        player2 = random.choice(smashFighters)

        # Ditto Check
        if player1 == player2:
            while player1 == player2:
                player2 = random.choice(smashFighters)

        # Random Results
        print(f'Player 1: {player1} VS Player 2: {player2}')
        userInput = input('Keep going? (Y/N)  ').upper()
        
        # Continue?
        if userInput == 'Y':
            smashFighters.remove(player1)
            smashFighters.remove(player2)
            print(str(len(smashFighters)) + " fighters left")
            if len(smashFighters) == 1:
                break
            continue
        else:
            sys.exit('Ending Session. Goodbye!')
    
    print('Roster Complete!')

main()