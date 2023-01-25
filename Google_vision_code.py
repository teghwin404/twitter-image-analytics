#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/python3.9
#pip3.9 install --user google-cloud
#pip3.9 install --user google-cloud-vision
#pip install xlrd==1.2.0
import xlrd
from google.cloud import vision
import os
import pandas as pd

Application_Credentials = 'desautels-2022-148645c7fe9c.json'
# If you encounter: module 'google.auth.transport' has no attribute 'requests'
# You just need to close the script and re-run it
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Application_Credentials
client = vision.ImageAnnotatorClient()
image = vision.Image()

# Make sure the format of image_url is xls file
loc = ("Twitter_image_data.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
df = pd.DataFrame()
# loop through every url, retrieve the image and send to google vision
for i in range(sheet.nrows):
    image_src_temp = sheet.cell_value(i, 0)
    image.source.image_uri = image_src_temp
    response = client.label_detection(image=image)
    labels = response.label_annotations
    l = []
    for label in labels:
        l.append(label.description)
    s = ' '.join(l)
    print("s")
    print(s)
    df = df.append({'URL': image_src_temp, 'Labels': s}, ignore_index=True)
df.to_excel("GV_Output.xlsx",index=False)

