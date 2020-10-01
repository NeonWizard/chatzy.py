class Client():
	"""
	Chatzy client used to do most things.

	"""

	def __init__(self):
		pass

	def login(self, email, password, force=False):
		"""Authenticate with Chatzy to get an API token.

		Args:
			email (str): Email associated with the account
			password (str): Password associated with the account
			force (bool): Whether to ignore saved bearer tokens
		Returns:
			Client

		"""
		raise NotImplementedError

	def join_room(self, room_id):
		"""Join a room identified by the room_id argument.

		Args:
			room_id (str): ID of the room to leave.
		Returns:
			Room

		"""
		raise NotImplementedError
	def leave_room(self, room_id):
		"""Leave a room identified by the room_id argument.

		Args:
			room_id (str): ID of the room to leave.
		Returns:
			Room

		"""
		raise NotImplementedError
