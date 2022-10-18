from string_outils import *

class Player():
	def play(self, hangman, stored):
		"""
		The player's turn
		"""
		chosen = self._ask_input(hangman)
		if chosen in hangman.word:
			print(f"\n{chosen} is in the word!")
			hangman.secret = replace_underscore(hangman.secret, chosen, stored)
			hangman.word = hangman.word.replace(chosen, "")
			hangman.set_available = [i for i in hangman.get_available if i != chosen]
		else:
			print(f"\n{chosen} is not in the word!")
			hangman.set_available = [i for i in hangman.get_available if i != chosen]
			hangman.stage += 1

	def _ask_input(self, hangman):
		"""
		The player selects a letter or asks for help
		"""
		choose = input("\nWhat letter do you select? (type 'help' to see remaining letters)\n>> ")
		while choose not in hangman.get_available:
			if choose == "help":
				print(column_format(hangman.get_available))
			else:
				print("Error, that is not an option")
			choose = input("What letter do you select? (type 'help' to see remaining letters)\n>> ")
		return choose

	def has_won(self, hangman):
		"""
		Returns True if the player has won
		"""
		return len(hangman.word) == 0
