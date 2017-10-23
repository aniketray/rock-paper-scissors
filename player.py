# Abstract base class for Player

import abc

class BasePlayer(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def Run(self, last_game, player_id, jfunc):
      """Computes a strategy and returns one of 'R','P', 'S'.

      Args:
        last_game: a (char, char) tuple, where char is one of 'R',
          'P', 'S'. Denotes what Player 1, Player 2 played last game.
        player_id: int, 1 or 2, depending if current player is
          player 1 or player 2.
       jfunc: a judging function that takes a game (char, char) tuple
          as input and returns the winner's player id 1 or 2.

      Returns:
        a char, one of 'R', 'P', 'S'.
      """
      pass
