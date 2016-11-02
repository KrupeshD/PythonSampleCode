from mrjob.job import MRJob

class MREarthQuakes(MRJob):

    def GetDay(self,longdate):
        return longdate[:10]

    def mapper(self, _, line):
        (publicid,eventtype,origintime,a,longitude,latitude,magnitude,depth,magnitudetype,depthtype,b,c,d,e,f,g,h,i,j,k,l) = line.split(',')
        yield eventtype,1

    def reducer(self,etype,cnt):
        yield etype, sum(cnt)

if __name__ == '__main__':
    MREarthQuakes.run()