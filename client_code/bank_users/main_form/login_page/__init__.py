from ._anvil_designer import login_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...user_form import user_module
from .. import main_form_module


class login_page(login_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    login_input = self.text_box_1.text.strip()
        # Get the password
    password = self.text_box_2.text.strip()
        # Get the user based on login input
    user = anvil.server.call('get_user_for_login',login_input)

        # Check if user exists and password matches
    if user is not None and user['password'] == password:
            print(login_input)
            if login_input:
                user_email = login_input
                print(user_email)
                check_user_already_exist = user_module.check_user_profile(user_email)
                print(check_user_already_exist)
                if check_user_already_exist is None:
                    print("main if statement was executed")
                    user_module.add_email_and_user_id(user_email)
                    main_form_module.email = user_email
                    main_form_module.flag = True
                    open_form('bank_users.main_form.basic_registration_form')
                else:
                    check_user_registration = user_module.check_user_registration_form_done_or_not_engine(user_email)
                    print("main else statement was executed")
                    user_profile_e = app_tables.fin_user_profile.get(email_user=user_email)
                    main_form_module.email = user_email
                    main_form_module.userId = user_module.find_user_id(user_email)
                    if user_profile_e is not None:
                        user_type = user_profile_e['usertype']
                        if user_type == 'admin' or user_type == 'super admin':
                            open_form('admin.dashboard')
                        elif user_type == 'lender':
                            open_form('lendor_registration_form.dashboard')
                        elif user_type == 'borrower':
                            if user_profile_e['one_time_settlement'] != True:
                                open_form('borrower_registration_form.dashboard')
                            elif user_profile_e['one_time_settlement'] == True:
                                open_form('borrower_registration_form.ots_dashboard')

                        elif user_profile_e['form_count'] >= 0:
                          open_form('bank_users.user_form')
                        else:
                            open_form('bank_users.main_form.basic_registration_form')
                    else:
                        # Handle the case when user_profile_e is None
                        open_form('bank_users.user_form')
            else:
                # Handle the case when current_user is None
                open_form('bank_users.user_form')


    else:
      self.error_label.text = 'Invalid email or password'
      self.error_label.visible = True


  def check_box_1_change(self, **event_args):
   #  """This method is called when this checkbox is checked or unchecked"""
        self.password_visible = self.check_box_1.checked
        if self.password_visible:
            self.text_box_2.hide_text = False  # Show decrypted password
        else:
            self.text_box_2.hide_text = True





