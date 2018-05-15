from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['demomaster0.shanghai.cloudapp.azurestack.corp.microsoft.com:9092'])
message = "Hello from python"
b_msg = bytearray()
b_msg.extend(map(ord, message))
producer.send('test', b_msg)
producer.flush()
