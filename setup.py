from setuptools import setup

setup(
    name='pynite',
    version='1.0.1',
    description='An asynchronous Python API wrapper for the Fortnite API',
    long_description=open('README.md').read(),
    url='https://github.com/cree-py/pynite',
    author='SharpBit and Umbresp',
    author_email='creepy.org3301@gmail.com',
    license='MIT',
    keywords=['fortnite', 'pynite', 'api-wrapper', 'async'],
    packages=['pynite'],
    install_requires=['aiohttp','python-box']
)
