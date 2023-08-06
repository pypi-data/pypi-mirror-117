# from setuptools import setup, find_packages
from setuptools import setup, Extension, find_packages

 
classifiers = [
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='propertypro scrapper',
  version='1.0',
  description='A scraper that helps scrape a housing website propertypro',
  long_description=open('README.txt').read(),
  url='https://github.com/Ifyokoh/',  
  author='Ifeoma Okoh',
  author_email='odibest1893@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='scraper', 
  packages=find_packages()
)
