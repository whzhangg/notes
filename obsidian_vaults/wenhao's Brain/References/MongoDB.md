# MongoDB
Created: October 2, 2021 11:24 AM

### General links
https://docs.mongodb.com/manual/introduction/
https://docs.mongoengine.org/guide/defining-documents.html

### Setting up connection
##### check the listening port on the mongo service
mongo configuration file is located at: [ref](https://docs.mongodb.com/manual/reference/configuration-options/)
- /etc/mongod.conf for Linux
- /install/bin/mongod.cfg for windows

Usually, the listening port is 27017, so to connect to a mongo server, we use:

```bash
mongo "mongodb://144.213.165.19:27017"  # ( server ip address )
```

##### Set firewall rule (on windows)
Open "windows defender firewall", in *New Rule* selet allow connection for mongod.exe

##### check connection
The following command will check connection to the remote service:

```bash
nc -zv 144.213.165.19 27017
>>> Connection to 144.213.165.19 27017 port [tcp/*] succeeded!
```

Then, we should be able to connect if the server is running, with the above connection command and
```bash
show dbs
```

##### Connecting Mongo by pymongo
[Reference](https://pymongo.readthedocs.io/en/stable/tutorial.html) ]

```python
client = MongoClient('host_ip', 'port')
# or 
client = MongoClient('mongodb://host_ip:port')
```

##### References:
Connecting to a remote mongo server: https://docs.mongodb.com/mongodb-shell/connect/

How to configure remote access for mongodb on Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-configure-remote-access-for-mongodb-on-ubuntu-20-04

Connecting to MongoDB from WSL2: https://blog.nakuraicodes.com/2020/11/wsl2-and-mongodb.html

### Useful Pymongo methods
##### Find object by `_id` field
object id is an bson object :` bson.objectid.ObjectId()`, therefore, we use:
```python
from bson.objectid import ObjectId
oid = ObjectId("613abb85a8d6e47ac4967297")
collection.find( { "_id" : oid } )
```

Reference: 
https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html)
https://stackoverflow.com/questions/8233014/how-do-i-search-for-an-object-by-its-objectid-in-the-mongo-console

##### List database
```python
collection.list_collection_names()
```

##### Drop collections in database
```python
db.collecton.drop()
```
https://docs.mongodb.com/manual/reference/method/db.collection.drop/

##### MongoDB query operator and search
Reference: https://docs.mongodb.com/manual/reference/operator/query/

| operator | example |
| -- | -- |
|$eq  |`{ <field>: { $eq: <value> } }` |
|$gt  |`{ <field>: { $gt: <value> } }` |
|$gte | |
|$in  | |
|$lt  | |
|$lte | |
|$ne  | |
|$nin | |
|$and |`{ $and: [ { <expression1> }, ... , { <expressionN> } ] }` |
|$not |`{ field: { $not: { <operator-expression> } } }` |
|$nor | |
|$or  | |

A combined search can be issued by:
```python
db.inventory.find(
	{ $and: [
		{ $or: [ { qty: { $lt : 10 } }, { qty : { $gt: 50 } } ] },
		{ $or: [ { sale: true }, { price : { $lt : 5 } } ] }
	] }
)
```

##### MongoDB regular expression
Mongo DB used Perl language for regular expression. [Ref]https://docs.mongodb.com/manual/reference/operator/query/regex/

For Perl Regular expression see: https://perldoc.perl.org/perlre