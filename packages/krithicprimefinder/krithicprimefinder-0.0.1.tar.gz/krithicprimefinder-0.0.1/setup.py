from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='krithicprimefinder',
  version='0.0.1',
  description='To check prime number and do stuffs in prime',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Krithic Sugumar',
  author_email='krithic2001@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='prime', 
  packages=find_packages(),
  install_requires=[''] 
)