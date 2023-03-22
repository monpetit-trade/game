import os
from notion_client import Client

notion = Client(auth="secret_Uo8BKCDMS2pVme83suCpH2IAyPQIjC2iQAMj3wFHNzP")

list_users_response = notion.users.list()
print(list_users_response)

list_pages = notion.pages.retrieve(page_id='Getting-Started-873a836d8c974cc682d71d6439a5c2dd')