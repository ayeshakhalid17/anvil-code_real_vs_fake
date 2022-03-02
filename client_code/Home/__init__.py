from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
from ..Form1 import Form1


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    #self.init_components(**properties)
    pass
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('Form1')
    pass

