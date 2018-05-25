#!/usr/bin/python

from dse.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from dse.policies import DCAwareRoundRobinPolicy,TokenAwarePolicy, ConstantSpeculativeExecutionPolicy
from dse import ConsistencyLevel

import sys
from random import randint
import calendar
import time,datetime
import string
import random
import decimal

#Configuration
contactpoints = ['172.31.2.8', '172.31.7.93']
localDC = "DC1"
keyspace = "codes"
CL = ConsistencyLevel.ONE
profile1 = ExecutionProfile( load_balancing_policy=DCAwareRoundRobinPolicy(local_dc=localDC, used_hosts_per_remote_dc=3),
                            speculative_execution_policy=ConstantSpeculativeExecutionPolicy(.1, 20),
                            consistency_level = CL
                            )

print "Connecting to cluster"

cluster = Cluster( contact_points=contactpoints,
                   execution_profiles={EXEC_PROFILE_DEFAULT: profile1},
                   )

session = cluster.connect(keyspace)

c = 0
x = 0
while 1:
   quotetime = int(time.time())
   code = random.choice(string.letters).lower() + random.choice(string.letters).lower() + random.choice(string.letters).lower()
   quoteprice = decimal.Decimal(random.randrange(10000))/100
   #print quotetime, code, quoteprice

   #session.execute (""" INSERT INTO codes.quotes (code, quotetime, quoteprice) VALUES (%s, %s, %s) """, (str(code), datetime.datetime.now().replace(microsecond=0).isoformat(), str(quoteprice)))
   session.execute_async (""" INSERT INTO codes.quotes (code, quotetime, quoteprice) VALUES (%s, %s, %s) """, (str(code), datetime.datetime.now().replace(microsecond=0).isoformat(), str(quoteprice)))
   c = c + 1
   x = x + 1
   if(x == 1000):
      print(c)
      x = 0

cluster.shutdown()
sys.exit(0)
