from setuptools import setup, find_packages
from scastpy import __version__, __author__


with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


def long_description():
    with open('README.md', 'r') as readme:
        return readme.read()


setup(
    name='scastpy',
    version=__version__,
    packages=find_packages(),

    author=__author__,
    author_email='ricterzheng@gmail.com',
    keywords=['DLNA', 'ScreenCast', 'SSDP', 'Media Player'],
    description='A simple digital media player written by Python',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/RicterZ/scastpy',
    download_url='https://github.com/RicterZ/scastpy/tarball/master',
    include_package_data=True,
    zip_safe=False,

    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'scastpy = scastpy.main:main',
        ]
    },
    license='MIT',
)