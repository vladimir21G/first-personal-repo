from woocommerce import API

wcapi = API(
    url="http://65.108.94.150/",
    consumer_key="ck_60325206de2c5925f7f3a341134c53f480343b51",
    consumer_secret="cs_21a9356a8b6784187351b369b181dcbb5bd5755f",
    version="wc/v3"
)

r = wcapi.get("products")

import pprint

pprint.pprint(r.json());