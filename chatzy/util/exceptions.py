class BadAPIResponse(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class NotFound(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class Forbidden(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class NotAuthenticated(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class RateLimit(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class InvalidContent(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class AlreadyAuthenticated(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
