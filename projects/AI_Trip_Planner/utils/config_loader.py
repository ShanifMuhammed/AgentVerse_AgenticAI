



import yaml
import os

def load_config(config_path: str = r"C:\Users\msk01\Desktop\SD\AgentVerse_AgenticAI\AI_Trip_Planner\config\config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        print(config)
    return config

load_config()