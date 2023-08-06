from distutils.core import setup
# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'whatsminer',         # How you named your package folder (MyLib)
  packages = ['whatsminer'],   # Chose the same as "name"
  version = '0.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Choose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Unofficial python API for MicroBT Whatsminer ASICs',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Satoshi Anonymoto',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/satoshi-anonymoto/whatsminer-api',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/satoshi-anonymoto/whatsminer-api/archive/refs/tags/0.1.0.tar.gz',
  keywords = ['whatsminer', 'microbt', 'api'],   # Keywords that define your package best
  install_requires=[
          'passlib',
          'pycryptodome',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)