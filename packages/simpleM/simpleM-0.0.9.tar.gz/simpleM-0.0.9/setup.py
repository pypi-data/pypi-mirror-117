from setuptools import setup, find_packages
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        print('post install dev hello')

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        print('post install hello')

VERSION = '0.0.9' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="simpleM", 
        version=VERSION,
        author="qiujingyu",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        data_files=[('man/man1', ['doc/a/b.txt'])],
        cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
        },

)