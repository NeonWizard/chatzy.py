import requests

from .room import Room
from .util import exceptions

class Client():
	"""
	Chatzy client used to do most things.

	"""

	def __init__(self):
		self.__token = None
		self.authenticated = False

	def login(self, email, password, force=False):
		"""Authenticate with Chatzy to get an API token.

		Args:
			email (str): The email associated with the account.
			password (str): The password associated with the account.
			force (bool, optional): Whether to ignore saved bearer tokens.
		Returns:
			Client: self
		Raises:
			BadAPIResponse: If login fails for any reason.
			AlreadyAuthenticated: If an auth token has already been requested
			and the force argument was not provided.

		"""

		if self.authenticated and not force:
			raise exceptions.AlreadyAuthenticated(
				f"Already authenticated with email {email}")

		headers = {
			'content-type': 'application/x-www-form-urlencoded'
		}
		data = {
		    'X7838': 'sign.htm',
			'X2309': '1581170387', # some constant
			'X4812': '1',
			'X4778': 'sign',
			'X3127': email,
			'X2420': '1',
			'X8485': password,
			'X2627': '1',
			'X3483': '0',
			'X2459': '1'
		}

		response = requests.post('https://www.chatzy.com/',
			headers=headers,
			data=data)

		if "redirect#ok:entered" in response.text:
			self.authenticated = True
			self.__token = response.cookies["ChatzyUser"]
			return self
		else:
			raise exceptions.BadAPIResponse

	def fetch_rooms(self, limit=50):
		"""Yields all rooms the user has visited previously.

		Args:
			limit (int, optional): Limit of amount of rooms to fetch. Defaults to 50.
		Yields:
			Room: A chatzy Room object.
		Raises:
			NotAuthenticated: If the client is not logged in.

		"""
		if not self.authenticated:
			raise exceptions.NotAuthenticated("Can't fetch rooms - not logged in!")

	def fetch_room(self, room_id):
		"""Fetches a room from an ID.

		Args:
			room_id (int): ID of the room to fetch.
		Returns:
			Room: A chatzy Room object.
		Raises:
			NotFound: If a room is not found with the provided ID.
			NotAuthenticated: If the client is not logged in.

		"""
		if not self.authenticated:
			raise exceptions.NotAuthenticated("Can't fetch room - not logged in!")

	def join_room(self, room_id):
		"""Join a room identified by the room_id argument.

		Args:
			room_id (str): ID of the room to join.
		Returns:
			Room: Room if wait flag set (when joined)
		Raises:
			NotFound: If a room is not found with the provided ID.
			NotAuthenticated: If the client is not logged in.

		"""
		if not self.authenticated:
			raise exceptions.NotAuthenticated("Can't join room - not logged in!")

	def leave_room(self, room_id):
		"""Leave a room identified by the room_id argument.

		Args:
			room_id (str): ID of the room to leave.
		Returns:
			Room: Room
		Raises:
			NotFound: If user is not in a room with the provided ID.
			NotAuthenticated: If the client is not logged in.

		"""
		if not self.authenticated:
			raise exceptions.NotAuthenticated("Can't leave room - not logged in!")
