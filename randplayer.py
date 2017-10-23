# Picks a random choice.
import random
import player

class Player(player.BasePlayer):
  def Run(self, last_game, player_id, jfunc):
    return random.choice('RPS')
