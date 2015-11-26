# -*- coding: utf-8 -*-
__version__ = '0.1-7'
import logging
from .render import _Render

class Feedback(object):
    def __init__(self, **kwargs):
        
        # Render manager / handler
        self.render   = _Render(**kwargs)
    
        # Logging attributes
        self._logger  = self._set_logger()
    
    def _log(self, msg, lvl):
        """
        Log a message
        """
        if self._logger:
            
            # Make sure the log level is valid
            if not hasattr(self._logger, lvl):
                raise Exception('Invalid log level: {0}'.format(lvl))
            _log = getattr(self._logger, lvl)
            
            # Log the message
            _log(msg)
    
    def _set_logger(self):
        """
        Option for setting up a logger.
        """
        log_attrs = self.kwargs.get('log', None)
        
        # Look for attributes
        if not log_attrs:
            return None
        
        # Must be in dictionary format
        if not isinstance(log_attrs, dict):
            raise Exception('Attribute <log> must be a dictionary')
    
        # Logger name / file / format / date format
        log_name     = log_attrs.get('name', None)
        log_file     = log_attrs.get('file', None)
        log_fmt      = log_attrs.get('format', '%(asctime)s %(name)s - %(levelname)s: %(message)s')
        log_date_fmt = log_attrs.get('date_format', '%d-%m-%Y %I:%M:%S')
        log_level    = log_attrs.get('level', 'INFO')

        # Log name and file required
        if not log_name or not log_file:
            raise Exception('Log <name> and <file> attributes required')

        # Set the logger module name
        logger = logging.getLogger(log_name)
        logger.setLevel(getattr(logging, log_level))
        
        # Log file handler
        lfh = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=10*1024*1024, backupCount=5)
        logger.addHandler(lfh)
        
        # Set the format
        lfm = logging.Formatter(fmt=log_fmt, datefmt=log_date_fmt)
        lfh.setFormatter(lfm)

        # Return the logger
        return logger
    
    def _set_message(self, msg):
        """
        Set and store the message.
        """
        if isinstance(msg, list):
            indent   = ' ' * 3
            _msg = '\n\n'
            for line in msg:
                _msg += '{0}{1}\n'.format(indent, line)
            _msg += '\n'
        else:
            _msg = msg
        
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
        self._log(msg, 'info')
        self._set_message(msg)
        return self.render.show('SUCCESS', color='green')
        
    def warn(self, msg): 
        """
        Display a warning message on the screen.
        """
        self._log(msg, 'warning')
        self._set_message(msg)
        return self.render.show('WARNING', color='yellow')
        
    def error(self, msg): 
        """
        Display an error message on the screen.
        """
        self._log(msg, 'error')
        self._set_message(msg)
        return self.render.show('ERROR', color='red')

    def block(self, msg, label='INFO'):
        """
        Display a block of indented text.
        """
        self._set_message(msg)
        return self.render.show(label, newline=False, color='white')

    def input(self, msg, key, default=None, secure=False, confirm=False, yes_no=False):
        """
        Display an input prompt on the screen.
        """
        self._log(msg, 'info')
        self._set_message(msg)
        return self.render.show('INPUT', 
            color         = 'white', 
            default       = default, 
            input_key     = key, 
            input_get     = True, 
            input_secure  = secure, 
            input_confirm = confirm, 
            input_yn      = yes_no
        )

    def info(self, msg): 
        """
        Display an informational message on the screen.
        """
        self._log(msg, 'info')
        self._set_message(msg)
        return self.render.show('INFO', color='white')