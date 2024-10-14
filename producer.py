from kafka import KafkaProducer
import json
import time
from random import randint

# Kafka producer setup
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Simulating sensor data ingestion
for _ in range(100):
    data = {
        "sensor_id": randint(1, 10),
        "value": randint(10, 100),
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    # Send data to the Kafka topic
    producer.send('incoming-data', data)
    print(f"Sent data: {data}")
    time.sleep(1)

producer.flush()
