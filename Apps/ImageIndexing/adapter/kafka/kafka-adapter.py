#
# def subscribe(self):
#     self.consumer.subscribe([self.topic_name])
#
# def consume(self):
#     while True:
#         msg = self.consumer.poll(0)
#         if msg is None:
#             continue
#         if msg.error():
#             print("Consumer error: {}".format(msg.error()))
#             continue
#
#         print('Received message: {}'.format(msg.value().decode('utf-8')))
#
# def close(self):
#     self.consumer.close()

class KafkaAdapter:
    def __init__(self):
        pass

