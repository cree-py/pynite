from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name='pynite',
    version='1.2.0',
    description='An async Python API wrapper for the Fortnite API',
    long_description=long_description,
    url='https://github.com/cree-py/pynite',
    author='SharpBit & Umbresp',
    author_email='creepy.org3301@gmail.com',
    license='MIT',
    keywords=['fortnite, pynite, api-wrapper, async'],
    packages=find_packages(),
    install_requires=['aiohttp', 'python-box']
)
