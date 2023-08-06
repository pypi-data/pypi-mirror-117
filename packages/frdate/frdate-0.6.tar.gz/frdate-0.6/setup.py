from setuptools import setup

setup(name='frdate',
      version='0.6',
      description='From string input to french date',
      author='Thibaut Spriet',
      author_email='thibaut@spriet.online',
      url='https://github.com/ThbtSprt/frdate',
      package_dir = {'': 'src'},
      packages=['frdate'],
      install_requires=["euros","dateutils"]
     )
