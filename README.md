# salesforce-bulkv2
salesforce Bulk Api 2.0 Utility Library

## import package 
```python
from sfbulkapiv2 import Bulk
```
## connection

Bulk Api connect using Outh2.0. So setup a connected Apps in salesforce and connect to salesforce as below.
```python
username = 'xxx@xxx.com'
password = 'xxxxxxxxxx'
client_id = 'xxxxxxxxxxxxxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxx'
BulkApi = Bulk(client_id, client_secret, username, password, False)
```

## Query
```python 
result=BulkApi.query("""select id,name from contact""")
```

## Insert

```python
content="""firstName,LastName
        john,phil"""
bulk.insert("contact", content)
```
## Upsert

```python
upsertData = """firstName,LastName,Customer_ID__c
        smith,test,X9999998
        will,test,X9999999
        """
bulk.upsert("contact", "Customer_ID__c", upsertData)
```

## Delete
 ```python
 query = """select id from contact where lastName='test'"""
 result = bulk.query(query)
 bulk.delete("contact", result)```


