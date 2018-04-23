from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['10.156.91.65:9092'],api_version=(0,10))
producer.send('test', b"Hello from python")
producer.flush()

