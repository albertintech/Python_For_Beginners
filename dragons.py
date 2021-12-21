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
