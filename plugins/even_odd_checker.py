import random

AUTHOR = "Cid"
APP_NAME = "Even or Odd Checker"

def run():
    """Main execution function called by main.py."""
    number = random.randint(1, 100)
    classification = "Even" if number % 2 == 0 else "Odd"
    return f"🎱 {APP_NAME}: The number {number} is {classification}."
