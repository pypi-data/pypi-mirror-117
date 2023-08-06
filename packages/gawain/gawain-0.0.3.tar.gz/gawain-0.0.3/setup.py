import re

from setuptools import setup


version = ''
with open('gawain/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()



if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()


setup(
    name='gawain',
    author='sinkaroid',
    author_email='anakmancasan@gmail.com',
    version='0.0.3',
    long_description=readme,
    url='https://github.com/sinkaroid/gawain',
    packages=['gawain'],
    license='MIT',
    description='Asyncio booru wrapper with spell blocker',
    include_package_data=True,
    keywords = ['booru', 'wrapper'],
    install_requires=requirements
)