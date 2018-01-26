from setuptools import setup

setup(
    name='pynite',
    version='1.0.0',
    description='A Python API wrapper for for fortnite api',
    long_description=open('README.md').read(),
    url='https://github.com/cree-py/pynite',
    author='SharpBit&Umbresp',
    author_email='Insert email lol',
    license='MIT',
    keywords=['fortnite', 'pynite', 'api-wrapper', 'async'],
    packages=['pynite'],
    install_requires=['aiohttp','python-box']
)
