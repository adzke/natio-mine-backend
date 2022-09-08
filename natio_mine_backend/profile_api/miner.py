import random, time

class Miner():

    def generate_random_time(self):
        return random.uniform(0.2, 2.0)

    def calculate_experience(self, profile):
        mining_actions_left = 5
        new_experience_level = 0
        current_profile = profile
        while(mining_actions_left > 0):
            time.sleep(self.generate_random_time())
            random_range = int(random.uniform(1.0, 3.5))
            new_experience_level += random_range
            mining_actions_left -= 1
            print(new_experience_level)
        return current_profile.experience + new_experience_level
        