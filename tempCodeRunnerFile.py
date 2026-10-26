#word guesser
import random

word_bank = [
    ("commit", "I forgot to add my changes before writing a git ____ message."),
    ("branch", "Let's create a new feature ____ so we don't break the main code."),
    ("merge", "There are thirty conflicting files in this pull request, good luck trying to ____ them."),
    ("cache", "Have you tried clearing your browser ____ before reporting the bug?"),
    ("script", "Instead of doing it manually three hundred times, I wrote a quick Python ____."),
    ("legacy", "Nobody knows how this old system works, it's pure undocumented ____ code."),
    ("refactor", "Don't add new features yet, we really need to ____ this messy function first."),
    ("stack", "My entire technical ____ consists of JavaScript, coffee, and sheer willpower."),
    ("hotfix", "We pushed a major ____ to production on a Friday night, what could possibly go wrong?"),
    ("agile", "We call our process ____, which mostly means we have twice as many meetings."),
    ("firewall", "The security team locked everything down behind a strict corporate ____."),
    ("cookie", "Accept every single tracking ____ or the website refuses to load."),
]
#the word bank where every word with its hint is stored
print("~" * 40)
print()
print("   Welcome to Jargon Jumble!")
print("   A Tech-Themed Word Scramble Game")
print()
print("~" * 40)
try:
  ROUNDS = int(input("Enter the number of rounds (for eg: 12) \n"))
except(ValueError):
  print("Enter a valid number!")

round_num = 1
score = 0
used = []

while round_num <= ROUNDS:
  
  word, hint = random.choice(word_bank)

  while (word, hint) in used:
    word, hint = random.choice(word_bank)

  used.append((word, hint))

  letters = list(word)
  random.shuffle(letters)
  scrambled_word = "".join(letters).upper()

  print()
  print(f"Round {round_num}")
  print()
  print(f"Scrambled: {scrambled_word}")
  print()

  guess = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()

  if guess == "hint":
    print()
    print(f"Hint: {hint}")
    print()
    guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()

  if guess == "quit":
    print("Thanks for playing!")
    break
  elif guess == "skip":
    print(f"Skipped! The word was '{word}'.")
  elif guess == word:
    score += 1
    print("✅  Correct!")
  else:
    print(f"❌ Sorry, the word was '{word}'.")

  round_num += 1

print()
print(f"Final score: {score}/{ROUNDS}")
print()
#converts the score into percentage for easier printing
if ROUNDS > 0:
    percentage = (score / ROUNDS) * 100
else:
    percentage = 0
if percentage == 100:
    print("Flawless! All tests passing, zero bugs.")
elif percentage >= 75:
    print("Near perfect, only one failing test!")
elif percentage >= 50:
    print("Good effort! The code runs, and that's what counts.")
elif percentage >= 25:
    print("Nice one! some practice and improvement is inevitable")
else: 
    print("Have you tried turning it off and on again?")


#this format of score can be used for pre determined rounds if the round is determined by user the above suits better
# if score == ROUNDS:
#   print("Flawless! All tests passing, zero bugs.")
# elif score == 4: 
#   print("Near perfect, only one failing test!")
# elif score == 3:
#   print("Good effort! The code runs, and that's what counts.")
# else: 
#   print("Have you tried turning it off and on again?")