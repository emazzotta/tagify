from distutils.core import setup
setup(
    name='tagify',
    version='0.1.9',
    description='parse yaml front matter and write osx tags',
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
