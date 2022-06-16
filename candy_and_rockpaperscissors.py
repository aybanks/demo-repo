# Candy Number Guessing 

response1 = int(input("How many pieces are left if the candy is evenly divided among 5 people : "))
response2 = int(input("How many pieces are left if the candy is evenly divided among 6 people : "))
response3 = int(input("How many pieces are left if the candy is evenly divided among 7 people : "))
print()

if response1 == 2 and response2 == 3 and response3 == 2:
    print("You've won the candies")
else:
    print("You've lost the candies")
print()

for i in range(1, 200):
    if i%5 == 2 and i%6 == 3 and i%7 == 2:
        print("The number of candies is", i)

#Rock Paper Scissors
import random

player_count, comp_count = 0, 0
rps = ["rock", "paper", "scissors"]
for i in range(5):
	response = input("Rock Paper Scissors : ")
	computer = rps[random.randint(0, 2)]
	if computer == response:
		print("Tie!")
	elif (computer == 'paper' and response == 'rock') or (computer == 'rock' and response == 'scissors') or (computer == "scissors" and response == "paper"):
		comp_count += 1
		print(f"Computer wins this round picking {computer}")
	else:
		player_count += 1
		print(f"You win this round against {computer}")
	print()
print(f"The computer's score is {comp_count}")
print(f"Your score is {player_count}")
print()
if comp_count > player_count:
	print("Computer won!")
elif comp_count == player_count:
	print("It's a tie!")
else:
	print("You won!")
