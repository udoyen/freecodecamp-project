import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        contents_info = self.contents_generator(**kwargs)
        self.contents = contents_info

    def draw(self, draw_count) -> list:
        """
        Function to draw specified
        number of balls from collection

        :param draw_count:
        :return:
        """
        drawn_balls = []
        # print(f"Contents 2: {random.sample(self.contents, draw_count)}")
        if draw_count > len(self.contents):
            return self.contents
        sample = random.sample(self.contents, draw_count)
        # print(f"Upper Sample: {sample}")
        [self.contents.pop(self.contents.index(x)) for x in sample]
        return sample

    @staticmethod
    def contents_generator(**kwargs) -> list:
        """
        Function to generate
        collection contents
        :param kwargs:
        :return:
        """
        contents = []
        for key, value in kwargs.items():
            for i in range(value):
                contents.append(key)
        return contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    """
    Function to run probability
    experiments
    :param hat:
    :param expected_balls:
    :param num_balls_drawn:
    :param num_experiments:
    :return:
    """
    hit = 0
    target = []
    # print(f"Sample: {sample}")
    for k, v in expected_balls.items():
        for i in range(v):
            target.append(k)

    for i in range(num_experiments):
        hat3 = copy.deepcopy(hat)
        t_length = len(target)
        sample = hat3.draw(num_balls_drawn)

        for j in target:
            try:
                n = sample.index(j)
            except:
                continue
            if t_length != 0:
                if sample.pop(sample.index(j)):
                    t_length -= 1
            if t_length == 0:
                hit += 1

    return hit / num_experiments
