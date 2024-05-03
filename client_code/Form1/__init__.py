from ._anvil_designer import Form1Template
from anvil import *
from datetime import date

def handle_rute(text):
  flag = 0
  today = date.today()

  output = "*RUTE UNISKAI " + today.strftime("%d-%b-%Y").upper() + "*\n\n"
  
  split_enter = text.strip().split("\n")
  temp_alamat = ""
  counter_flag = 0
  for idx, text in enumerate(split_enter):
    split_tab = text.split("\t")
    print(split_tab)
    length = len(split_tab)

    if length == 1:
      temp_alamat = split_tab[0]
      continue

    alamat = split_tab[0]
    nama = split_tab[1].strip()
    no_hp = split_tab[2]
    keperluan = split_tab[3].strip()
    pic = split_tab[4].strip()
    prioritas=""
    if(len(split_tab) == 6):
      prioritas = split_tab[5].strip()

    if len(temp_alamat) > 0:
      alamat += temp_alamat + alamat
      temp_alamat = ""
    output += str(flag+1) + " " + nama + "\n" + alamat + "\n"
    if len(no_hp) > 0:
      output += no_hp + "\n"
    output += pic + " (" + keperluan + ")\n"

    if len(prioritas) > 0:
      output += "_"+ prioritas.upper() + "_\n"
    output += "\n"
    flag+=1

  return output
  
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def input_text_area_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    input = self.input_text_area.text
    if input:
      
      summary = None
      summary = handle_rute(input)
      # print("summary", summary)
      if summary:
        self.result.visible = True
        self.result.text = summary
        
    pass

  def clear_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.input_text_area.text = ""
    pass
  
  def copy_click(self, **event_args):
    """This method is called when the button is clicked"""

    get_open_form().call_js("cpy", self.result.text)
    n = Notification("Copied to Clipboard", title="Status", style="success")
    n.show()
