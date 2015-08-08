#!/usr/bin/python
from feedback import Feedback

"""
Basic script used to assist in testing changes to the module.
"""

# Create a new instance
feedback = Feedback()

# Test INFO / SUCCESS / WARN / ERROR
feedback.info('Initializing test without timestamp...')
feedback.info('Testing informational message')
feedback.success('Testing success message')
feedback.warn('Testing warning message')
feedback.error('Testing error message')

# Test INPUT
feedback.input('Testing unconfirmed plain text input (please enter a value): ', key='a')
feedback.input('Testing unconfirmed secure input (please enter a value): ', key='b', secure=True)
feedback.input('Testing confirmed secure input (please enter a value): ', key='c', secure=True, confirm=True)
feedback.input('Testing yes/no input (please enter a value): ', key='d', yes_no=True)

# Test BLOCK
feedback.block([
  'Input one response: {}'.format(feedback.get_response('a')),
  'Input two response: {}'.format(feedback.get_response('b')),
  'Input three response: {}'.format(feedback.get_response('c')),
  'Input four response: {}'.format(feedback.get_response('d'))
], 'RESULTS')

# Test with timestamp
del feedback
feedback = Feedback(use_timestamp=True)
feedback.info('Initializing test with timestamp...')
feedback.info('Testing informational message')
feedback.success('Testing success message')
feedback.warn('Testing warning message')
feedback.error('Testing error message')

# Test INPUT
feedback.input('Testing unconfirmed plain text input (please enter a value): ', key='a')
feedback.input('Testing unconfirmed secure input (please enter a value): ', key='b', secure=True)
feedback.input('Testing confirmed secure input (please enter a value): ', key='c', secure=True, confirm=True)
feedback.input('Testing yes/no input (please enter a value): ', key='d', yes_no=True)

# Test BLOCK
feedback.block([
  'Input one response: {}'.format(feedback.get_response('a')),
  'Input two response: {}'.format(feedback.get_response('b')),
  'Input three response: {}'.format(feedback.get_response('c')),
  'Input four response: {}'.format(feedback.get_response('d'))
], 'RESULTS')

# Test complete
feedback.success('All tests complete!')
