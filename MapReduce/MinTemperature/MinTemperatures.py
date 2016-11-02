from mrjob.job import MRJob

class MRMinTemperature(MRJob):

    def MakeFahrenheit(self,tenthsOfCelsius):
        celsius=float(tenthsOfCelsius) / 10.0
        fahrenheit=celsius * 1.8 + 32.0
        return fahrenheit

    def mapper(self, _, line):
        (location,date,type,data,x,v,z,w) = line.split(',')
        if (type == 'TMIN'):
            temperature=self.MakeFahrenheit(data)
            yield location,temperature

    def reducer(self,location,temperature):
        yield location, min(temperature)

if __name__ == '__main__':
    MRMinTemperature.run()