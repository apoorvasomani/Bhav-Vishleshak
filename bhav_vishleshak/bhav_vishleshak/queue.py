

class BaseQueueClass(object):

	EXCHANGE = None
	ROUTING_KEY = None
	MESSAGE = None
	MESSAGE_TYPE = None

	def publish(self):
		"""
		Publish the message

		"""
		pass

	def callback(self):
		"""
		Action that needs to be taken to on messages in the queue
		
		"""
		pass

	def start_consuming(self):
		"""
		Start consuming messages from the queue

		"""
