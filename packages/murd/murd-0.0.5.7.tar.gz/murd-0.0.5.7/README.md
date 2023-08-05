# Murd
Python Management of Matrix-like Key-Value store memories across disparate backends. Murd is the lowest level, pure python implementation backed by JSON. See [murdaws](gitlab.com/musingsole/murdaws) for AWS implementations.

## Data Model

It is best to think of a Murd as a simple key-value store, but with a mysterious dark past utterly at odds with its outwardly waify-bookishness. Much like a goodly priest knowing too much about guns and the criminal underworld, Murds allow a few tricks for segmenting data and searching within those segments. Dirty tricks no JSON object was meant know.

**Murd can be a footgun.** But used with a bit of cleverness for its keys and how to search them, Murds allow a network of distributed data stores backed by a variety of technologies including JSON, SQLite^, DynamoDB, and S3^.

^ Not yet implemented 

## Instantiate

my_murd = Murd()

### Open from file

my_murd = Murd("/home/me/my_murd.json")

## Update

murd.update([{"GROUP": "TEST": "SORT": "0": "DATA": 42}])

## Read

murd.read(group='TEST')

## Delete

murd.update([{"GROUP": "TEST": "SORT": "0": "DATA": 42}])

## Save to file

my_murd.write_murd("/home/me/my_murd.json")
