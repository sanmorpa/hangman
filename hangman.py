import settings
from random import choice

class HangMan():
	def __init__(self):
		self._available = list("abcdefghijklmnopqrstuvwxyz")
		self.word = None
		self.stage = 0
		self.secret = "_"

	def pick_word(self):
		"""
		Chooses a random word and sets the number of blankspaces to show the player
		"""
		self.word = choice(settings.WORD_BANK)
		self.secret += " _" * (len(self.word) - 1)

	def is_alive(self):
		"""
		Returns true if there are still letters in the available list and the user hasn't lost
		"""
		return len(self._available) > 0 and self.stage < settings.LIVES and len(self.word) > 0

	@property
	def get_available(self):
		return self._available

	@get_available.setter
	def set_available(self, new):
		self._available = new
