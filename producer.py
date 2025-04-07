from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(30, 60):
    producer.send(topic='test-topic',key="0".encode("utf-8"), value=f"new message {i}".encode('utf-8'))


producer.flush()