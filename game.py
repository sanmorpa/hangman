from hangman import HangMan
from viewer import Viewer
from player import Player

class Game():
	def __init__(self):
		self.hangman = HangMan()
		self.alive = True
		self.viewer = Viewer()
		self.player = Player()

	def start_game(self):
		"""
		Sets the configuration for the game and starts the loop
		"""
		self._configuration()
		self._loop()

	def _configuration(self):
		"""
		Sets the random word from the word list
		"""
		self.hangman.pick_word()

	def _loop(self):
		""""
		Game loop that controls the game flow
		"""
		stored = self.hangman.word
		self.viewer.welcome(stored)
		while self.hangman.is_alive():
			self.viewer.secret_word(self.hangman)
			self.player.play(self.hangman, stored)
			self.viewer.picture(self.hangman.stage)
		if self.player.has_won(self.hangman):
			print(f"CONGRATULATIONS! You've won. The word was {stored}")
		else:
			print(f"OH NO! You've lost. The word was {stored}")
