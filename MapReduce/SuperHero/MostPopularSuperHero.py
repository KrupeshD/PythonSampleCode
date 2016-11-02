from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMostPopularSuperHero(MRJob):

    def configure_options(self):
        super(MRMostPopularSuperHero,self).configure_options()
        self.add_file_option('--names',help='Path to Marvel-names.txt')

    def steps(self):
        return [
             MRStep(mapper=self.mapper_count_friends_per_line,
                   reducer=self.reducer_combine_friends),
            MRStep(mapper = self.mapper_prep_for_sort,
                   mapper_init=self.load_name_dict,
                   reducer = self.reducer_find_max_friends)
        ]

#Each line in graph.txt represents list of friends of the superhero character denoted by the first value. That's the characterId of the superhero in question.
#Rest of characterIds in that line respresent friends of the superhero

    def mapper_count_friends_per_line(self, _, line):
        fields = line.split()
        heroID = fields[0]
        numFriends = len(fields) - 1
        yield int(heroID),int(numFriends)


    def reducer_combine_friends(self, key, values):
        yield key,sum(values)

    def load_name_dict(self):
        self.heroNames={}

#encoding = 'latin-1', in open function, is used to avoid following error.
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 2892: invalid continuation byte

        with open("names.txt",encoding='latin-1') as f:
            for line in f:
                fields = line.split('"')
                self.heroNames[int(fields[0])] = fields[1]

    def  mapper_prep_for_sort(self,key,value):
        yield None,(value,self.heroNames[key])

    def reducer_find_max_friends(self, key, values):
        yield max(values)



if __name__ == '__main__':
    MRMostPopularSuperHero.run()