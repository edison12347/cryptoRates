import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cryptoRates.settings")
# os.environ['DJANGO_SETTINGS_MODULE'] = 'cryptoRates.settings'

import django
django.setup()

# FAKE POP Script
import randoms
from test_app.models import AcessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'News']

def add_topic():
    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    topic.save()
    return topic

def populate(N=5):

    for entry in range(N):

        # get topic for entry
        top = add_topic()

        # create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for the webpage
        acc_rec = AcessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating sctript start')
    populate(10)
    print('populating complete')
