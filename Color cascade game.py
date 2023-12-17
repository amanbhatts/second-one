import random

def color_cascade_game():
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    score = 0
    target_color = random.choice(colors)

    print("Welcome to the Color Cascade Game!")
    print("Match the falling blocks with the target color.")
    print("Change the target color quickly to keep scoring!")

    while True:
        print(f"\nTarget Color: {target_color}")
        user_input = (input("Enter the color of the falling block: ").lower()
                      .strip())

        if user_input == 'quit':
            print(f"Game over! Your final score is {score}.")
            break

        if user_input == target_color:
            print("Correct! +1 point")
            score += 1
            target_color = random.choice(colors)
        else:
            print("Wrong! Game over. Your final score is", score)
            break

if __name__ == "__main__":
    color_cascade_game()
