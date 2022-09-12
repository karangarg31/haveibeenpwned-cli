# haveibeenpwned-cli
This is a Python based command line interface that runs on Linux for the service haveibeenpwned.com. Have I been Pwned is a brilliant service which when given account name (email address or phone number) returns the list of breaches

## Background
This effort has started as a small project - but I definitely intend to keep adding to it. Additionally, haveibeenpwned.com needs an API key for it to be used here. I have currently set up the keyu inside the code, but I am going to be removing it in near future. User will be able to use their own key by setting an environment variable in Linux

## Pre Requisites
To run this app, you will need the following (languages or modules) installed:
* Python 3
* requests
* tabulate

There are a few other modules as well, but they are usually available with Python distributions out of the box.

## Usage
To see how to use the API - please execute the following command to see all available options
`./haveibeenpwned-cli.py -h`

Thank you for reading - hopw you enjoy using this little app.
