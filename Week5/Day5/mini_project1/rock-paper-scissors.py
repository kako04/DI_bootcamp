from game import Game

def get_user_menu_choice():
    while True:
        choice = input("Please select an option:\n1. Play a new game\n2. Show scores\n3. Quit\n")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
            
def print_results(results):
    print("Thank you for playing! Here are the results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    
def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        else:
            print_results(results)
            break

if __name__ == '__main__':
    main()
