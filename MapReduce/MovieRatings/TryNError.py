from mrjob.job import MRJob
from mrjob.step import MRStep


class MovieSimilarities(MRJob):

    def mapper(self, key, line):
        # Outputs userID => (movieID, rating)
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield  userID, (movieID, float(rating))

    def reducer(self, user_id, itemRatings):
        #Group (item, rating) pairs by userID

        ratings = []

        for movieID, rating in itemRatings:
            ratings.append((movieID, rating))

        yield user_id, ratings

if __name__ == '__main__':
    MovieSimilarities.run()