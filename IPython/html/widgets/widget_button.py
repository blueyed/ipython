"""ButtonWidget class.  

Represents a button in the frontend using a widget.  Allows user to listen for
click events on the button and trigger backend code when the clicks are fired.
"""
#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from .widget import DOMWidget, CallbackDispatcher
from IPython.utils.traitlets import Unicode, Bool

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------
class ButtonWidget(DOMWidget):
    _view_name = Unicode('ButtonView', sync=True)

    # Keys
    description = Unicode('', help="Description of the button (label).", sync=True)
    disabled = Bool(False, help="Enable or disable user changes.", sync=True)
    
    def __init__(self, **kwargs):
        """Constructor"""
        super(ButtonWidget, self).__init__(**kwargs)
        self._click_handlers = CallbackDispatcher()
        self.on_msg(self._handle_button_msg)

    def on_click(self, callback, remove=False):
        """Register a callback to execute when the button is clicked.

        The callback will be called with one argument,
        the clicked button widget instance.

        Parameters
        ----------
        remove : bool (optional)
            Set to true to remove the callback from the list of callbacks."""
        self._click_handlers.register_callback(callback, remove=remove)

    def _handle_button_msg(self, _, content):
        """Handle a msg from the front-end.

        Parameters
        ----------
        content: dict
            Content of the msg."""
        if content.get('event', '') == 'click':
            self._click_handlers(self)
