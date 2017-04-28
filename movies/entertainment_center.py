import media
import fresh_tomatoes

# Create movie objects from media module populated with args

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/' +
                        'Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     'http://upload.wikimedia.org/wikipedia/id/b/b0/' +
                     'Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=d1_JBMrrYw8')
clueless = media.Movie('Clueless',
                       'Upper-class girls who care more about' +
                       'fashion than grades',
                       'http://static.rogerebert.com/uploads/movie/mov' +
                       'ie_poster/clueless-1995/large_lEXuvv0yxjQC2LSKwh5gS' +
                       'ia3d5E.jpg',
                       'https://www.youtube.com/watch?v=RS0KyTZ3Ie4')
captain_f = media.Movie('Captain Fantastic', 'Dad raises kids in woods',
                        'https://images-na.ssl-images-amazon.com/images/M/' +
                        'MV5BMjE5OTM0OTY5NF5BMl5BanBnXkFtZTgwMDcxOTQ3ODE@' +
                        '._V1_UY1200_CR90,0,630,1200_AL_.jpg',
                        'https://www.youtube.com/watch?v=D1kH4OMIOMc')
hachiko = media.Movie('Hachiko',
                      "A lost puppy becomes the world's best dog",
                      'http://www.sonypictures.com/movies/hachi' +
                      'adogstale/assets/images/onesheet.jpg',
                      'https://www.youtube.com/watch?v=mhEHr7B1QiU')
jobs = media.Movie('Jobs', 'The early days of Apple',
                   'https://upload.wikimedia.org/wikipedia/' +
                   'en/e/e0/Jobs_%28film%29.jpg',
                   'https://www.youtube.com/watch?v=FrvkCS0ZGPU')

# Populate a list with the movie objects

movie_list = [
    toy_story,
    avatar,
    clueless,
    captain_f,
    hachiko,
    jobs,
    ]

# Call the open_movies function and pass in the movie list as an arg

fresh_tomatoes.open_movies_page(movie_list)
