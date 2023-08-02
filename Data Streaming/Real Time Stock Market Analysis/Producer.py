# env: kafka
import pandas as pd
from kafka import KafkaProducer
from time import sleep
import json


producer = KafkaProducer(
    bootstrap_servers = [':9092'],
    value_serializer = lambda x: json.dumps(x).encode('utf-8') 
                         )

market_data = pd.read_csv('data/market_data.csv')

while True:
	sample = market_data.sample(1).to_dict(orient = 'record')[0]
	producer.send('market_data',  = sample)
	sleep(1)