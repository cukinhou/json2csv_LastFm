
#import musicbrainzngs as m
import json
from pprint import pprint
#from sklearn.feature_selection import variance_threshold as vt
from os import listdir, path
import numpy as np
import csv
import urllib


# In[2]:

path = '/home/aspma/Downloads/lfm-genre-ds-training/'
csv_path ='/home/aspma/aspma-course/csv/'
files = listdir(path)
data = json.load(open(path+files[0],'r'))


# In[3]:

groundT = json.load(urllib.urlopen('http://www.dtic.upf.edu/~aporter/amplab/lastfm-genre-mapping-2016-03-02.json'))


# In[ ]:




# In[7]:

with open(csv_path+'last_fm_sin clat_easy.csv','wb+') as csvFile:
     
    data = json.load(open(path+files[0],'r'))
    csv_file = csv.writer(csvFile)
    namespaces = data.keys()
    header = ['ID']
    header.append('Genre')

    #Read first JASON file in order to extract Header structure
    for n in namespaces[0:3]:
        for d in data[n].keys():
            if type(data[n][d]) is dict:
                for j in data[n][d].keys():
                    if type(data[n][d][j]) is not list:
                        name = str(n + '.' + d + '.' + j)
                        header.append(name)
            else:
                name = str(n + '.' + d)
                header.append(name)

    csv_file.writerows([header])
        
    for idx in range(len(files)):
        data = json.load(open(path+files[idx],'r'))
        genre = groundT[files[idx][0:len(files[0])-5]]
        
        value = [files[idx][0:len(files[0])-5]]
        value.append(genre)
        for n in namespaces[0:3]:
            for d in data[n].keys():

                if type(data[n][d]) is dict:

                    for j in data[n][d].keys():

                        if type(data[n][d][j]) is not list:
                            value.append(data[n][d][j])


                else:
                    value.append(data[n][d])


        csv_file.writerows([value])

