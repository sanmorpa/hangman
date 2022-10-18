from settings import *
from string_outils import *

class Viewer():
	def welcome(self, word):
		"""
		Shows a welcome message to the game
		"""
		print(f"Welcome to the Hangman! Your word has {len(word)} letters. Enjoy!\n")

	def picture(self, stage):
		"""
		Shows the picture of the current stage that the hangman is in
		"""
		print(HANGMAN[stage]+ "\n")

	def secret_word(self, hangman):
		"""
		Shows the secret word blank and filled spaces of a hangman
		"""
		print(hangman.secret)

	def remaining_letters(self, hangman):
		"""
		Shows the letters of a hangman that haven't been used
		"""
		formated = column_format(hangman.get_available)
		for item in formated:
			print(item)
