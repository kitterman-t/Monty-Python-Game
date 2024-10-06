"""
Monty Python and the Holy Grail Game

This is a text game based on the movie. Players take on the role of King Arthur.
They will navigate through various scenarios from the movie in search of the Holy Grail.

Author: Tim Kitterman
Date: 03 Oct 2024
"""

import random

# Dictionary: Stores game states and their corresponding narratives
game_states = {
    "start": "You are King Arthur, and your quest for the Holy Grail begins!",
    "castle": "You approach a castle. A French guard taunts you from the ramparts.",
    "bridge": "You encounter the Bridge of Death, guarded by the old man from Scene 24.",
    "forest": "You enter a dark and very expensive forest.",
    "swamp": "You find yourself in a swamp, surrounded by Knights who say Ni!",
    "cave": "You discover a cave with ancient writing on the wall.",
    "end_victory": "Congratulations! You have found the Holy Grail!",
    "end_defeat": "Your quest has ended in failure. Better luck next time!",
    "end_arrest": "You are arrested by modern-day police for a historian's murder."
}

# Dictionary of Lists: Stores available choices for each game state
choices = {
    "start": ["Seek the Holy Grail", "Recruit Knights", "Go to Camelot"],
    "castle": ["Insult the French", "Use the Trojan Rabbit", "Retreat"],
    "bridge": ["Answer the questions", "Run away", "Push the old man"],
    "forest": ["Chop down a tree with a herring", "Run from the Knights who say Ni!", "Offer a shrubbery"],
    "swamp": ["Say 'Ni!'", "Cut down the mightiest tree with a herring", "Give them a shrubbery"],
    "cave": ["Read the ancient writing", "Look for the Holy Grail", "Leave the cave"]
}

def initialize_player():
    """
    Initialize the player's stats.
    
    Returns:
    tuple: A tuple containing (score, coconuts, shrubberies)
    """
    return (0, 2, 0)  # Tuple: (score, coconuts, shrubberies)

def display_state(state, player_stats):
    """
    Display the current game state and player stats.
    
    Args:
    state (str): The current game state
    player_stats (tuple): A tuple containing (score, coconuts, shrubberies)
    """
    print(f"\n------ Score: {player_stats[0]} | Coconuts: {player_stats[1]} | Shrubberies: {player_stats[2]} ------")
    print("\n" + game_states[state])

