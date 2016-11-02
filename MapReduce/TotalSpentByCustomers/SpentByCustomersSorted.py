from mrjob.job import MRJob
from mrjob.step import MRStep

class MRSpentByCustomersSorted(MRJob):


    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_orders,
                   reducer=self.reducer_count_total),
            MRStep(mapper=self.mapper_make_counts_key,
                   reducer=self.reducer_output_total)
        ]


    def mapper_get_orders(self, _, line):
        (custid,itemid,amount) = line.split(',')
        yield custid,float(amount)


    def reducer_count_total(self,key,values):
        yield key, sum(values)

    def mapper_make_counts_key(self,custid,total):
        #yield float(total),custid
        yield '%04.02f'%float(total),custid

    def reducer_output_total(self,total,custids):
        for custid in custids:
            yield custid,total


if __name__ == '__main__':
    MRSpentByCustomersSorted.run()