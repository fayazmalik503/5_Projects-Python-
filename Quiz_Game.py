# Quiz Game
playing  = input("Do you want to play? ")

if playing.lower() != "yes":
    print('Good Bye!')
    quit()
print("okay! let's play: ")
score = 0

answer = input("What does CPU means ? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score  += 1

else:
    print("Answer is wrong!")

answer = input("When Pakistan get freedom ? ")
if answer == "1947":
    print('Correct!')
    score += 1

else:
    print("Answer is wrong!")

answer = input("what we smallest particle on earth ? ")
if answer.lower() == "atom":
    print('Correct!')
    score += 1

else:
    print("Answer is wrong!")

answer = input("what is color of Pakistan Flag ? ").lower()
if answer == "green":
    print('Correct!')
    score += 1

else:
    print("Answer is wrong!")


print("you got " + str(score) + " question correct!")
print("You got " + str((score/4)*100) + "%")