def get_player_choice(state):
    """
    Get the player's choice for the current state.
    
    Args:
    state (str): The current game state
    
    Returns:
    int: The index of the player's choice
    """
    print("\nWhat will you do?")
    for i, choice in enumerate(choices[state], 1):
        print(f"  {i}. {choice}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: ")) - 1
            if 0 <= choice < len(choices[state]):
                print("")
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def update_state(state, choice, player_stats):
    """
    Update the game state based on the player's choice.
    
    Args:
    state (str): The current game state
    choice (int): The index of the player's choice
    player_stats (tuple): A tuple containing (score, coconuts, shrubberies)
    
    Returns:
    tuple: A tuple containing the new state and updated player stats
    """
    score, coconuts, shrubberies = player_stats
    
    # State transitions based on player choices
    if state == "start":
        if choice == 0:  # Seek the Holy Grail
            print("Your quest begins in earnest!")
            score += 10
            return "castle", (score, coconuts, shrubberies)
        elif choice == 1:  # Recruit Knights
            print("You gather the Knights of the Round Table.")
            score += 5
            return "forest", (score, coconuts, shrubberies)
        else:  # Go to Camelot
            print("On second thought, let's not go to Camelot. 'Tis a silly place.")
            return "swamp", (score, coconuts, shrubberies)
    
    elif state == "castle":
        if choice == 0:  # Insult the French
            print("Your mother was a hamster and your father smelt of elderberries!")
            score -= 5
            return "forest", (score, coconuts, shrubberies)
        elif choice == 1:  # Use the Trojan Rabbit
            print("The French catapult your own rabbit back at you!")
            score += 5
            return "bridge", (score, coconuts, shrubberies)
        else:  # Retreat
            print("You bravely run away!")
            return "swamp", (score, coconuts, shrubberies)
    
    elif state == "bridge":
        if choice == 0:  # Answer the questions
            if random.random() < 0.5:  # 50% chance of success
                print("You answer the questions correctly and cross the bridge!")
                score += 20
                return "cave", (score, coconuts, shrubberies)
            else:
                print("You are cast into the Gorge of Eternal Peril!")
                return "end_defeat", (score, coconuts, shrubberies)
        elif choice == 1:  # Run away
            print("You wisely decide not to risk it.")
            return "forest", (score, coconuts, shrubberies)
        else:  # Push the old man
            print("You push the old man, but fall into the gorge yourself!")
            return "end_defeat", (score, coconuts, shrubberies)
    
    elif state == "forest":
        if choice == 0:  # Chop down a tree with a herring
            print("The Knights who say Ni! appear and demand a shrubbery!")
            return "swamp", (score, coconuts, shrubberies)
        elif choice == 1:  # Run from the Knights who say Ni!
            print("You bravely run away!")
            return "castle", (score, coconuts, shrubberies)
        else:  # Offer a shrubbery
            if shrubberies > 0:
                print("The Knights who say Ni! are appeased!")
                score += 15
                shrubberies -= 1
                return "cave", (score, coconuts, shrubberies)
            else:
                print("You don't have a shrubbery to offer!")
                return "swamp", (score, coconuts, shrubberies)
    
    elif state == "swamp":
        if choice == 0:  # Say 'Ni!'
            print("The Knights who say Ni! are not impressed.")
            score -= 5
            return "forest", (score, coconuts, shrubberies)
        elif choice == 1:  # Cut down the mightiest tree with a herring
            print("You fail miserably, but the Knights are amused.")
            score += 5
            return "bridge", (score, coconuts, shrubberies)
        else:  # Give them a shrubbery
            if shrubberies > 0:
                print("The Knights who say Ni! are appeased!")
                score += 15
                shrubberies -= 1
                return "cave", (score, coconuts, shrubberies)
            else:
                print("You don't have a shrubbery to give!")
                return "forest", (score, coconuts, shrubberies)
    
    elif state == "cave":
        if choice == 0:  # Read the ancient writing
            print("The writing reveals the location of the Holy Grail!")
            score += 10
            return "end_victory", (score, coconuts, shrubberies)
        elif choice == 1:  # Look for the Holy Grail
            if random.random() < 0.3:  # 30% chance of finding the Grail
                print("You've found the Holy Grail!")
                score += 50
                return "end_victory", (score, coconuts, shrubberies)
            else:
                print("You find nothing but an empty cave.")
                return "castle", (score, coconuts, shrubberies)
        else:  # Leave the cave
            print("You decide to search elsewhere.")
            return "bridge", (score, coconuts, shrubberies)
    
    # Random events (chance element)
    if random.random() < 0.2:  # 20% chance of a random event
        event = random.choice(["coconut", "shrubbery", "arrest"])
        if event == "coconut":
            print("You found coconuts! You can now simulate the sound of horse hooves.")
            coconuts += 1
            score += 5
        elif event == "shrubbery":
            print("You stumbled upon a shrubbery!")
            shrubberies += 1
            score += 10
        elif event == "arrest":
            print("Modern-day police arrive to arrest you for the historian's murder!")
            return "end_arrest", (score, coconuts, shrubberies)
    
    return state, (score, coconuts, shrubberies)

def play_game():
    """
    Main game loop.
    """
    state = "start"
    player_stats = initialize_player()
    
    while state not in ["end_victory", "end_defeat", "end_arrest"]:
        display_state(state, player_stats)
        choice = get_player_choice(state)
        state, player_stats = update_state(state, choice, player_stats)
    
    display_state(state, player_stats)
    print(f"\nFinal Score: {player_stats[0]}")
    print("Game Over!")

if __name__ == "__main__":
    play_game()