import random

walls = {
    (1, 1): ['e', 's'],
    (2, 1): ['w', 'e'],
    (3, 1): ['w'],
    (1, 2): ['e'],
    (2, 2): ['w', 'e', 's'],
    (3, 2): ['w', 's'],
    (1, 3): ['e', 's'],
    (2, 3): ['w', 's'],
}

def is_valid_move(position, direction):
    if direction in walls.get(position, []):
        return False
    x, y = position
    if direction == 'n' and y < 3: return True
    if direction == 's' and y > 1: return True
    if direction == 'e' and x < 3: return True
    if direction == 'w' and x > 1: return True
    return False

def initialize_levers():
    levers = set()
    while len(levers) < 4:  
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if (x, y) not in [(1, 1), (3, 1)]:  
            levers.add((x, y))
    return levers



def move_player(position, direction):
    if direction == 'n': return (position[0], position[1] + 1)
    if direction == 's': return (position[0], position[1] - 1)
    if direction == 'e': return (position[0] + 1, position[1])
    if direction == 'w': return (position[0] - 1, position[1])
    return position

def has_lever(position):
    return position in [(1, 2), (2, 2), (2, 3), (3, 3)]

def pull_lever(coins):
    print("You see a lever.")
    if input("PULL LEVER? (y/n): ").lower() == 'y':
        coins += 1
        print("You received a gold coin!")
    return coins



def main():
    position = (1, 1)  
    coins = 0  
    levers = initialize_levers()  
    used_levers = set() 
    while position != (3, 1):
        print(f"You are at {position}. You have {coins} gold coins.")
        available_directions = ['n', 's', 'e', 'w']
        walls_here = walls.get(position, [])
        
        valid_directions = [d for d in available_directions if d not in walls_here]
        print(f"Available directions: {', '.join(valid_directions).upper()}")
        
        direction = input("Choose a direction (n/e/s/w): ").lower()

        if direction in valid_directions and is_valid_move(position, direction):
            position = move_player(position, direction)
            if position in levers and position not in used_levers:
                coins = pull_lever(coins)
                used_levers.add(position)
        else:
            print("Not a valid direction!")

    print(f"Congratulations! You've reached the victory tile with {coins} gold coins!")

if __name__ == "__main__":
    main()

