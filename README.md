# Text Summarization

Text summarization CLI application written in Python, greatly inspired by 
[this article](https://stackabuse.com/text-summarization-with-nltk-in-python).

## Usage

For Linux and macOS users: create a virtual environment and install dependencies from `requirements.txt`.

```bash
# Create a virtual environment
$ python3 -m venv env

# Activate a virtual environment
$ source env/bin/activate

# Confirm you're in the virtual environment
$ which python

# Install dependencies
$ pip3 install -r requirements.txt
```

Then, you launch the CLI application by providing two arguments: the URL you're scraping and the number of sentences
that your summary should contain, for example

```bash
$ python3 main.py 'https://en.wikipedia.org/wiki/Europe' 4
```
