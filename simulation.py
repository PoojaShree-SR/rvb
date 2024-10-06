import random

# Simulating the Red Team (Attackers)
class RedTeamSimulator:
    def __init__(self):
        # List of attack types
        self.attacks = ["SQL Injection", "Cross-Site Scripting (XSS)", "Phishing Email"]

    # Function to randomly pick an attack
    def launch_attack(self):
        attack = random.choice(self.attacks)
        print(f"Red Team: Launching {attack}")
        return attack

# Simulating the Blue Team (Defenders)
class BlueTeamMonitor:
    def __init__(self):
        # List of detection methods
        self.detection_methods = ["Log Analysis", "Network Monitoring", "Intrusion Detection System"]

    # Function to randomly detect an attack
    def detect_attack(self, attack):
        detection = random.choice(self.detection_methods)
        print(f"Blue Team: Using {detection} to detect {attack}")
        # Randomly decide if the attack was detected or not
        detected = random.choice([True, False])
        if detected:
            print(f"Blue Team: Attack {attack} detected!")
        else:
            print(f"Blue Team: Attack {attack} not detected.")
        return detected

# Simulating the Red vs. Blue Team Interaction
class Simulation:
    def __init__(self):
        # Initialize red team (attackers) and blue team (defenders)
        self.red_team = RedTeamSimulator()
        self.blue_team = BlueTeamMonitor()

    # Function to run the simulation for a number of rounds
    def run(self, rounds=3):
        results = []
        for round_num in range(1, rounds + 1):
            print(f"\n--- Round {round_num} ---")
            attack = self.red_team.launch_attack()
            detected = self.blue_team.detect_attack(attack)
            results.append((attack, detected))
        return results

    # Function to evaluate results of the simulation
    def evaluate_results(self, results):
        print("\n--- Evaluation Report ---")
        total_attacks = len(results)
        detected_attacks = sum(detected for _, detected in results)
        detection_rate = (detected_attacks / total_attacks) * 100
        print(f"Total Attacks: {total_attacks}")
        print(f"Detected Attacks: {detected_attacks}")
        print(f"Detection Rate: {detection_rate:.2f}%")

# Run the simulation
if __name__ == "__main__":
    simulation = Simulation()
    results = simulation.run()
    simulation.evaluate_results(results)
