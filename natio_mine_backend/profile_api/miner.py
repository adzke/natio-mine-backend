import random, time

class Miner():

    def generate_random_time(self):
        return random.uniform(0.2, 2.0)

    def find_gold(self):
        random_range = round(random.uniform(1, 10), 0)
        if(random_range == 10):
            print("YEEEEHAW")
            return 1
        return 0


    def calculate_experience(self, profile):
        mining_actions_left = 5
        new_experience_level = 0
        current_gold_stash = profile.gold
        current_profile = profile
        while(mining_actions_left > 0):
            time.sleep(self.generate_random_time())
            random_range = int(random.uniform(1.0, 3.5))
            new_experience_level += random_range
            mining_actions_left -= 1
            gold_found = self.find_gold()
            current_gold_stash += gold_found
        return {"experience": current_profile.experience + new_experience_level, "gold": current_gold_stash}

    def run_mining_operation(self, profile):
        experience_result = self.calculate_experience(profile)
        
        