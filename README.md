# ProblemsHunter
The bot will find problems(sorted by number of submissions) of given ratings that are unsolved by a set of users.

## Prerequisites

[Python3](https://www.python.org/downloads/)

[Google Chrome](https://www.google.com/intl/en_in/chrome/)

Install Requirements
```bash
pip install -r requirements.txt
```

## Usage

1.Run it using this command.

```bash
python3 test.py
```
2.Enter usernames separated by space.

3.Enter the problem ratings separated by space.

The bot will then take some time to process and will show results in terminal int the format:

```bash
rating: link to problem
```

To see the bot working comment line no. 54.

# Note:
To avoid webdriver from downloading again and again, download [chrome web driver](http://chromedriver.chromium.org/downloads?tmpl=%2Fsystem%2Fapp%2Ftemplates%2Fprint%2F&showPrintDialog=1) for your chrome version and extract it to a location and paste the location in variable PATH and replace line 55 in app.py with:

```bash
driver = webdriver.Chrome(PATH, options=chrome_options)
```
