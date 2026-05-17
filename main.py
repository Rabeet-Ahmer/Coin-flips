import random

def simulate_coin_flips(num_flips):
    """Simulates flipping a coin num_flips times."""
    heads = 0
    tails = 0
    
    for _ in range(num_flips):
        result = random.choice(['Heads', 'Tails'])
        if result == 'Heads':
            heads += 1
        else:
            tails += 1
            
    return heads, tails

def main():
    print("--- Coin Flip Probability Simulator ---")
    print("This program tests the theory that flipping a coin many times results in a 50-50 distribution.\n")
    
    try:
        user_input = input("Enter the number of times you want to flip the coin: ")
        num_flips = int(user_input)
        
        if num_flips <= 0:
            print("Please enter a positive integer.")
            return

        print(f"\nFlipping the coin {num_flips} times...")
        heads, tails = simulate_coin_flips(num_flips)
        
        heads_percent = (heads / num_flips) * 100
        tails_percent = (tails / num_flips) * 100
        
        print("\n--- Results ---")
        print(f"Heads: {heads} ({heads_percent:.2f}%)")
        print(f"Tails: {tails} ({tails_percent:.2f}%)")
        print(f"Total: {num_flips}")
        
        diff = abs(heads_percent - 50)
        print(f"\nDifference from 50-50: {diff:.2f}%")
        
        if diff < 5:
            print("The results are quite close to the 50-50 theory!")
        else:
            print("The results deviate slightly from the 50-50 theory, which can happen with smaller samples or random chance.")

    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

if __name__ == "__main__":
    main()
