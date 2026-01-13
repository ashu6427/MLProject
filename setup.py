from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file:
        requirement = file.readlines()
        requirement = [req.replace("\n", "") for req in requirement]
        requirements.extend(requirement)

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Ashutosh",
    author_email="ashutosh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
