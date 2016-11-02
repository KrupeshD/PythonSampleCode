from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMostRatedMovieNicer(MRJob):

    def configure_options(self):
        super(MRMostRatedMovieNicer,self).configure_options()
        self.add_file_option('--items',help="Path to u.item")

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer_init=self.reducer_int,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_find_max)
        ]


    def mapper_get_ratings(self,key,line):
        (userID,movieID,rating,timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_int(self):
        self.movieNames={}

#encoding = 'latin-1', in open function, is used to avoid following error.
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 2892: invalid continuation byte

        with open("u.item",encoding='latin-1') as f:
            for line in f:
                fields = line.split('|')
                self.movieNames[fields[0]] = fields[1]
                #unicode(fields[1], "utf-8", errors="ignore") #avoids issues in mrjob 5.0

    def reducer_count_ratings(self,key,values):
        yield None, (sum(values),self.movieNames[key])

    def reducer_find_max(self,key,values):
        yield max(values)


if __name__ == '__main__':
    MRMostRatedMovieNicer.run()