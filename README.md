# Feedback Manager

A simple Python module used to display different categories of messages on the command line, as well as capturing user input. This was originally an internal module for a project of mine, but I ended up using it elsewhere, so I am splitting it off into its own project. Mainly used in Python scripts that should be run on the terminal.

### Basic Use
```python
# Import and load the handler class
import feedback
fb = feedback.Feedback()

# Displaying single line messages
fb.set('Set the message, then call the render method').info()
fb.set('Something good just happended, :-)').success()
fb.set('Something bad just happended, :-(').error()
fb.set('Better watch out, something looks fishy').warn()

# Capturing user input. Only one response is stored at a time, and must
# be retrieved after calling the input method, otherwise it will be
# overwritten at the next input method call.
fb.set('Ask the user for some data: ').input()
rsp_one = fb.get_response()
fb.set('Ask the user a "y" or "n" question? (y/n): ').input(yes_no=True)
rsp_two = fb.get_response()
fb.set('Ask the user for a password and confirm: ').input(secure=True, confirm=True)
rsp_three = fb.get_response()

# Displaying an indented block of text. Pass an array as an argument
# with one line per entry.
fb.set([
    'This is a block of indented text, and here is some stuff to look at:',
    'Response 1: {}'.format(rsp_one),
    'Response 2: {}'.format(rsp_two),
    'Response 3: {}'.format(rsp_three),
    'And that\'s the end of this block'
]).block('ABOUT')
```

This is what the output looks like from the above code snippet:
```sh
[   INFO  ]: Set the message, then call the render method
[ SUCCESS ]: Something good just happended, :-)
[  ERROR  ]: Something bad just happended, :-(
[ WARNING ]: Better watch out, something looks fishy
[  INPUT  ]: Ask the user for some data: somedata
[  INPUT  ]: Ask the user a "y" or "n" question? (y/n): h
[  ERROR  ]: Response must be "y" or "n"...
[  INPUT  ]: Ask the user a "y" or "n" question? (y/n): n
[  INPUT  ]: Ask the user for a password and confirm: 
[ CONFIRM ]: Please re-enter the value: 
[  ERROR  ]: Values do not match, please try again...
[  INPUT  ]: Ask the user for a password and confirm: 
[ CONFIRM ]: Please re-enter the value: 
[  ABOUT  ]: This is a block of indented text, and here is some stuff to look at:
             Response 1: somedata
             Response 2: False
             Response 3: secret
             And that's the end of this block
```