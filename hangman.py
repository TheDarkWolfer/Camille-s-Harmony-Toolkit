PLUGIN_METADATA = {
    'name': 'Hangman',
    'version': '1.0',
    'author': 'Camille.Is_Me',
    'description': 'A plugin to play the hangman game in the terminal.',
    'dependencies':['nltk','random', 'math']
}

def info():
    """
    Returns information about the plugin.
    """
    return PLUGIN_METADATA

def register_args(parser):
    """
    Register arguments for the hangman plugin.
    """
    parser.add_argument('--hangman', help='Starts a game of Hangman', action="store_true")

def execute(args):
    """
    Execute the hangman game (that sounds off...).
    """

    import random
    import nltk
    import math

    if args.hangman:

        nltk.download("words")

        word_list = nltk.corpus.words.words()

        pick = ""

        while len(pick) < 4 or len(pick) > 10:
            pick = random.choice(word_list)

        solution = list((pick).upper())
        solution_line = ["_ "] * len(solution)
        failed_tries = []

        RED = '\033[31m'
        GREEN = '\033[32m'
        RESET = '\033[0m'
        BOLD = '\033[1m'

        parts = 0
        hints = round(math.ceil(len(pick)/4))-1

        while True:

            board = [
        [f" ",f" ",f" ",f" ",f" ",f" ",f" "],
        [f" ",f" ",f"{'╋' if parts >= 3 else '┃' if parts >= 2 else ' '}",f"{'━' if parts >= 3 else ' '}",f"{'━' if parts >= 3 else ' '}",f"{'┯' if parts >= 4 else '━' if parts == 3 else ' '}",f" "],
        [f" ",f" ",f"{'┃' if parts >= 2 else ' '}",f" ",f" ",f"{'O' if parts >= 4 else ' '}",f" "],
        [f" ",f" ",f"{'┃' if parts >= 2 else ' '}",f" ",f"{'╱' if parts >= 6 else ' '}",f"{'|' if parts >= 5 else ' '}",f"{'╲' if parts >= 7 else ' '}"],
        [f" ",f" ",f"{'┃' if parts >= 2 else ' '}",f" ",f" ",f"{'|' if parts >= 8 else ' '}",f" "],
        [f" ",f" ",f"{'┃' if parts >= 2 else ' '}",f" ",f"{'╱' if parts >= 9 else ' '}",f" ",f"{'╲' if parts >= 10 else ' '}"],
        [f" ",f"{'━' if parts >= 1 else ' '}",f"{'━' if parts == 1 else '┻' if parts >= 2 else ' '}",f"{'━' if parts >= 1 else ' '}",f"{'━' if parts >= 1 else ' '}",f"{'━' if parts >= 1 else ' '}",f" "]
                ]
            
            #print(f"DEBUG: {solution} | {parts}")

            if parts == 11:
                print("You lost!")
                print("The word was: " + "".join(solution))
                break

            if "_ " not in solution_line:

                print(f" You won ! The word was : {GREEN}{BOLD}{''.join(solution)}{RESET} ")
                for j in failed_tries:
                    print(f"{RED}{BOLD}{j}{RESET}", end=" ")

                for x in range(len(board)):
                    print("".join(board[x]))

                break

            for i in solution_line:
                if i == "_ ":
                    print("".join(f"{RED}{BOLD}{'_ '}{RESET}"), end="")
                else:
                    print("".join(f"{GREEN}{BOLD}{i}{RESET}"), end="")

            print("\n")

            for j in failed_tries:
                print(f"{RED}{BOLD}{j}{RESET}", end=" ")

            for x in range(len(board)):
                print("".join(board[x]))

            print("\n")

            guess = input(f"Guess a letter{',' if hints > 0 else ' or '}the whole word{f', or {GREEN}@{RESET} for a hint ({hints} remaining)' if hints > 0 else ' '}: ").upper()

            if guess == "@":
                
                hints -= 1
                hint_pick = random.choice(solution)
                
                while (hint_pick in failed_tries) or (hint_pick+" " in solution_line):
                    hint_pick = random.choice(solution)

                guess = hint_pick

            if guess in solution:

                print(f"Correct! {GREEN}{BOLD}{guess}{RESET} is in the word!")

                for i in range(len(solution)):
                    if solution[i] == guess:
                        solution_line[i] = guess+" "

            elif len(guess) > 1:
    
                    if guess == "".join(solution):
                        print(f" You won ! The word was : {GREEN}{BOLD}{''.join(solution)}{RESET} ")
                        for j in failed_tries:
                            print(f"{RED}{BOLD}{j}{RESET}", end=" ")
    
                        for x in range(len(board)):
                            print("".join(board[x]))
    
                        break
    
                    else:
                        print(f"{RED}{BOLD}{guess}{RESET} is not the word!")    
                        parts += 1


            elif guess in failed_tries:
                    
                    print(f"You already tried {RED}{BOLD}{guess}{RESET}!")

            else:
                parts += 1
                failed_tries.append(guess)

            for i in range(25):
                print("\n")