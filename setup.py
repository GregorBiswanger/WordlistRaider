from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wordlistraider',
    version='1.0',
    python_requires='>=3.7',
    install_requires=[
        "colorama==0.4.3",
        "more_termcolor",
        "pyfiglet"
    ],
    packages=find_packages(),
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
