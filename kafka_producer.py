from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['10.0.0.4:6667'])
message = "Hello from python"
b_msg = bytearray()
b_msg.extend(map(ord, message))
producer.send('test', b_msg)
producer.flush()
