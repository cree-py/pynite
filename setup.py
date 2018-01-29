from setuptools import setup, find_packages
setup(
    name='pynite',
    version='1.1.5',
    description='An async Python API wrapper for the Fortnite API',
    long_description="async python wrapper for the Fortnite API. Also, we don't yet have a good description so this empty page will have to do.",
    url='https://github.com/cree-py/pynite',
    author='SharpBit & Umbresp',
    author_email='creepy.org3301@gmail.com',
    license='MIT',
    keywords=['fortnite, pynite, api-wrapper, async'],
    packages=find_packages(),
    install_requires=['aiohttp', 'python-box']
)
