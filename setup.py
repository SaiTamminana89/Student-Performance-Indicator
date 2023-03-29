from setuptools import find_packages,setup
from typing import List

HYPEN_EDOT = '-e.'
def get_requirements(file_Path:str)->List[str]:
    # this function returns the list of requirements
    requirements = []
    with open(file_Path) as file:
        requirements = file.readlines()
        requirements = [r.replace('\n','') for r in requirements ]
        if HYPEN_EDOT in requirements:
            requirements.remove(HYPEN_EDOT) 
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author = 'SaiKumar',
    email = 'saitamminana@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
       
    
)