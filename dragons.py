# add an element with append()
# add several elements with extend()
# remove elements with remove()
# insert an element at a specified position with insert()
# check if an element is in a list or not with the in and not in operators
# count how many times an element occurs in a list with count()
# get the position of an element in a list with index().

dragons = []  # we do not have dragons yet

dragons.append('Rudror')
dragons.append('Targiss')
dragons.append('Coporth')

print(dragons)

dragons.remove('Targiss')
print(dragons)  # ['Rudror', 'Coporth']

dragons = ['Rudror', 'Targiss', 'Coporth', 'Targiss']
dragons.remove('Targiss') # Only removes first occurrence
print(dragons)  # ['Rudror', 'Coporth', 'Targiss']

dragons = ['Rudror', 'Targiss', 'Coporth']
del dragons[1]
print(dragons)  # ['Rudror', 'Coporth']

dragons = ['Rudror', 'Targiss', 'Coporth']
last_dragon = dragons.pop()
print(last_dragon)  # 'Coporth'
print(dragons)      # ['Rudror', 'Targiss']

dragons = ['Rudror', 'Targiss', 'Coporth']
first_dragon = dragons.pop(0)
print(first_dragon)  # 'Rudror'
print(dragons)       # ['Targiss', 'Coporth']
