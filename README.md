# ProblemsHunter
The bot will find problems(sorted by number of submissions) of given ratings that are unsolved by a set of users.

## Prerequisites

[Python3](https://www.python.org/downloads/)

[Google Chrome](https://www.google.com/intl/en_in/chrome/)

To install Requirements run command:
```bash
pip install -r requirements.txt
```

## Usage

1.Run it using this command:

```bash
python3 app.py
```
2.Enter usernames separated by space.

3.Enter the problem ratings separated by space.

The bot will then take some time to process and will show results in terminal int the format:

```bash
rating: link to problem
```


# Note:
To avoid webdriver from downloading again and again, download [chrome web driver](http://chromedriver.chromium.org/downloads?tmpl=%2Fsystem%2Fapp%2Ftemplates%2Fprint%2F&showPrintDialog=1) for your chrome version and extract it to a location and paste the location in variable PATH in app.py.

# UPDATE 1:
Added the feature to avoid returning problems that were ever featched by the bot before.It was needed because mashup problems does are not shown in user submissions.The file solved.txt is for storing all the problems returned by the bot.

# UPDATE 2:
Added the feature to add participants directly from the mashup contest page.
