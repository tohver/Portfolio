from kafka import KafkaConsumer
from time import sleep
import json
from s3fs import S3FileSystem
import configparser


BOOTSTRAP_URL = ''
BUCKET_NAME = ''
s3 = S3FileSystem()

consumer = KafkaConsumer(
	'market_data', 
	bootstrap_servers = [f'{BOOTSTRAP_URL}:9092'], 
	value_deserializer = lambda x: json.loads(x.decode('utf-8')))

for count, values in enumerate(consumer):
	with s3.open(f"s3://BUCKET_NAME/stock_data{count}.json") as fh:
		json.dump(values.value, fh)

