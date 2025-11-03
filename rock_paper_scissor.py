import random
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissor": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}
# score variables
wins=0
lose=0
ties=0
while True:
    user_choice=input('Enter the choice rock,paper or scissor:\n').lower()
    if user_choice not in ['rock','paper','scissor']:
        print('Invalid input,Try again')
        continue
    computer_choice=random.choice(['rock','paper','scissor'])

    print(f"\n🧍 You chose:\n{ascii_art[user_choice]}")
    print(f"🤖 Computer chose:\n{ascii_art[computer_choice]}")

    if user_choice==computer_choice:
        print('Its a draw')
        ties+=1
    elif (user_choice=='rock' and computer_choice=='scissor') or \
         (user_choice=='paper' and computer_choice=='rock') or \
         (user_choice=='scissor' and computer_choice=='paper'):
        print('You win')
        wins+=1
    else:
        print('You lose')
        lose+=1

# show scores
    print(f'Scores: Wins = {wins}, Losses = {lose}, Ties = {ties}')

    play_again=input('Play again (yes or no)\n').lower()
    if play_again!='yes':
        print("\n🏁 Final Score:")
        print(f"✅ Wins: {wins}")
        print(f"❌ Losses: {lose}")
        print(f"⚖️ Ties: {ties}")
        print("Thanks for playing!")
        break
