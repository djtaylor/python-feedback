# Feedback Manager

A simple Python module used to display different categories of messages on the command line, as well as capturing user input. This was originally an internal module for a project of mine, but I ended up using it elsewhere, so I am splitting it off into its own project. Mainly used in Python scripts that should be run on the terminal.

### Basic Use
```python
# Import and load the handler class
from feedback import Feedback
feedback = Feedback()

# Create an instance using a timestamp
feedback_ts  = Feedback(use_timestamp=True)

# Create an instance using a custom timestamp
feedback_tsc = Feedback(use_timestamp=True, timestamp_format='%Y-%m-%d %H:%M:%S')

# Displaying single line messages
fb.set('Set the message, then call the render method').info()
fb.set('Something good just happended, :-)').success()
fb.set('Something bad just happended, :-(').error()
fb.set('Better watch out, something looks fishy').warn()

# Capturing user input.
fb.set('Ask the user for some data: ').input('key_one')
fb.set('Ask the user a "y" or "n" question? (y/n): ').input('key_two', yes_no=True)
fb.set('Ask the user for a password and confirm: ').input('key_three', secure=True, confirm=True)

# Displaying an indented block of text. Pass an array as an argument
# with one line per entry.
fb.set([
    'This is a block of indented text, and here is some stuff to look at:',
    'Response 1: {}'.format(feedback.get_response('key_one')),
    'Response 2: {}'.format(feedback.get_response('key_one')),
    'Response 3: {}'.format(feedback.get_response('key_one')),
    'And that\'s the end of this block'
]).block('ABOUT')
```