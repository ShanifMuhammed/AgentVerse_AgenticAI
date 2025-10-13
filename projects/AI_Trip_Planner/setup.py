from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    this function will return list of the requirements
    """
    requirement_list:List[str]=[]
    try:
        with open("requirement.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("file not found error")
    return requirement_list

print (get_requirements())

setup(
    name= "AI_travel_planner",
    version="0.0.1",
    author="Muhammed Shanif KP",
    author_email = "if56015549@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.13"
)

