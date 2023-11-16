import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Molecular_similarities.settings')

import django

django.setup()
import json
import random 
from Similarity_search.models import Compound
#from faker import Faker
'''
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #create teh fake data for teh entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create teh new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url = fake_url, name = fake_name)[0]

        #create a fake access record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")
'''
with open('c:\\Users\\Maxym\\Desktop\\ecmdb_sdf\\cleaned_ecmdb.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
def populating():
    for item in data:
        entries = Compound.objects.get_or_create(Name = item["name"], 
                                                 Description = item["description"],
                                                 SMILES = item["smiles"],
                                                 IUPAC = item["moldb_iupac"])[0]
if __name__ == '__main__':
    print("populating script")
    populating()
    print("populating complete")       
