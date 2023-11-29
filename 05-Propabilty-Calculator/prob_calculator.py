import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      for i in range(0, value):
        self.contents.append(key)

  def draw(self, number):
    if number >= len(self.contents):
      return self.contents
    result = []

    for i in range(number):
      num = random.randint(0, len(self.contents) - 1)
      result.append(self.contents.pop(num))
    return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum(
            [1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        M += 1 if balls_req == len(expected_balls) else 0

    return M / num_experiments



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
