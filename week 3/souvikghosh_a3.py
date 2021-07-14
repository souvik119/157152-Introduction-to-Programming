movie_input = input('Eating Guide!!\nEnter a number between 1-10 : ')
movie_input = int(movie_input)
print('You should eat:')
if (movie_input == 1):
    print('Panda Express')
elif (movie_input == 2):
    print('Mcdonalds')
elif (movie_input == 3):
    print('Subway')
elif (movie_input > 3 and movie_input <= 6):
    print('Burger King')
else:
    print('Dominos')