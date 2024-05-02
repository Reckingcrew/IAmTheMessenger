def game():
    
    #Starting Variables/imports
    import os
    import time 
    import random 
    gamename = "I Am The Messenger"
    inventory = []
    completed = []
    Diamond = True
    global maze_completed
    maze_completed = False
    people = 1
    duration = 0 
    family = False
    churchdone = False
    tries = 5

    #Game over
    def gamedone():
        clear()
        print("After all of your missions, your messages that you delivered. \n")
        time.sleep(3)
        print("You realize that while you have helped these people...\n")
        time.sleep(3)
        print("These people have also helped you.\n")
        while True:
            time.sleep(1000)

    #clear screen
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    #Actions
    def actions():   
        clear()
        print("Actions: \n\nGo 'direction' (travel north, south, east, or west) \n\nGet 'item' (add nearby item to your inventory) \n\nHelp 'Mission' (Any \033[1mbolded\033[0m idea that you might need to combat) \n\nMap: will display a small Map of the area\n\nActions: will result in this menu again\n\nType 'exit' at any time to reset\n")
    
    #Starting game
    def prompt():

        #Starting Info
        clear()
        print(f"\t\t{gamename}\n\n")
        print ("This is a text-based game where you navigate your city as Ed Kennedy.")
        input("Press enter to continue... \n")
        clear()

        #Continue?
        clear()
        
        #Intro info 
        print ("You are Ed Kennedy.\n")
        time.sleep(2.5)
        print ("You are a 19 year old cab driver in Australia.\n")
        time.sleep(2.5)
        print ("Your mother hates you.\n")
        time.sleep(2.5)
        print ("Your brother overshadows you.\n")
        time.sleep(2.5)
        
        #Audry info
        first_half = "The only person you love,"
        second_half = " doesn't love you back.\n"
        print(first_half, end='', flush=True)
        time.sleep(2.5)
        print(second_half)
        time.sleep(2.5)
        
        #Intro info cont
        print("You are bored, lonely, and lack potential and purpose...\n")
        time.sleep(3)
        input("Press enter to continue... \n")

        #Define actions 
        actions()
        input("Press enter to continue... \n")

    #rooms
    rooms = {
            'Ed\'s House' : {'South' : 'Milla\'s House', 'North' : 'The Thomas O\'Reilly Church', 'West' : 'The Tatapu Home', 'East' : 'The Bell Street Theatre', 'Item' : ['Ace of Diamonds', 'Ace of Clubs', 'Ace of Hearts', 'Ace of Spades']},
            'Milla\'s House' : {'North' : 'Ed\'s House', 'Mission': 'Loneliness'}, #Stop Milla from being so lonely
            'The Thomas O\'Reilly Church' : {'South' : 'Ed\'s House', 'Mission' : 'Community'}, #Bring people to the church, connect with brother
            'The Bell Street Theatre' : {'West': 'Ed\'s House', 'Mission' : 'Purpose'}, #Play a movie
            'The Tatapu Home' : {'East' : 'Ed\'s House', 'Mission' : 'Connection'}, #Put up the lights        
    }

    #Current Room 
    current_room = "Ed's House"

    #Result of Last Move
    msg = ""

    clear()
    prompt()

    #Gameplay Loop
    while True:
        clear()
        #Display Player Info
        print(f"You are in {current_room}\nInventory : {inventory}\nCompleted : {completed} \n----------------------")

        #Display Turn Message
        print(msg)
        
        #Item Indicator
        if current_room == "Ed's House":
            if 'Item' in rooms[current_room]:
                nearby_items = rooms[current_room]['Item']
                if isinstance(nearby_items, str):
                    nearby_items = [nearby_items]  # Convert single item to list for uniform handling
                for nearby_item in nearby_items:
                    if nearby_item not in inventory:
                        if nearby_item == "Ace of Diamonds" and Diamond == False:
                            continue
                        elif nearby_item == "Ace of Clubs" and "Loneliness" not in completed:
                            continue
                        elif nearby_item == "Ace of Hearts" and "Purpose" not in completed:
                            continue
                        elif nearby_item == "Ace of Spades" and "Connection" not in completed:
                            continue
                        else:
                            print(f"You see an {nearby_item}")
        else:
            pass
        
        #Mission Indicator
        if ((current_room == "Milla's House" and "Loneliness" in completed) or (current_room == "The Thomas O'Reilly Church" and "Brotherhood" in completed) or (current_room == "The Bell Street Theatre" and "Purpose" in completed) or (current_room == "The Tatapu Home" and "Connection" in completed)):
            pass
        else:
            if current_room == "Milla's House":
                if "Loneliness" not in completed:
                    print("You feel that the woman here, Milla, has a lot of \033[1mLoneliness\033[0m")
            elif current_room == "The Thomas O'Reilly Church":
                if "brotherhood" not in completed:
                    pass
                    #print("You talk to the pastor and want to help him with his \033[1mbrotherhood\033[0m") #NEEDS HELP URGET URGENT
                if "community" not in completed:
                    print("You feel that the church needs a better sense of \033[1mcommunity\033[0m")
            elif current_room == "The Bell Street Theatre":
                if "purpose" not in completed:
                    print ("It seems as though the man working here is lonely, he needs a sense of \033[1mpurpose\033[0m")
            elif current_room == "The Tatapu Home":
                if "connection" not in completed: 
                    print ("They seem happy, but they are missing something, a \033[1mconnection\033[0m that would perfect their christmas season.")
                    
        #Accept Players Move as Input
        user_input = input("Enter your Move:\n")

        #Split Moves
        next_move = user_input.split(' ')

       # First word is action
        action = next_move[0].title()
        if len(next_move) > 1: 
            item = next_move[1:]
            direction = next_move[1].title()
            mission = next_move[1:]

            item = ' '.join(item).title()
            mission = ' '.join(mission).title()
        else: 
            msg = ("Invalid Command")
        # Moving between Rooms
        if action == "Go": 
            try:
                # Capitalize the direction input before accessing the dictionary
                direction = direction.capitalize()
                to_go = rooms[current_room][direction]
                if to_go == "Milla's House" and "Ace of Diamonds" not in inventory:
                    msg = "You do not have access to this location"
                elif to_go == "The Bell Street Theatre" and "Ace of Clubs" not in inventory:
                    msg = "You do not have access to this location"
                elif to_go == "The Tatapu Home" and "Ace of Hearts" not in inventory:
                    msg = "You do not have access to this location"
                elif to_go == "The Thomas O'Reilly Church" and "Ace of Spades" not in inventory:
                    msg = "You do not have access to this location"
                else: 
                    msg = f"You travel {direction}"
                    current_room = to_go
                    to_go = ""
            except KeyError:  # Handle the case where the direction key is not found
                msg = "You may not travel that direction"

        # Picking up items
        elif action == "Get": 
            if (current_room == "Ed's House" and "Loneliness" not in completed) or \
                (current_room == "Ed's House" and "Brotherhood" not in completed) or \
                (current_room == "Ed's House" and "Connection" not in completed): 
                try:
                    for room, details in rooms.items():
                        if "Ace of Diamonds" in details['Item'] and "Ace of Diamonds" not in inventory:
                            inventory.append("Ace of Diamonds")
                            msg = ("Ace of Diamonds has been added to your inventory")
                            break  # Stop the loop after adding the item to the inventory
                        elif "Ace of Clubs" in details['Item'] and "Ace of Clubs" not in inventory:
                            inventory.append("Ace of Clubs")
                            msg = ("Ace of Clubs has been added to your inventory")
                            break  # Stop the loop after adding the item to the inventory
                        elif "Ace of Hearts" in details['Item'] and "Ace of Hearts" not in inventory:
                            inventory.append("Ace of Hearts")
                            msg = ("Ace of Hearts has been added to your inventory")
                            break  # Stop the loop after adding the item to the inventory
                        elif "Ace of Spades" in details['Item'] and "Ace of Spades" not in inventory:
                            inventory.append("Ace of Spades")
                            msg = ("Ace of Spades has been added to your inventory")
                            break  # Stop the loop after adding the item to the inventory
                    else:
                        print(f"Ace of Diamonds not found in the room")
                except KeyError: 
                    print("KeyError: 'Item' key not found in room details")
                except Exception as e: 
                    print("An error occurred:", e)
            else: 
                msg = f"Can't find {item}"
            
        #Completing Missions
        elif action == "Help":
            try:
                if mission == rooms[current_room]["Mission"]:
                    if mission not in completed:
                        #Missions
                        if current_room == "Milla's House": #Milla's house mission (tic tac toe)
                            clear()
                            print("Milla would like to play Tic-Tac-Toe with you.\n")
                            input("Press enter to continue...\n")

                            # Tic Tac Toe game against the computer with basic strategy

                            # Initialize the board
                            board = [' ' for _ in range(9)]

                            # Variable to keep track of the current player
                            current_player = 'X'


                            # Function to print the board
                            def print_board():
                                row1 = '|'.join(board[0:3])
                                row2 = '|'.join(board[3:6])
                                row3 = '|'.join(board[6:9])
                                clear()
                                print(row1)
                                print('-' * 5)
                                print(row2)
                                print('-' * 5)
                                print(row3)

                            # Function to check if a player has won
                            def check_win(player):
                                # Check rows
                                for i in range(0, 9, 3):
                                    if board[i] == board[i + 1] == board[i + 2] == player:
                                        return True
                                # Check columns
                                for i in range(3):
                                    if board[i] == board[i + 3] == board[i + 6] == player:
                                        return True
                                # Check diagonals
                                if board[0] == board[4] == board[8] == player:
                                    return True
                                if board[2] == board[4] == board[6] == player:
                                    return True
                                return False

                            # Function to make a smart move for the computer
                            def computer_move():
                                # Check if computer can win
                                for i in range(9):
                                    if board[i] == ' ':
                                        board[i] = 'O'
                                        if check_win('O'):
                                            return
                                        board[i] = ' '  # Undo the move
                                
                                # Check if player can win and block
                                for i in range(9):
                                    if board[i] == ' ':
                                        board[i] = 'X'
                                        if check_win('X'):
                                            board[i] = 'O'
                                            return
                                        board[i] = ' '  # Undo the move
                                
                                # If no winning moves, make a random move
                                empty_positions = [i for i in range(9) if board[i] == ' ']
                                position = random.choice(empty_positions)
                                board[position] = 'O'

                            # Main game loop
                            while True:
                                print_board()
                                
                                if current_player == 'X':
                                    position = int(input(f"Choose a position (1-9): ")) - 1
                                    if board[position] == ' ':
                                        board[position] = current_player
                                        if check_win(current_player):
                                            print_board()
                                            print("You won and helped Milla with her Loneliness!\n")
                                            print("By helping her with her Loneliness, you also realize that you are no longer as lonely yourself.\n")
                                            input("Press enter to continue...\n")
                                            msg = ("You successfully helped Milla with her Loneliness!")
                                            completed.append("Loneliness")
                                            break
                                        if ' ' not in board:
                                            print_board()
                                            print("You tied and helped Milla with her Loneliness!\n")
                                            print("By helping her with her Loneliness, you also realize that you are no longer as lonely yourself.\n")
                                            msg = ("You successfully helped Milla with her Loneliness!")
                                            completed.append("Loneliness")
                                            input("Press enter to continue...\n")
                                            break
                                        current_player = 'O'
                                    else:
                                        print("That position is already taken. Please choose another one.")
                                else:
                                    # Computer's turn
                                    computer_move()
                                    if check_win('O'):
                                        print_board()
                                        print("You lost... but, you helped Milla with her Loneliness!\n")
                                        print("By helping her with her Loneliness, you also realize that you are no longer as lonely yourself.\n") 
                                        input("Press enter to continue...\n")
                                        msg = ("You successfully helped Milla with her Loneliness!")
                                        completed.append("Loneliness")
                                        break
                                    if ' ' not in board:
                                        print_board()
                                        print("You tied and helped Milla with her Loneliness!\n")
                                        print("By helping her with her Loneliness, you also realize that you are no longer as lonely yourself.\n")
                                        input("Press enter to continue...\n")
                                        msg = ("You successfully helped Milla with her Loneliness!")
                                        completed.append("Loneliness")                                 
                                        break
                                    current_player = 'X'
                                    clear()
                        elif current_room == "The Bell Street Theatre": #Theatre Mission (Maze)
                            def mazegame():
                                if "Purpose" not in completed:
                                    clear()
                                    print("You give him a sense of purpose by having him play you a movie.\n")
                                    print("Navigate your player (P) to the theatre (E) to watch the movie.\n")
                                    input("Press enter to continue...\n")
                                    # Define constants for maze dimensions
                                    WIDTH = 8
                                    HEIGHT = 8

                                    # Define symbols for player, walls, exit, and clear spaces
                                    PLAYER_SYMBOL = 'P'
                                    WALL_SYMBOL = '#'
                                    EXIT_SYMBOL = 'E'
                                    CLEAR_SYMBOL = ' '

                                    # Initialize maze with walls
                                    maze = [[WALL_SYMBOL] * WIDTH for _ in range(HEIGHT)]

                                    # Initialize player position
                                    player_x = random.randint(0, WIDTH - 1)
                                    player_y = random.randint(0, HEIGHT - 1)

                                    # Carve out the maze using modified DFS and randomized Prim's algorithm
                                    def generate_maze():
                                        stack = [(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))]
                                        visited = set(stack)
                                        while stack:
                                            x, y = stack[-1]
                                            neighbors = []
                                            for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                                                nx, ny = x + dx, y + dy
                                                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and (nx, ny) not in visited:
                                                    neighbors.append((nx, ny))
                                            if neighbors:
                                                nx, ny = random.choice(neighbors)
                                                mx, my = (x + nx) // 2, (y + ny) // 2
                                                maze[my][mx] = CLEAR_SYMBOL
                                                maze[ny][nx] = CLEAR_SYMBOL
                                                visited.add((nx, ny))
                                                stack.append((nx, ny))
                                            else:
                                                stack.pop()

                                        # Place the exit in the maze
                                        exit_x, exit_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
                                        while maze[exit_y][exit_x] != CLEAR_SYMBOL:
                                            exit_x, exit_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
                                        maze[exit_y][exit_x] = EXIT_SYMBOL

                                    # Print the maze with player position
                                    def print_maze():
                                        for y in range(HEIGHT):
                                            for x in range(WIDTH):
                                                if x == player_x and y == player_y:
                                                    print(PLAYER_SYMBOL, end=' ')
                                                else:
                                                    print(maze[y][x], end=' ')
                                            print()

                                    # Move the player
                                    def move_player(dx, dy):
                                        nonlocal player_x, player_y
                                        new_x = player_x + dx
                                        new_y = player_y + dy
                                        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and maze[new_y][new_x] != WALL_SYMBOL:
                                            player_x = new_x
                                            player_y = new_y
                                            if maze[player_y][player_x] == EXIT_SYMBOL:
                                                clear()
                                                print("Congratulations! You've found the theatre!")
                                                print("While giving the map a sense of purpose, you realize that you have given yourself a sense of purpose; Both by helping him, and by helping Milla.")
                                                input("Press enter to continue...\n")
                                                return True
                                        return False

                                    generate_maze()
                                    while True:
                                        clear()
                                        print_maze()
                                        print("Use WASD keys to move. 'q' to quit.")
                                        command = input("Enter your move: ").lower()
                                        if command == 'q':
                                            print("Goodbye!")
                                            return False
                                        elif command in ['w', 'a', 's', 'd']:
                                            dx, dy = 0, 0
                                            if command == 'w':
                                                dy = -1
                                            elif command == 'a':
                                                dx = -1
                                            elif command == 's':
                                                dy = 1
                                            elif command == 'd':
                                                dx = 1
                                            if move_player(dx, dy):
                                                completed.append("Purpose")
                                                return True
                                        else:
                                            print("Invalid command! Use WASD to move or 'q' to quit.")
                                else:
                                    return False

                            # Inside the game loop
                            if mazegame():
                                msg = "You have given the man a sense of purpose."
                            else:
                                msg = "You have given the man a sense of purpose."

                            mazegame()
                        elif current_room == "The Tatapu Home":
                            clear()

                            # Function to create the board with random values
                            def create_board():
                                values = [f'\033[94mBlue\033[0m  ', f'\033[91mRed\033[0m   ', f'\033[92mGreen\033[0m ', f'\033[93mYellow\033[0m']
                                values = values * 2  # Duplicate each letter
                                random.shuffle(values)
                                board = [values[:4], values[4:]]
                                return board

                            # Function to display the board
                            def display_board(board, revealed):
                                clear()
                                print("Matching Game")
                                print("-------------")
                                for i in range(2):
                                    for j in range(4):
                                        if revealed[i][j]:
                                            print(board[i][j], end=' ')
                                        else:
                                            print("#     ", end=' ')
                                    print()

                            # Function to check if the game is over
                            def is_game_over(revealed):
                                for i in range(2):
                                    for j in range(4):
                                        if not revealed[i][j]:
                                            return False
                                return True

                            # Function to check if two selected positions contain the same value
                            def check_match(board, positions):
                                x1, y1 = positions[0]
                                x2, y2 = positions[1]
                                return board[x1][y1] == board[x2][y2]

                            # Function to run the game
                            def run_game():
                                
                                print("You see the family's christmas lights and decide they look too old.\n")
                                print("You know that the order of colors is very important so you decide that you will maintain it for them.\n")
                                print("Learn and match the colors together to keep the pattern the same.\n")
                                input("Press enter to continue...\n")

                                board = create_board()
                                revealed = [[False] * 4, [False] * 4]
                                pairs_found = 0

                                while not is_game_over(revealed):
                                    display_board(board, revealed)

                                    # Get input for the first card
                                    print("Enter the number of the first card you will try (1-8):")
                                    while True:
                                        num1 = input()
                                        if num1.isdigit() and 1 <= int(num1) <= 8:
                                            break
                                        else:
                                            print("Invalid input! Please enter a number between 1 and 8.")
                                    num1 = int(num1) - 1
                                    x1, y1 = num1 // 4, num1 % 4

                                    # Check if the position is valid
                                    if revealed[x1][y1]:
                                        print("Card already flipped!")
                                        time.sleep(1)
                                        continue

                                    revealed[x1][y1] = True
                                    display_board(board, revealed)

                                    # Get input for the second card
                                    print("Enter the number of the second card you will try (1-8):")
                                    while True:
                                        num2 = input()
                                        if num2.isdigit() and 1 <= int(num2) <= 8:
                                            break
                                        else:
                                            print("Invalid input! Please enter a number between 1 and 8.")
                                    num2 = int(num2) - 1
                                    x2, y2 = num2 // 4, num2 % 4

                                    # Check if the position is valid
                                    if revealed[x2][y2]:
                                        print("Card already flipped!")
                                        time.sleep(1)
                                        revealed[x1][y1] = False  # Flip the first card back
                                        continue

                                    revealed[x2][y2] = True
                                    display_board(board, revealed)

                                    # Check if the cards match
                                    if check_match(board, [(x1, y1), (x2, y2)]):
                                        print("Congratulations! You found a pair!")
                                        pairs_found += 1
                                        time.sleep(1)
                                    else:
                                        print("Sorry, no match. Flipping cards back...")
                                        time.sleep(3)
                                        revealed[x1][y1] = False
                                        revealed[x2][y2] = False

                                print("Congratulations! You found all the pairs!")
                                clear()
                                print("After putting up the lights you see the Family drive in and notice them, you silently realize that you made a small difference in their lives.")
                                print("While forming the connection in their lives, you realize the differce you made in your own life.")
                                completed.append("Connection")
                                msg = "You have formed a connection in the Tatapu Family" #Why isn't this line working. 
                            run_game()
                        elif current_room == "The Thomas O\'Reilly Church":
                            def churchgame():
                                def fill_bar(duration):
                                    start_time = time.time()
                                    end_time = start_time + duration
                                    bar_length = 20

                                    while time.time() < end_time:
                                        elapsed_time = time.time() - start_time
                                        progress = elapsed_time / duration
                                        filled_length = int(progress * bar_length)
                                        bar = '█' * filled_length + '-' * (bar_length - filled_length)
                                        progress_str = f"Progress: [{bar}] {int(progress * 100)}%"
                                        print(progress_str, end='\r')  # Print progress bar with carriage return
                                        time.sleep(0.1)  # Adjust the sleep time for smoother animation

                                    # After the loop completes, explicitly print 100%
                                    print(f"Progress: [{'█' * bar_length}] 100%")

                                people = 1
                                tries = 5
                                clear()
                                print("In order to help the church get a better community, you decide to try to get people to come to this week's service.\n")
                                input("Press enter to continue...\n")

                                family = False
                                churchdone = False

                                def churchinfo():
                                    clear()
                                    print("You have 5 days to get enough people to come to the service, each option listed below takes 1 day.\n")
                                    print("If you take more than 5 days, you have to restart. ")
                                    print("To help attract people you have 5 options:\n")
                                    print("1: Poster: \n• Requires 1 person \n• Gains 1 attendee\n• Takes 3 Seconds\n")
                                    print("2: Social Media Post: \n• Requires 3 people \n• Gains 5 attendees\n• Takes 5 Seconds\n")
                                    print("3: Invite Friends and Family: \n• Requires self \n• Gains 10 attendees\n• Takes 8 Seconds\n")
                                    print("4: Print Banners: \n• Requires 10 people \n• Gains 10 attendees\n• Takes 6 Seconds\n")
                                    print("5: Spray Paint Advertisment on the Road: \n• Requires 50 people \n• Gains 50 attendees\n• Takes 20 Seconds\n")
                                    print("6: Go back to this screen.\n")
                                churchinfo()

                                while not churchdone:
                                    if people == 1:
                                        print(f"You have: {people} person")
                                    else:
                                        print(f"You have: {people} people")
                                    
                                    #people over 100
                                    if people >= 100:
                                        churchdone = True
                                        completed.append("Community")
                                        clear()
                                        print("You have found enough people for the service this Sunday\n")
                                        print("During the process of working to create a community, you see yourself become more and more of a community-minded person.\n")
                                        input("Press any key to continue...\n")
                                        gamedone()
                                        clear()
                                        break
                                    if tries <= 0:
                                        clear()
                                        print("You have run out of time.\n")
                                        input("Press enter to continue...\n")
                                        churchgame()
                                    get_people = input("Input the number that corresponds with the option that you choose: \n")

                                    try:
                                        get_people = int(get_people)
                                    except ValueError:
                                        print("Invalid input! Please enter a number.")
                                        continue

                                    if people >= 0:
                                        clear()

                                    # Poster
                                    if get_people == 1:
                                        print("You choose to make a poster.")
                                        duration = 3
                                        fill_bar(duration)
                                        people += 1
                                        tries -= 1

                                    # Social Media Post
                                    elif get_people == 2:
                                        if people >= 3:
                                            print("You choose to post on Social Media.")
                                            duration = 5
                                            fill_bar(duration)
                                            people += 5
                                            tries -= 1
                                        else:
                                            print("You do not have enough people for this choice.")

                                    # Friends And Family
                                    elif get_people == 3:
                                        if not family:
                                            print("You choose to invite your friends and family.")
                                            duration = 8
                                            fill_bar(duration)
                                            people += 10
                                            family = True
                                            tries -= 1
                                        else:
                                            print("You have already invited your friends and family.")

                                    # Banners
                                    elif get_people == 4:
                                        if people >= 10:
                                            print("You choose to print a banner.")
                                            duration = 6
                                            fill_bar(duration)
                                            people += 10
                                            tries -= 1
                                        else:
                                            print("You do not have enough people for this choice.")

                                    # Paint Road
                                    elif get_people == 5:
                                        if people >= 50:
                                            print("You choose to vandalize the street.")
                                            duration = 15
                                            fill_bar(duration)
                                            people += 50
                                            tries -= 1
                                        else:
                                            print("You do not have enough people for this choice.")

                                    elif get_people == 6:
                                        churchinfo()

                                    else:
                                        print("That is not an option")
                            churchgame()
                        else: 
                            msg = "Bug with missions, name of location not consistant"

                elif mission == "Loneliness" or mission == "Brotherhood" or mission == "Purpose" or mission == "Connection":
                    msg = f"You have already completed this message"
                else: 
                    msg = f"That is not an option"
            except: 
                msg = f""

        #Display Actions
        elif action == "Actions":
            actions()
            input("Press enter to continue...\n")

        #Display Map
        elif action == "Map":
            clear()
            print ("""


                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@
                                   @                           @
                                   @                           @
                                   @        The Thomas         @
                                   @      O'Reilly Church      @
                                   @                           @
                                    @                         @
                                     @@@@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @                          @     @                           @    @                           @
  @                          @     @                           @    @                           @
  @     The Tatapu Home      @     @         Ed's House        @    @      The Bell Street      @
  @                          @     @                           @    @          Theatre          @
  @                          @     @                           @    @                           @
   @                        @       @                         @      @                         @
    @@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@
            N                      @                           @
            |                      @                           @
       W----+----E                 @        Milla's House      @
            |                      @                           @
            S                       @                         @
                                     @@@@@@@@@@@@@@@@@@@@@@@@@


""")
            input("Press enter to continue...\n")

        #exit 
        elif action == "Exit": 
            game()

        #Invalid Commands 
        else: 
            msg = "Invalid Command"
game()