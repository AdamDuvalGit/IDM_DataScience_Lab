#!/usr/bin/env python
# coding: utf-8

# In[196]:


get_ipython().system('pip install yfinance')


# In[142]:


import yfinance as yf


# In[143]:


tesla = yf.Ticker('TSLA')


# In[144]:


tesla_data = tesla.history(period = "max")


# In[145]:


tesla_data.reset_index(inplace = True)


# In[184]:


tesla_data.head()


# In[153]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[52]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# In[185]:


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text


# In[195]:


soup = BeautifulSoup(html_data, 'html5lib')
#soup = html_data.find_all('tbody')
tables = soup.find_all('tbody')
tables


# In[190]:


tesla_revenue = pd.DataFrame(columns=["Quarter", "Revenue"])


# In[189]:


for row in soup.find("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    quarter = col[0].text
    revenue = col[1].text
    tesla_revenue = tesla_revenue._append({"Quarter":quarter, "Revenue":revenue}, ignore_index=True)    


# In[128]:


tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "").str.replace(",","")


# In[183]:


tesla_revenue.tail()


# In[70]:


gme = yf.Ticker('GME')


# In[71]:


gme_data = gme.history(period = "max")


# In[72]:


gme_data.reset_index(inplace = True)


# In[163]:


gme_data.tail()


# In[78]:


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'


# In[79]:


html_data = requests.get(url).text


# In[80]:


soup = BeautifulSoup(html_data, 'html5lib')


# In[85]:


gme_revenue = pd.DataFrame(columns=["Year", "Revenue"])


# In[88]:


for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    year = col[0].text
    revenue = col[1].text
    gme_revenue = gme_revenue._append({"Year":year, "Revenue":revenue}, ignore_index=True) 


# In[126]:


gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$","").str.replace(",","")


# In[127]:


gme_revenue.head()

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
#    fig.add_trace(go.Scatter(x=pd.stock_data.Date, y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
#    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Year, 'infer_datetime_format'), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible = False)
    fig.show()
# In[164]:


from datetime import datetime


# In[179]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=False, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=revenue_data.Year, y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible = False)
    fig.show()


# In[181]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




