from distutils.core import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tagify',
    version='0.2.4',
    description='parse yaml front matter and write osx tags',
    long_description=long_description,
    author='Simon Breiter, Emanuele Mazzotta',
    author_email='hello@simonbreiter.com, hello@emanuelemazzotta.com',
    license='MIT',
    url='https://gitlab.com/sibr/tagify',
    keywords=['yaml', 'front matter', 'osx', 'tags'],
    classifiers=[],
    py_modules=['tagify'],
    entry_points={
        'console_scripts': [
            'tagify=tagify:main',
        ],
    },
)
