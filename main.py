firstName = str(input("First Name: "))
lastName = str(input('Last Name: '))

print("\nYour initial is " + firstName[0] + lastName[0])

score = 0

if len(firstName) > 5:
  score += 3
else:
  score += 5

if len(lastName) > 5:
  score += 3
else:
  score +=5

print("\nYour name has score " + str(score) + " points!")