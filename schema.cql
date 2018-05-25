CREATE KEYSPACE codes WITH replication = {'class': 'NetworkTopologyStrategy', 'DC1': '3', 'search': '3'}  AND durable_writes = true;

CREATE TABLE codes.quotes (
    code text,
    quotetime timestamp,
    quoteprice text,
    solr_query text,
    PRIMARY KEY (code, quotetime)
