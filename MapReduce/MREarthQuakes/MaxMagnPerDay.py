from mrjob.job import MRJob

class MRMaxMagnPerDay(MRJob):

    ##def GetDay(self,longdate):
      ##  return longdate[:10]

    def mapper(self, _, line):
        (publicid,eventtype,origintime,a,longitude,latitude,magnitude,depth,magnitudetype,depthtype,b,c,d,e,f,g,h,i,j,k,l) = line.split(',')
        if (eventtype == 'earthquake'):
            yield origintime[:10],magnitude

    def reducer(self,day,magnitudes):
        yield day, round(float(max(magnitudes)),2)

if __name__ == '__main__':
    MRMaxMagnPerDay.run()