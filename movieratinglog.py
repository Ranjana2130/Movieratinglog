#Create a movie rating log using oops concept for rating the movies 


class Movie_Rating:

  def __init__(self,moviename,storyrating,actorrating,musicrating):
    self.movie_name = moviename
    self.story_rating = storyrating
    self.actor_rating = actorrating
    self.music_rating = musicrating
    self.avg_rating = int((self.story_rating + self.actor_rating + self.music_rating)/3)


  def display(self):
    print("Movie name= ",self.movie_name,"Story rating=",self.story_rating ,"Actor rating=",self.actor_rating,"Music rating = ",self.music_rating,
          "Avg rating= ",  self.avg_rating)


moviereview1 = Movie_Rating("RRR",2,3,4)
moviereview2 = Movie_Rating("Avatar",3,4,5)
moviereview3 = Movie_Rating("Titanic",3,4,5)
moviereview4 = Movie_Rating("The Matrix",3,4,5)
moviereview5 = Movie_Rating("Spiderman",3,4,5)

moviereview1.display()
moviereview2.display()
moviereview3.display()
moviereview4.display()
moviereview5.display()
