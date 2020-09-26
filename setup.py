from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wordlistraider',
    version='1.0',
    python_requires='>=3.7',
    install_requires=[
        "atomicwrites==1.4.0",
        "attrs==20.1.0",
        "colorama==0.4.3",
        "iniconfig==1.0.1",
        "more-itertools==8.5.0",
        "packaging==20.4",
        "pluggy==0.13.1",
        "py==1.9.0",
        "pyparsing==2.4.7",
        "pytest==6.0.1",
        "six==1.15.0",
        "toml==0.10.1"
    ],
    packages=find_packages()+['.'],
    include_package_data=True,
    url='https://github.com/GregorBiswanger/WordlistRaider',
    license='MIT',
    description='Returns a selection of words that matches the passed conditions in an existing list.',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='wordlist passwordlist cutter raider',
    entry_points={
        'console_scripts': [
            'wordlistraider = wordlistraider.wordlistraider',
        ],
    },
)
