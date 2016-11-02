#### DOWNLOAD DATA ####

Download Movie data from http://grouplens.org/datasets/movielens/
Unzipping 100K and 1M files will create ml-100k and ml-1m folders respectively

#### Execute ####

After setting up AWS SECURITY KEY environment variables. Execute following command to run MapReduce job in AWS EMR

## 100k data with 4 nodes.
python MovieSimilarities.py -r emr --num-ec2-instances 4 --items=ml-100k/u.item ml-100k/u.data > sims-4-machines.txt

## 1M data with 16 nodes.

python MovieSimilaritiesLarge.py -r emr --num-ec2-instances=20 --items=ml-1m/movies.dat ml-1m/ratings.dat > sims-16-machines.txt

## Troubleshooting EMR jobs (subsitute your job ID):
python -m mrjob.tools.emr.fetch_logs --find-failure j-1NXMMBNEQHAFT