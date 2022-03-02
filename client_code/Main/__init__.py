from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
from ..Home import Home


class Main(MainTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.content_panel.add_component(Home(), full_width_row=True)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home(), full_width_row=True)







