from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    Parameters
    ----------
    file_path : str
        requirements.txt

    Returns
    -------
    List[str]
        list of requirements to be installed
    '''
    
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
setup(
      name = 'Student-Performance',
      version = '0.0.1',
      author = 'Subhashis',
      author_email = 'subhashishansda2@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt')
)