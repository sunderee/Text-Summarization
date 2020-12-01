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
[nltk_data] Downloading package stopwords to
[nltk_data]     /Users/peteraleksanderbizjak/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package punkt to
[nltk_data]     /Users/peteraleksanderbizjak/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
In the course of the 5th century BC, several of the Greek city states would ultimately check the Achaemenid Persian
advance in Europe through the Greco-Persian Wars, considered a pivotal moment in world history, as the 50 years of peace
that followed are known as Golden Age of Athens, the seminal period of ancient Greece that laid many of the foundations
of Western civilisation. According to UN population projection, Europe's population may fall to about 7% of world
population by 2050, or 653 million people (medium variant, 556 to 777 million in low and high variants, respectively).
European integration is the process of political, legal, economic (and in some cases social and cultural) integration of
European states as it has been pursued by the powers sponsoring the Council of Europe since the end of World War II The
European Union has been the focus of economic integration on the continent since its foundation in 1993. Both world wars
took place for the most part in Europe, contributing to a decline in Western European dominance in world affairs by the
mid-20th century as the Soviet Union and the United States took prominence.
```