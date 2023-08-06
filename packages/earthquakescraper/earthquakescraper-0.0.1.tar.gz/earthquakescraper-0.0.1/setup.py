from setuptools import setup
from setuptools import find_packages

setup(
    name='earthquakescraper', ## This will be the name your package will be published with
    version='0.0.1', 
    description='Web scraper that scrapes erathquake data from the USGS.',
    url='https://github.com/Marianna-Karavangeli/Earthquake_scraper.git', # Add the URL of your github repo if published 
                                                                   # in GitHub
    author='Marianna-Karavangeli', # Your name
    license='MIT',
    packages=find_packages(), # This one is important to explain. See the notebook for a detailed explanation
    install_requires=['selenium', 'pandas', 'botocore', 'boto3', 'logging', 'sqlalchemy'], # For this project we are using two external libraries
                                                     # Make sure to include all external libraries in this argument
)