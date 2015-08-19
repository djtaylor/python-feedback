#!/usr/bin/env python3
from sys import path
path.append('{PYTHON_PATH}')
from feedback import Feedback

# Create new instance
feedback = Feedback()

# Test basic messages
feedback.info('Testing information message')
feedback.success('Testing success message')
feedback.warn('Testing warning message')
feedback.error('Testing error message')

# Test user input
feedback.input('Ask the user for some data: ', key='key_one')
feedback.input('Ask the user a "y" or "n" question? (y/n): ', key='key_two', yes_no=True)
feedback.input('Ask the user for a password and confirm: ', key='key_three', secure=True, confirm=True)
feedback.input('This input has a default value (123): ', key='key_four', default=123)

# Test block display and response retrieval
feedback.block([
    'This is a block of indented text, and here is some stuff to look at:',
    'Response 1: {0}'.format(feedback.get_response('key_one')),
    'Response 2: {0}'.format(feedback.get_response('key_two')),
    'Response 3: {0}'.format(feedback.get_response('key_three')),
    'Response 4: {0}'.format(feedback.get_response('key_four')),
    'And that\'s the end of this block'
], 'ABOUT')

# Create new instance with timestamp
del feedback
feedback = Feedback(use_timestamp=True)

# Test basic messages
feedback.info('Testing information message')
feedback.success('Testing success message')
feedback.warn('Testing warning message')
feedback.error('Testing error message')