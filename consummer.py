# manually assign the partition list for the consumer
from kafka import KafkaConsumer
consumer = KafkaConsumer('test-topic',bootstrap_servers='localhost:9092',auto_offset_reset="earliest")

for messages in consumer:
    print(messages.value.decode('utf-8'))