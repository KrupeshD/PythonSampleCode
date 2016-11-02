from mrjob.job import MRJob

class MRAverageFriends(MRJob):
    def mapper(self, key, line):
        (userid,name,age,nfriends) = line.split(',')
        yield age,float(nfriends)

    def reducer(self,age,nfriends):
        total=0
        numElem=0
        for x in nfriends:
            total +=x
            numElem +=1
        yield age, total/numElem

if __name__ == '__main__':
    MRAverageFriends.run()