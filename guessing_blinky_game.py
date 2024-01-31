import time
import board
import neopixel
from random import randint

def turn_green(pixels):
    pixels.fill((0, 255, 0))
    time.sleep(1)

def turn_blue(pixels):
    pixels.fill((0, 0, 255))
    time.sleep(1)

def turn_red(pixels):
    pixels.fill((255, 0, 0))
    time.sleep(1)

def main():
    print("Starting Code Challenge")

    pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

    user_number = int(input("Enter an integer number from 1-10 > "))

    if 1 <= user_number <= 10:
        print(f'Your number {user_number} is a valid Integer from 1-10. Thanks')
    else:
        print('Invalid input. Please enter a number between 1 and 10.')
        return

    turn_green(pixels)

    count = 1
    while count <= 5:
        print(f"Starting Guess #{count}")

        computer_guess = randint(1, 10)
        print(f"I guessed {computer_guess}")

        if computer_guess == user_number:

            turn_blue(pixels)
            print(f'I Win, I guessed your number in {count} tries')
            break  
        else:
     
            turn_red(pixels)
            count += 1  

    if count > 5:
        print(f'You Win, I did not guess your number in {count} tries')

    print("Ending Code Challenge")

if __name__ == "__main__":
    main()
