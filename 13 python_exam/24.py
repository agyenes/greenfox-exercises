
class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.song_ratings = []

    def rate(self, rating):
        if rating >= 1 and rating <= 5:
            self.song_ratings.append(rating)
        else:
            raise Error('rating must be between 1 and 5')

    def get_average_rating(self):
        sum_of_ratings = 0
        for num in self.song_ratings:
            sum_of_ratings += num
        return sum_of_ratings/len(self.song_ratings)

class Jukebox(object):
    def __init__(self, list_of_songs):
        self.list_of_songs = list_of_songs

    def rate(self, title, rating):
        for song in self.list_of_songs:
            if title == song.title:
                song.rate(rating)

    def get_song_titles_by_artist(self, input_artist):
        song_titles_by_artist = []
        for song in self.list_of_songs:
            if input_artist == song.artist:
                song_titles_by_artist.append(song.title)
        return song_titles_by_artist

    def get_top_rated_title(self):
        top_rated = self.list_of_songs[0]
        for song in self.list_of_songs[1:len(self.list_of_songs)]:
            if song.rating > top_rated.rating:
                top_rated = song
        return top_rated.title

song1 = Song('nice as fuck', 'mall music')
song2 = Song('big business', 'regulars')
song3 = Song('big business', 'send help')
song4 = Song('big business', 'horses')
song5 = Song('prostitutes', 'pregnant toad')
song6 = Song('prostitutes', 'cheap amplifiers')

song1.rate(5)
song2.rate(4)
song3.rate(3)
song3.rate(5)
song4.rate(5)
song5.rate(2)
song6.rate(3)

print(song1.get_average_rating())
print(song3.get_average_rating())

jukebox1 = Jukebox([song1, song2, song3, song6])

jukebox1.rate(song1, 3)
jukebox1.rate(song2, 2)
jukebox1.rate(song3, 1)
jukebox1.rate(song4, 5)

print(jukebox1.get_song_titles_by_artist('big business'))

print(jukebox1.get_top_rated_title())
