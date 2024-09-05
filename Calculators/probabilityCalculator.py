# Free Code Camp Project (Certification Requirement)

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Initialize the contents list with the appropriate number of balls for each color.
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count) # Add 'color' (count) times.


    def draw(self, num_balls):
         # If the number of balls to draw is greater than available, return all balls and clear the hat
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]  # Make a copy of all the balls
            self.contents = []  # Empty the hat
            return drawn_balls
        
        # randomly draw balls from the hat
        drawn_balls = random.sample(self.contents, num_balls)

        # remove drawn balls from the hat 
        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Create new copy of the hat.
        trial_hat = Hat(**{ball: hat.contents.count(ball) for ball in set(hat.contents)})

        # Draw balls from the hat
        drawn_balls = trial_hat.draw(num_balls_drawn)

        # Count num of balls of each color in drawn balls
        drawn_count = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}

        # if drawn balls meet or exceed expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1
        
    # return the probability as the ratio of successful experiments
    return success_count / num_experiments


hat = Hat(blue=10, red=10, green=10)
probability = experiment(
    hat=hat,
    expected_balls={'red': 1},
    num_balls_drawn=1,
    num_experiments=10000
)

print(f"Probability: {probability}")