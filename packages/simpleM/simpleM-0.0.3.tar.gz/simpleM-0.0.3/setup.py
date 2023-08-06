import distutils.cmd
import distutils.log
import setuptools
import subprocess
import os
from setuptools import setup, find_packages

# class PylintCommand(distutils.cmd.Command):
#   """A custom command to run Pylint on all Python source files."""

#   description = 'run Pylint on Python source files'
#   user_options = [
#       # The format is (long option, short option, description).
#       ('pylint-rcfile=', None, 'path to Pylint config file'),
#   ]

#   def initialize_options(self):
#     """Set default values for options."""
#     # Each user option must be listed here with their default value.
#     self.pylint_rcfile = ''

#   def finalize_options(self):
#     """Post-process options."""
#     if self.pylint_rcfile:
#       assert os.path.exists(self.pylint_rcfile), (
#           'Pylint config file %s does not exist.' % self.pylint_rcfile)

#   def run(self):
#     """Run command."""
#     command = ['/usr/bin/pylint']
#     if self.pylint_rcfile:
#       command.append('--rcfile=%s' % self.pylint_rcfile)
#     command.append(os.getcwd())
#     self.announce(
#         'Running command: %s' % str(command),
#         level=distutils.log.INFO)
#     subprocess.check_call(command)


VERSION = '0.0.3' 
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
        package_data = {"doc":["a/b.txt"]}

)