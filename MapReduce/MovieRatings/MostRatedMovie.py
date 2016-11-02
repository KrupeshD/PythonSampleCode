from mrjob.job import MRJob
from mrjob.step import MRStep

class MRRatingCounter(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(mapper=self.mapper_passthrough,
                   reducer=self.reducer_find_max)
        ]


    def mapper_get_ratings(self,key,line):
        (userID,movieID,rating,timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_ratings(self,key,values):
        yield None, (sum(values),key)

#This mapper does nothing; it's just here to avoid a bug in some
#versions of mrjob related to "non-script steps." Normally this
#wouldn't be needed.

    def mapper_passthrough(self, key, value):
        yield key, value

    def reducer_find_max(self,key,values):
        yield max(values)


if __name__ == '__main__':
    MRRatingCounter.run()