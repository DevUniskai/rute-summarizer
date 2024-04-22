from ._anvil_designer import Form1Template
from anvil import *
from datetime import date

def handle_rute(text):
  flag = 0
  output = ""
  split_enter = text.strip().split("\n")
  temp_alamat = ""
  counter_flag = 0

  today = date.today()
  today_date = today.strftime("%d %B %Y")
  today_date = str(today_date).upper()
  output += "*RUTE UNISKAI " + today_date + "*\n\n\n"
  for idx, text in enumerate(split_enter):
    split_tab = text.split("\t")
    length = len(split_tab)

    if length == 1:
      temp_alamat = split_tab[0]
      continue
    
    if idx == len(split_enter)-1:
      counter_flag = 1

    alamat = ' '.join(split_tab[0:length-5+counter_flag])
    nama = split_tab[length-5+counter_flag].strip()
    no_hp = split_tab[length-4+counter_flag]
    keperluan = split_tab[length-3+counter_flag].strip()
    pic = split_tab[length-2+counter_flag].strip()
    # prioritas = split_tab[length-1+counter_flag].strip()

    if len(temp_alamat) > 0:
      alamat += temp_alamat + alamat
      temp_alamat = ""
    output += str(flag+1) + " " + nama + "\n" + alamat + "\n"
    if len(no_hp) > 0:
      output += no_hp + "\n"
    output += pic + " (" + keperluan + ")\n\n"
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
    pass