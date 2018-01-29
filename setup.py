<<<<<<< HEAD
from setuptools import setup

=======
from setuptools import setup, find_packages
# SharpBit told me to edit something
>>>>>>> efa02732aee43e165f56a110b2cc9f8a7a53b048
setup(
    name='pynite',
    version='1.1.3',
    description='An asynchronous Python API wrapper for the Fortnite API',
    long_description="Asynchronous python wrapper for the Fortnite API. Also, we don't yet have a good description so this empty page will have to do.",
    url='https://github.com/cree-py/pynite',
    author='SharpBit and Umbresp',
    author_email='creepy.org3301@gmail.com',
    license='MIT',
<<<<<<< HEAD
    keywords=['fortnite', 'pynite', 'api-wrapper', 'async'],
    packages=['pynite'],
    install_requires=['aiohttp==2.2.5', 'python-box==3.1.1']
=======
    keywords=['fortnite pynite api-wrapper async'],
    packages=find_packages(),
    install_requires=['aiohttp', 'python-box']
>>>>>>> efa02732aee43e165f56a110b2cc9f8a7a53b048
)
