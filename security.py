# example.py

import os

def execute_command(user_input):
    os.system(f"echo {user_input}")

user_input = input("Enter something: ")
execute_command(user_input)
-------------------------------------------
# .deepsource.toml

[analysis]
  [analysis.python]
    [analysis.python.bandit]
      enabled = true  # Enable Bandit security analysis


