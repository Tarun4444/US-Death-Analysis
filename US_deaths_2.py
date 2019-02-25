
# coding: utf-8

# In[2]:


import csv


# In[9]:


f=open('guns.csv','r')
data=list(csv.reader(f))


# In[13]:


headers=data[1:]
years=[year[1] for year in headers]


# In[16]:


year_counts={}
for year in years:
    if year in year_counts:
        year_counts[year]+=1
    else:
        year_counts[year]=1


# In[17]:


year_counts


# In[24]:


import datetime
dates=[datetime.datetime(year=int(x[1]),month=int(x[2]),day=1) for x in headers]


# In[36]:


date_counts={}
for date in dates:
    if date in date_counts:
        date_counts[date]+=1
    else:
        date_counts[date]=1



# In[43]:


sex=[x[5] for x in headers]


# In[49]:


races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
race_counts


# In[45]:


import csv


# In[47]:


f=open('census.csv','r')
census=list(csv.reader(f))
census


# In[50]:


race_counts


# In[51]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}


# In[52]:


race_per_hundredk={}
for key,value in mapping.items():
    a=(race_counts[key]/mapping[key])*100000
    race_per_hundredk[key]=a
race_per_hundredk


# In[ ]:


intents = [row[3] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk

