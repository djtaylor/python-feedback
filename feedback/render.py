import string
from time import time
from copy import copy
from sys import stdout
from getpass import getpass
from datetime import datetime
from termcolor import colored
from colorama import init as colorama_init

class _Render(object):
    """
    Private class used to handle rendering any messages set by the
    public feedback class.
    """
    def __init__(self, **kwargs):
        
        # Initialize colorama
        colorama_init()
        
        # Default tag width
        self.width     = 9
        
        # Message / input response / kwargs
        self.msg       = None
        self.response  = {}
        self.kwargs    = kwargs
    
        # Timestamp boolean
        self.timestamp = kwargs.get('use_timestamp', False)
    
    def _get_timestamp(self):
        """
        Get a timestamp string
        """
        return datetime.fromtimestamp(time()).strftime(self.kwargs.get('timestamp_format', '%H:%M:%S'))
    
    def _get_tag(self, tag, color='white'):
        """
        Generate a tag string.
        """

        # Timestamp / tag
        timestamp  = '' if not self.timestamp else ' {} |'.format(self._get_timestamp())
        tag        = colored(string.center(tag, self.width), color)
        
        # Return the tag string
        return '[{}{}]'.format(timestamp, tag)
    
    def get_response(self, key, default=None):
        """
        Return a response variable.
        """
        return self.response.get(key, default)
    
    def set_message(self, msg):
        """
        Set the internal message variable.
        """
        self.msg = msg
    
    def show(self, tag, **kwargs):
        """
        Format the message and render depending on the tag type and color.
        Center the tag to the width defined in the class constructor.
        """
        
        # Refresh / newline flags
        line_ref  = '\r' if kwargs.get('refresh', False) else ''
        line_new  = '\n' if kwargs.get('newline', True) else ''
        
        # Tag / message
        tag       = self._get_tag(tag, kwargs.get('color', ''))
        message   = '{}{}: {}{}'.format(line_ref, tag, self.msg, line_new)
        
        # If capturing input
        if kwargs.get('input_get'):
            msg_input = '{}: {}'.format(tag, self.msg)
            
            # If using a secure prompt
            if kwargs.get('input_secure'):
                
                # Confirm the input
                if kwargs.get('input_confirm'):
                    msg_confirm = '{}: Please re-enter the value: '.format(self._get_tag('CONFIRM'))
                    
                    # Input / confirmation prompts
                    prompt = lambda: (getpass(msg_input), getpass(msg_confirm))
        
                    # Get input and confirm
                    def _get_and_confirm_input():
                        val_one, val_two = prompt()
                        if not val_one == val_two:
                            stdout.write('{}: Values do not match, please try again...\n'.format(self._get_tag('ERROR', 'red')))
                            return _get_and_confirm_input()
                        return val_one
                    self.response[kwargs.get('input_key')] = _get_and_confirm_input()
                    
                # No confirmation needed
                else:
                    self.response[kwargs.get('input_key')] = getpass(prompt=msg_input)
                
            # Plain text prompt
            else:
                
                # If parsing a yes/no answer
                if kwargs.get('input_yn', False):
                    def _get_yn_response():
                        _response = raw_input(msg_input)
                        _response = _response.lower()
                        if _response != 'y' and _response != 'n': 
                            stdout.write('{}: Response must be "y" or "n"...\n'.format(self._get_tag('ERROR', 'red')))
                            return _get_yn_response()
                        return True if _response == 'y' else False
                    self.response[kwargs.get('input_key')] = _get_yn_response()
                else:
                    self.response[kwargs.get('input_key')] = raw_input(msg_input)
            
        # Write straight to stdout
        else:
            stdout.write(message)