#!/usr/bin/python
from feedback import Feedback

"""
Basic script used to assist in testing changes to the module.
"""

# Create a new instance
feedback = Feedback()

# Test INFO / SUCCESS / WARN / ERROR
feedback.set('Initializing test without timestamp...').info()
feedback.set('Testing informational message').info()
feedback.set('Testing success message').success()
feedback.set('Testing warning message').warn()
feedback.set('Testing error message').error()

# Test INPUT
feedback.set('Testing unconfirmed plain text input (please enter a value): ').input('a')
feedback.set('Testing unconfirmed secure input (please enter a value): ').input('b', secure=True)
feedback.set('Testing confirmed secure input (please enter a value): ').input('c', secure=True, confirm=True)
feedback.set('Testing yes/no input (please enter a value): ').input('d', yes_no=True)

# Test BLOCK
feedback.set([
  'Input one response: {}'.format(feedback.get_response('a')),
  'Input two response: {}'.format(feedback.get_response('b')),
  'Input three response: {}'.format(feedback.get_response('c')),
  'Input four response: {}'.format(feedback.get_response('d'))
]).block('RESULTS')

# Test with timestamp
del feedback
feedback = Feedback(use_timestamp=True)
feedback.set('Initializing test with timestamp...').info()
feedback.set('Testing informational message').info()
feedback.set('Testing success message').success()
feedback.set('Testing warning message').warn()
feedback.set('Testing error message').error()

# Test INPUT
feedback.set('Testing unconfirmed plain text input (please enter a value): ').input('a')
feedback.set('Testing unconfirmed secure input (please enter a value): ').input('b', secure=True)
feedback.set('Testing confirmed secure input (please enter a value): ').input('c', secure=True, confirm=True)
feedback.set('Testing yes/no input (please enter a value): ').input('d', yes_no=True)

# Test BLOCK
feedback.set([
  'Input one response: {}'.format(feedback.get_response('a')),
  'Input two response: {}'.format(feedback.get_response('b')),
  'Input three response: {}'.format(feedback.get_response('c')),
  'Input four response: {}'.format(feedback.get_response('d'))
]).block('RESULTS')

# Test complete
feedback.set('All tests complete!').success()
