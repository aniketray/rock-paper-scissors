# Plays whatever gave the most wins till now.
from collections import defaultdict
import random
import player

class Player(player.BasePlayer):

  def __init__(self):
    self._play_count = defaultdict(lambda: 1.0)
    self._win_count = defaultdict(lambda: 1.0)


  def CustomCmp(self, item1, item2):
    return cmp(float(self._win_count[item1]) / self._play_count[item1],
        float(self._win_count[item2]) / self._play_count[item2])


  def Run(self, last_game, player_id, jfunc):
    if last_game:
      winner = jfunc(last_game)
      i_played = last_game[player_id-1]
      if winner == player_id:
        self._win_count[i_played]+=1

    if (self._play_count['R'] > 0 and
        self._play_count['P'] > 0 and
        self._play_count['S'] > 0):
      rps = list('RPS')
      rps.sort(self.CustomCmp)
      print rps
      print self._win_count
      print self._play_count
      play = rps[-1]
      self._play_count[play] += 1
      return play

    play = random.choice('RPS')
    self._play_count[play] += 1
    return play
