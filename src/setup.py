from setuptools import setup, find_packages

setup(name='python-tuya',
      version='1.0.0',
      description='Control and read Tuya based devices',
      url='http://github.com/jesserockz/python-tuya',
      author='Jesse Hills',
      license='MIT',
      install_requires=['requests>=2.0'],
      packages=find_packages(exclude=["dist"]),
      zip_safe=True)
