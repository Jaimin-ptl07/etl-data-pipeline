from kafka import KafkaConsumer
import json

# Kafka consumer setup
consumer = KafkaConsumer('incoming-data',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))

# Reading data from Kafka
for message in consumer:
    data = message.value
    print(f"Received data: {data}")
