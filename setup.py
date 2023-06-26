from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    Hyphen_E_DOT = '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if Hyphen_E_DOT in requirements:
            requirements.remove(Hyphen_E_DOT)
        
    return  requirements

setup(
name='mlproject',
version='1.0',
author='vivek',
author_email='vivek.eie57@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
 