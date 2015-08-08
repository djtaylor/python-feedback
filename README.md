# Feedback Manager

A simple Python module used to display different categories of messages on the command line, as well as capturing user input. This was originally an internal module for a project of mine, but I ended up using it elsewhere, so I am splitting it off into its own project. Mainly used in Python scripts that should be run on the terminal.

### Installation
```sh
pip install feedback
```

### Basic Use
```python
# Import and load the handler class
from feedback import Feedback
fb_no_ts = Feedback()

# Create an instance using a timestamp
fb_ts    = Feedback(use_timestamp=True)

# Create an instance using a custom timestamp
fb_tsc   = Feedback(use_timestamp=True, timestamp_format='%Y-%m-%d %H:%M:%S')

# Displaying single line messages
fb_no_ts.info('Set the message, then call the render method')
fb_no_ts.success('Something good just happended, :-)')
fb_no_ts.error('Something bad just happended, :-(')
fb_no_ts.warn('Better watch out, something looks fishy')

# Capturing user input.
fb_no_ts.input('Ask the user for some data: ', key='key_one')
fb_no_ts.input('Ask the user a "y" or "n" question? (y/n): ', key='key_two', yes_no=True)
fb_no_ts.input('Ask the user for a password and confirm: ', key='key_three', secure=True, confirm=True)

# Displaying an indented block of text. Pass an array as an argument
# with one line per entry.
fb_no_ts.block([
    'This is a block of indented text, and here is some stuff to look at:',
    'Response 1: {}'.format(feedback.get_response('key_one')),
    'Response 2: {}'.format(feedback.get_response('key_one')),
    'Response 3: {}'.format(feedback.get_response('key_one')),
    'And that\'s the end of this block'
], 'ABOUT')
```