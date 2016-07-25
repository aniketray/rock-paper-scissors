
import random

class Player(object):
  def Run(self, last_game, player_id, jfunc):
    other_player_id = 3 - player_id
    if last_game:
      winner = jfunc(last_game)
      if winner == player_id:
        return last_game[other_player_id-1]
      elif winner == other_player_id:
        return list(set('RPS') - set(last_game))[0]
    return random.choice('RPS')

