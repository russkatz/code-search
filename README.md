### Demo showing DSE Search with workload isolation.

Steps:
* Install/Config a DSE 6.0+ cluster with two DCs: DC1 and search (https://docs.datastax.com/en/install/doc/install/installTOC.html)
* Enable DSE search on only the search DC
* Clone this repo onto a node: git clone https://github.com/russkatz/code-search/edit/master/README.md
* Load schema: cqlsh -f schema.cql (Note that this also enables DSE Search indexing on the table)
* Install DSE Python drivers: pip install dse-driver
* Generate data: ./producer.py (You can let this run, or hit ctrl+c to stop)
* Login to node in search DC and run cqlsh
* Try some searches! (Your data will be different, so edit as needed)
** `select * from cme.quotes where solr_query = '{"q":"code:mow", "fq":"quotetime:[* TO 2018-05-23T23:03:16.000Z]", "sort":"quotetime desc" }' LIMIT 1 ;` 

