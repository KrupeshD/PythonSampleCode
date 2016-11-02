from mrjob.job import MRJob

class MRSpentByCustomers(MRJob):

    def mapper(self, _, line):
        (custid,itemid,amount) = line.split(',')
        yield custid,float(amount)

    def reducer(self,custid,amounts):
        yield custid, sum(amounts)

if __name__ == '__main__':
    MRSpentByCustomers.run()