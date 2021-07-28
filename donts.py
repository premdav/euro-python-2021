'''
change casing of every other letter in string => hello -> HeLlO
'''

# starting point
def myFunc(a):
  empty = []
  for i in range(len(a)):
    if i % 2 == 0:
      empty.append(a[i].upper())
    else:
      empty.append(a[i].lower())
  return ''.join(empty)

# naming matters -> naming changes
# enumerate me -> for loop gives us access to both index and value
# nest sparingly -> since we have to append regardless, we bring the append outside of the nested if else statements
# truthy, falsy, bool -> we do not need to check agains the value of 0, which is falsy for the mod operator
#       the expression will either have a truthy or falsy value to begin with
# conditional expressions 
# def altCasing(text):
#   letters = []
#   for idx, char in enumerate(text):
#     if idx % 2:
#       character = char.lower()
#     else:
#       character = char.upper()
#     letters.append(character)
#   return ''.join(letters)

def altCasing(text):
  letters = []
  for idx, char in enumerate(text):
    letters.append(
      char.lower() if idx % 2 else char.upper()
    )
  return ''.join(letters)

# list comprehension
def alertnate_casing(text):
  return ''.join([
    char.lower() if idx % 2 else char.upper()
    for idx, char in enumerate(text)
  ])


print(myFunc('preston'))
print(altCasing('preston'))
print(alertnate_casing('preston'))
