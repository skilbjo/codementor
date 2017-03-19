#!/usr/bin/env python

class Yelp(object):
  def __init__(self, restaurants, ratings):
    self.restaurants = restaurants
    self.ratings = ratings

  def find(self, coordinates, radius, dining_hour=None, sort_by_rating=False):
    # Returns list of Restaurant within radius.
    #
    #  coordinates: (latitude, longitude)
    #  radius: kilometer in integer
    #  dining_hour: If None, find any restaurant in radius.
    #               Otherwise return list of open restaurants at specified hour.
    #  sort_by_rating: If True, sort result in descending order,
    #                  highest rated first.
    results = []
    radius = radius * 0.1 # Turn radius into lat/long scale

    def in_search_radius(coordinates, radius):
      if (restaurant.latitude - coordinates[0] < radius) or (restaurant.longitude - coordinates[1] < radius):
        return True
      else:
        return False

    for i,restaurant in enumerate(self.restaurants):
      if in_search_radius(coordinates,radius):
        if dining_hour:
          if restaurant.open_hour <= dining_hour <= restaurant.close_hour:
            results.append((restaurant.name,self.ratings[i].rating))
        else:
          results.append((restaurant.name,self.ratings[i].rating))

    if sort_by_rating:
      results.sort(key = lambda restaurant: (restaurant[1] * -1, restaurant[0]))

    return results

class Restaurant(object):
  # where open_hour and close_hour is in [0-23]
  def __init__(self, id, name, latitude, longitude, open_hour, close_hour):
    self.id = id
    self.name = name
    self.latitude = latitude
    self.longitude = longitude
    self.open_hour = open_hour
    self.close_hour = close_hour

class Rating(object):
  # rating is in [1-5]
  def __init__(self, restaurant_id, rating):
      self.restaurant_id = restaurant_id
      self.rating = rating

def main():
  restaurants = [Restaurant(0, "Domino's Pizza", 37.7577, -122.4376, 7, 23),
                 Restaurant(1, "Another Cafe", 40.7577, 122.4376, 10, 18),
                 Restaurant(2, "Olea", 37.7587, -122.4376, 10, 18)]
  ratings = [Rating(0, 3), Rating(1,5), Rating(2,4)]

  y = Yelp(restaurants, ratings)
  results = y.find((37.7, -122.6), 5, None, False)
  print results
  return results

if __name__ == '__main__':
  main()
