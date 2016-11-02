# To run locally:
# !python MovieSimilarities.py --items=ml-100k/u.item ml-100k/u.data > sims.txt

# To run on a single EMR node:
# !python MovieSimilarities.py -r emr --items=ml-100k/u.item ml-100k/u.data

# To run on 4 EMR nodes:
#!python MovieSimilarities.py -r emr --num-ec2-instances=4 --items=ml-100k/u.item ml-100k/u.data

# Troubleshooting EMR jobs (subsitute your job ID):
# !python -m mrjob.tools.emr.fetch_logs --find-failure j-1NXMMBNEQHAFT


from mrjob.job import MRJob
from mrjob.step import MRStep
from math import sqrt

from itertools import combinations

class MovieSimilarities(MRJob):

    def configure_options(self):
        super(MovieSimilarities, self).configure_options()
        self.add_file_option('--items', help='Path to u.item')

    def load_movie_names(self):
        # Load database of movie names.
        self.movieNames = {}

        with open("u.item") as f:
            for line in f:
                fields = line.split('|')
                self.movieNames[int(fields[0])] = fields[1].decode('utf-8', 'ignore')

    def steps(self):
        return [
            MRStep(mapper=self.mapper_parse_input,
                    reducer=self.reducer_ratings_by_user),
            MRStep(mapper=self.mapper_create_item_pairs,
                    reducer=self.reducer_compute_similarity),
            ]

    def mapper_parse_input(self, key, line):
        # Outputs userID => (movieID, rating)
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield  userID, (movieID, float(rating))

    def reducer_ratings_by_user(self, user_id, itemRatings):
        #Group (item, rating) pairs by userID

        ratings = []
        for movieID, rating in itemRatings:
            ratings.append((movieID, rating))

        yield user_id, ratings

    def mapper_create_item_pairs(self, user_id, itemRatings):
        # Find every pair of movies each user has seen, and emit
        # each pair with its associated ratings

        # "combinations" finds every possible pair from the list of movies
        # this user viewed.
        for itemRating1, itemRating2 in combinations(itemRatings, 2):
            movieID1 = itemRating1[0]
            rating1 = itemRating1[1]
            movieID2 = itemRating2[0]
            rating2 = itemRating2[1]

            # Produce both orders so sims are bi-directional
            yield (movieID1, movieID2), (rating1, rating2)
            yield (movieID2, movieID1), (rating2, rating1)




    def reducer_compute_similarity(self, moviePair, ratingPairs):
        # Compute the similarity score between the ratings vectors
        # for each movie pair viewed by multiple people

        # Output movie pair => score, number of co-ratings


        yield moviePair, ratingPairs




if __name__ == '__main__':
    MovieSimilarities.run()
