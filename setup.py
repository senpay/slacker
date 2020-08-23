import os
from setuptools import setup
from slacker2 import constants


with open('README.rst') as f:
    readme = f.read()


lib_folder = os.path.dirname(os.path.realpath(__file__))
requirements_txt = os.path.join(lib_folder, 'requirements.txt')
with open(requirements_txt) as f:
    install_requires = list(f.read().splitlines())

setup(
    name='slacker2',
    version=constants.VERSION,
    packages=['slacker2'],
    description='Slack API client, fork of slacker',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Oktay Sancak, Alexander Pushkarev',
    author_email='oktaysancak@gmail.com, alexspush@gmail.com',
    url='http://github.com/senpay/slacker/',
    install_requires=install_requires,
    setup_requires=install_requires,
    license='http://www.apache.org/licenses/LICENSE-2.0',
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='slack api'
)
