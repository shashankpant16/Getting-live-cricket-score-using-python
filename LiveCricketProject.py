#!/usr/bin/env python
# coding: utf-8

# In[88]:


import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# In[89]:


url ="http://www.espncricinfo.com/scores"
res = requests.get(url)


# In[90]:


soup = BeautifulSoup(res.content,'html.parser')


# In[91]:


lst = []
for i in soup.find('div',{'class':'scoreCollection__content cricket'}).find_all('a'):
    #print(i.get('href'))
    if  'http' in str(i.get('href')):
        lst.append(str(i.get('href')))


# In[93]:


len(lst)


# In[92]:


for i in lst:
    res = requests.get(i)
    soup = BeautifulSoup(res.content,'html.parser')
    cont = []
    try:
        for i in soup.find('div',{'class':'content'}).strings:
            cont.append(str(i))
        player = []
        player.append(cont[21])
        player.append(cont[35])
        score = []
        score.append(int(cont[23]))
        score.append(int(cont[37]))
            #print(player[0],player[1])
        plt.bar(player,score)
        plt.show()
    except:
        pass
        


# In[ ]:





# In[ ]:





# In[ ]:




