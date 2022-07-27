import random

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','V','b','n','m']

#print(random.choice(vowel))
#print(random.choice(consonant))

letters = 0
selection = []

while letters <= 9:
  choice = input('Press 1 for Vowel or 2 for Consonet... ')

  if choice == '1':
    turn = random.choice(vowel)
    print(turn)
    letters += 1
    selection.append(turn)
    print(selection)
  elif choice == '2':
    turn = random.choice(consonant)
    print(turn)
    letters += 1
    selection.append(turn)
    print(selection)
  else: 
    print('I did not reconise that input')

print(f'Your letters are:{selection}.')
print('end')