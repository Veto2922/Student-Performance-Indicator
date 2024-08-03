from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    req = []
    with open(file_path) as f:
        req = f.readlines()
        req = [i.replace('\n', '') for i in req]
    
        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    
    return req

setup(
    name='student_Performance_Indicator',
    version='0.0.1',
    author='Abdelrahman Mohamed',
    author_email='abdelrahman.m2922@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
