# Imdb movie details : This program displays a list of movies and based on the user input shows
# more details about the same. This continues until the user types q

movie_dict = {"The Shawshank Redemption": ["Frank Darabont", """Two imprisoned men bond over a 
number of years, finding solace and eventual redemption through acts of common decency"""],

              "Forrest Gump": ["Robert Zemeckis", """The presidencies of Kennedy and Johnson, the Vietnam 
War, the Watergate scandal and other historical events unfold from the perspective of an 
Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart."""],

              "The Godfather": ["Francis Ford Coppola", """An organized crime dynasty's aging patriarch 
transfers control of his clandestine empire to his reluctant son."""],

              "Pulp Fiction": ["Quentin Tarantino", """The lives of two mob hitmen, a boxer, a gangster 
and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."""],

              "Fight Club": ["David Fincher", """An insomniac office worker and a devil-may-care soap maker 
form an underground fight club that evolves into much more."""],

              "Avatar": ["James Cameron", """A paraplegic Marine dispatched to the moon Pandora on a unique 
mission becomes torn between following his orders and protecting the world he feels is his home."""]
              }

user_response = 'y'
while user_response != 'q':
    print("###########################################")
    print("#############IMDB Movie Details############")
    print("###########################################")
    print("List of movies:")
    for movie_name in movie_dict:
        print(movie_name)
    movie_choice = input("Pick one to know more details : ")
    print('---------------------------------------')
    print("Movie name chosen :", movie_choice)
    print("Director :", movie_dict[movie_choice][0])
    print("Summary :", movie_dict[movie_choice][1].replace("\n", " "))
    print('---------------------------------------')
    user_response = input("Enter q to quit or any other letter to continue : ")
