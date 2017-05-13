from setuptools import setup, find_packages

setup(name='python-tuya',
      version='0.0.1',
      description='Control and read Tuya based devices',
      url='http://github.com/python-tuya/python-tuya',
      author='Jesse Hills',
      license='MIT',
      install_requires=['paho-mqtt', 'pycrypto'],
      packages=find_packages(exclude=["dist"]),
      zip_safe=True)
