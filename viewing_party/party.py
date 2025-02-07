# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
   if title == None or genre == None or rating == None:
       return None
   dict = {}
   dict["title"] = title
   dict["genre"] = genre
   dict["rating"] = rating
   return dict
    

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            add_to_watched(user_data, user_data["watchlist"][i])
            del user_data["watchlist"][i]
            break
    return user_data

        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0.0
    tot_watched = len(user_data["watched"])
    if tot_watched ==0:
        return 0.0
    for i in range(tot_watched):
        sum_rating = sum_rating + user_data["watched"][i]["rating"]
    return sum_rating/tot_watched

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genres = {}
    for i in range(len(user_data["watched"])):
        temp_genre = user_data["watched"][i]["genre"]
        if temp_genre in genres:
           genres[temp_genre] += 1
        else:
           genres[temp_genre] = 1 
    most_watched_genre = max(genres, key=genres.get)
    
    return most_watched_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# {watched:[{},{}..], friends:[{watched:[{movie:{title}}...]},{}] }

def get_unique_watched(user_data):
    friends_watch = []
    user_watch = []
    result = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watch.append(movie["title"])
    
    for movie in user_data["watched"]:
        user_watch.append(movie["title"])
        
    my_unique_title = list(set(user_watch)-set(friends_watch))
    for movie in user_data["watched"]:
        if movie["title"] in my_unique_title:
            result.append(movie) 
    
    return result


def get_friends_unique_watched(user_data):
    friends_watch = []
    user_watch = []
    result = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watch.append(movie["title"])
    
    for movie in user_data["watched"]:
        user_watch.append(movie["title"])
        
    friend_unique_title = list(set(friends_watch)-set(user_watch))
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friend_unique_title and movie not in result:
                result.append(movie) 
    
    return result


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# user_data={subscriptions:[], friends:[{watched:{movie: {host:xxx}}},{}] }
def get_available_recs(user_data):
    recommended_movies = []
    only_friends_watched = get_friends_unique_watched(user_data)    
    for movie in only_friends_watched:
        if (movie["host"] in user_data["subscriptions"]):
            recommended_movies.append(movie)

    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    most_genre = get_most_watched_genre(user_data)
    only_friends_watched = get_friends_unique_watched(user_data) 
    for movie in only_friends_watched:
        if movie["genre"] == most_genre:
            recommended_movies.append(movie)
    return recommended_movies

# {favorites:[{},..] }
def get_rec_from_favorites(user_data):
    recommend_movies = []
    only_user_watched = get_unique_watched(user_data)
    for movie in only_user_watched:
        if movie in user_data["favorites"]:
            recommend_movies.append(movie) 
    return recommend_movies
