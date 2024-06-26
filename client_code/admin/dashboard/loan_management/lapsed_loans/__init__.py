from ._anvil_designer import lapsed_loansTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class lapsed_loans(lapsed_loansTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.fin_loan_details.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []
    self.list_6 = []
    self.list_7 = []
    self.list_8 = []
    self.list_9 = []
    self.list_10 = []
    
    
    for i in self.data:
      a+=1
      self.list_1.append(i['loan_id'])
      self.list_2.append(i['borrower_customer_id'])
      self.list_3.append(i['borrower_full_name'])
      self.list_4.append(i['loan_updated_status'])
      self.list_5.append(i['lender_full_name'])
      self.list_6.append(i['lender_customer_id'])
      self.list_7.append(i['interest_rate'])
      self.list_8.append(i['tenure'])
      self.list_9.append(i['loan_amount'])
      self.list_10.append(i['lender_accepted_timestamp'])
    print(a)

    self.result = []
    self.index = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      b = -1
      for i in self.list_4:
        b+=1
        if i == "lapsed loan" or i == 'Lapsed loan' or i == "Lapsed Loan" or i == 'lapsed' or i == 'Lapsed':
          self.index.append(b)
          
      for i in self.index:
        self.result.append({'loan_id' : self.list_1[i], 'coustmer_id' : self.list_2[i], 'full_name' : self.list_3[i], 'loan_status' : self.list_4[i],'lendor_full_name' : self.list_5[i],'lender_customer_id':self.list_6[i],'interest_rate':self.list_7[i],'tenure':self.list_8[i],'loan_amount':self.list_9[i],'lender_timestamp':self.list_10[i]})

      self.repeating_panel_2.items = self.result


  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.loan_management')

  def repeating_panel_1_show(self, **event_args):
    """This method is called when the RepeatingPanel is shown on the screen"""
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
