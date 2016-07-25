
import randplayer
import smarthistplayer
import histplayer

_RUN_COUNT = 300


def Play(run_count):
  history = []  # List of tuples.
  last_game = ()  # Tuple of who played what.
  p1 = randplayer.Player()
  p2 = smarthistplayer.Player()
  for i in range(run_count):
    # Run is sent the last game, the player_id and a
    # function to figure out who played what.
    first = p1.Run(last_game, 1, Judge)
    second = p2.Run(last_game, 2, Judge)
    last_game = (first, second)
    history.append(last_game)
  return history


# Takes a tuple of who played what.
# Returns 0 if draw, otherwise returned player_id
# of the winner.
def Judge(game):
  if game[0] == game[1]:
    return 0
  if game[0] == 'R' and game[1] == 'P':
    return 2
  if game[0] == 'P' and game[1] == 'S':
    return 2
  if game[0] == 'S' and game[1] == 'R':
    return 2
  return 1

def main():
  games = Play(_RUN_COUNT)
  count = [0] * 3
  for game in games:
    winner = Judge(game)
    print "%s v %s. Winner: %d" % (game[0], game[1], winner)
    count[winner] += 1
  print "Draw count = %d" % count[0]
  print "Player 1 win count = %d" % count[1]
  print "Player 2 win count = %d" % count[2]


if __name__ == "__main__":
  main()
