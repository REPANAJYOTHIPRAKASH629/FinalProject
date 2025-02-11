from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)
                
    except FileNotFoundError as e:
        print("requirements.txt file is not exists")
    return requirement_list

setup(
    name="GenerativeAIProject",
    author="Sivakumar",
    author_email="mshivakumarreddy78@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements()
)