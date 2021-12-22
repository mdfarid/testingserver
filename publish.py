import tableauserverclient as TSC
import argparse
import getpass
import logging
from tableauserverclient.models import tableau_auth
#9rJfznZdQcu5iu986bSM8Q==:HBSLruhhtGIsplOOK16qqg8LNAZr4DXx

from conf import

##Global Variables 
project_id = {};





def _tokenAuth():
      # import tableauserverclient as TSC
      tableau_auth = TSC.PersonalAccessTokenAuth('dev','9rJfznZdQcu5iu986bSM8Q==:HBSLruhhtGIsplOOK16qqg8LNAZr4DXx','pitiftpreport')
      server = TSC.Server('https://dub01.online.tableau.com', use_server_version=True)
      server.auth.sign_in(tableau_auth)      
      print("Sign In Success")

      ## Publish workbook in citiFTP Report Project
      ## Extract Json file & path 

      with server.auth.sign_in(tableau_auth):
            ## Get workbook items
            # all_workbooks_items, pagination_item = server.workbooks.get()
            # print([workbook.name for workbook in all_workbooks_items])

            #Store Project Items as Dict
            all_project_items, pagination_item = server.projects.get()
            for proj in all_project_items:
                  project_id.update({proj.name:proj.id})

            ## Get Projecct id
            target_project = project_id.get("CitiFTP Reports")
            print(target_project)

      # Sign out
      server.auth.sign_out()
      print("Sign Out Success")

# _tokenAuth()