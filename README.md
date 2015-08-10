# Feedback Manager

A simple Python module used to display different categories of messages on the command line, as well as capturing user input. This was originally an internal module for a project of mine, but I ended up using it elsewhere, so I am splitting it off into its own project. Mainly used in Python scripts that should be run on the terminal.

### Installation (APT)
Add the following sources to your apt sources configuration file:
```
deb http://ppa.launchpad.net/djtaylor13/main/ubuntu trusty main 
deb-src http://ppa.launchpad.net/djtaylor13/main/ubuntu trusty main
```
Next import the public key, update software sources, and install:
```sh
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D4409661DAA6AF94
$ sudo apt-get update
# Python 2
$ sudo apt-get install python-feedback
# Python 3
$ sudo apt-get install python3-feedback
```
### Installation (PIP)
```sh
# Python 2
$ sudo pip install feedback
# Python 3
$ sudo pip3 install feedback 
```

### Basic Use
```python
# Import and load the handler class
from feedback import Feedback

"""
Create an instance of the feedback handler:

Parameters
----------
use_timestamp : bool
   Enable or disable the timestamp in the message tag.
timestamp_format : str
   Set a custom timestamp format (default is '%H:%M:%S')
"""
feedback = Feedback()

# Displaying single line messages
feedback.info('Set the message, then call the render method')
feedback.success('Something good just happended, :-)')
feedback.warn('Better watch out, something looks fishy')
feedback.error('Something bad just happended, :-(')

# Capturing user input.
feedback.input('Ask the user for some data: ', key='key_one')
feedback.input('Ask the user a "y" or "n" question? (y/n): ', key='key_two', yes_no=True)
feedback.input('Ask the user for a password and confirm: ', key='key_three', secure=True, confirm=True)

# Displaying an indented block of text. Pass an array as an argument
# with one line per entry.
feedback.block([
    'This is a block of indented text, and here is some stuff to look at:',
    'Response 1: {}'.format(feedback.get_response('key_one')),
    'Response 2: {}'.format(feedback.get_response('key_one')),
    'Response 3: {}'.format(feedback.get_response('key_one')),
    'And that\'s the end of this block'
], 'ABOUT')
```