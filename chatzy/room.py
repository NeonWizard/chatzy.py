import requests

class Room:
	"""
	A chatroom on Chatzy.

	"""

	def __init__(self):
		pass

	def join(self):
		"""Join this Chatzy room.

		Args:
		Returns:
			Room: self
		Throws:
			NotImplementedError
		"""
		raise NotImplementedError

	def leave(self):
		"""Leave this Chatzy room.

		Args:
		Returns:
			Room: self
		Throws:
			NotImplementedError

		"""
		raise NotImplementedError

	def send_message(self, message):
		"""Send a message.

		Args:
			message (str): Message content to send.
		Returns:
			Message: Created message object
		Throws:
			NotImplementedError
		"""
		raise NotImplementedError
