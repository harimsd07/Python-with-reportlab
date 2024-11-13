import MetaTrader5 as mt  # pip install MetaTrader5
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly
from datetime import datetime
# start the platform with initialize()
mt.initialize()
# login to Trade Account with login()
# make sure that trade server is enabled in MT5 client terminal

login = 69296677
password = 'Guna@2626'
server = 'Exness-Trial8'

log = mt.login(login, password, server)
print(log)
# get account info
account_info = mt.account_info()
print(account_info)

# getting specific account data
login_number = account_info.login
balance = account_info.balance
equity = account_info.equity

print()
print('login: ', login_number)
print('balance: ', balance)
print('equity: ', equity)
