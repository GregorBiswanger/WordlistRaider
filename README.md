WordlistRaider
=======
WordlistRaider is a Python tool for preparing existing wordlists. As an example we have a GB big wordlist and we only want passwords with a length of at least 8 characters. This optimizes word lists and saves unnecessary requests.
## Screenshots

![WordlistRaider](https://github.com/GregorBiswanger/WordlistRaider/blob/master/screenshot.jpg "WordlistRaider in action")

## Installation

```
git clone https://github.com/GregorBiswanger/WordlistRaider.git
```

## Recommended Python Version:

WordlistRider currently supports **Python 3**.

* The recommended version for Python 3 is **3.8.x**

## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-w            | --wordlist      | The wordlist to raid
-t            | --target  | Path to the target wordlist
--min            | --minlength       | Minimum length of password (default: 8)
--max            | --maxlength     | Maximum length of password
-n            | --numbers     | Password must include numbers (default: false)
-s            | --specialcharacters     | Includes passwords with special characters (default: false)
-h            | --help        | show the help message and exit

### Example

* To list all the basic options and switches use -h switch:

```python WordlistRaider.py -h```

* Use passwords with at least 10 characters, they can contain numbers and special characters:

``python WordlistRaider.py -w source.txt -t target.txt --min 10 -n true -s true``

## License

WordlistRaider is licensed under the MIT license. take a look at the [LICENSE](https://github.com/GregorBiswanger/WordlistRaider/blob/master/LICENSE) for more information.


## Version
**Current version is 1.0**