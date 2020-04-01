from os import path

from setuptools import find_packages, setup


def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='iitb_oauth',
    version='1.0',
    author='Nautatva Navlakha',
    author_email="nnautatva@gmail.com",
    url="https://github.com/nautatva/iitb_oauth/",
    description="Django app for authentication using IIT Bombay gymkhana SSO.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    python_requires='>1.1.1',
    install_requires=[
        'Django',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "License :: OSI Approved :: MIT License",
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
    packages=find_packages(exclude=('*tests*', 'example*', )),
)
