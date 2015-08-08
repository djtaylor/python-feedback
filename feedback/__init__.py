# -*- coding: utf-8 -*-
__version__ = '0.1-1'
from getpass import getpass
from common import _Common
from render import _Render

class Feedback(_Common):
    def __init__(self, **kwargs):
        super(Feedback, self).__init__()
        
        # Render manager / handler
        self.render   = _Render(**kwargs)
    
    def _set_message(self, msg):
        """
        Set and store the message.
        """
        if isinstance(msg, str):
            _msg = msg
        if isinstance(msg, list):
            indent   = ' ' * 3
            _msg = '\n\n'
            for line in msg:
                _msg += '{}{}\n'.format(indent, line)
            _msg += '\n'
        
        # Pass the message to the rendering handler
        self.render.set_message(_msg)
    
    def get_response(self, key, default=None):
        """
        Return then clear the response variable.
        """
        return self.render.get_response(key, default)
        
    def success(self, msg): 
        """
        Display a success message on the screen.
        """
        self._set_message(msg)
        self.render.show('SUCCESS', color=self.color['green'])
        
    def warn(self, msg): 
        """
        Display a warning message on the screen.
        """
        self._set_message(msg)
        self.render.show('WARNING', color=self.color['yellow'])
        
    def error(self, msg): 
        """
        Display an error message on the screen.
        """
        self.render.show('ERROR', color=self.color['red'])

    def block(self, msg, label='INFO'):
        """
        Display a block of indented text.
        """
        self._set_message(msg)
        self.render.show(label, newline=False)

    def input(self, msg, key, secure=False, confirm=False, yes_no=False):
        """
        Display an input prompt on the screen.
        """
        self._set_message(msg)
        self.render.show('INPUT', input_key=key, input_get=True, input_secure=secure, input_confirm=confirm, input_yn=yes_no)

    def info(self, msg): 
        """
        Display an informational message on the screen.
        """
        self._set_message(msg)
        self.render.show('INFO')