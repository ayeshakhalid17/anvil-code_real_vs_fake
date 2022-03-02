from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def file_loader_1_change(self, file, **event_args):
       uploaded_image=self.file_loader_1.file
       self.upload_image.source=uploaded_image
       if uploaded_image=="_/theme/placeholder.png":
        self.primary_color_1.remover_event_handler()


  def primary_color_1_click(self, **event_args):
      result = anvil.server.call('classify',self.upload_image.source)
      if result=='horse':
        self.rich_text_1.content="Non-living Object\n Fake Horse"
      elif result=='realhorse':
        self.rich_text_1.content="Living Object\n Real Horse"
      elif result=='fakehuman':
        self.rich_text_1.content="Non-living Object\n Fake Human"
      elif result=='realhuman':
        self.rich_text_1.content="Living Object\n Real Human"
      elif result=='toycar':
        self.rich_text_1.content="Non-living Object\n Fake Car"
      elif result=='realcar':
        self.rich_text_1.content="Non-living Object\n Real Car"
      else:
        self.rich_text_1.content="Enter a valid category object\n Car, Horse or Human"

  def primary_color_2_click(self, **event_args):
    self.upload_image.source="_/theme/placeholder.png"
    self.rich_text_1.content="Real or fake?"
    self.file_loader_1.text="Upload Image"







