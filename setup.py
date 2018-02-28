from setuptools import setup, find_packages

setup(
    name='pynite',
    version='1.4.0',
    description='An async Python API wrapper for the Fortnite API',
    long_description='Powered by fortnitetracker.com. Async python 3.5+',
    url='https://github.com/cree-py/pynite',
    author='SharpBit & Umbresp',
    author_email='creepy.org3301@gmail.com',
    license='MIT',
    keywords=['fortnite, pynite, api-wrapper, async'],
    packages=find_packages(),
    install_requires=['aiohttp', 'python-box']
)
