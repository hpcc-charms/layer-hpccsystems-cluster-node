#!/usr/bin/env python3
#import os
#import platform
#import yaml
#from subprocess import check_call

from charms.reactive import scopes
from charms.reactive.helpers import is_state

from charms.reactive.bus import (
    set_state,
    get_state,
    remove_state
)

from charms.reactive.decorators import (
    hook,
    when,
    when_not
)

from charmhelpers.core.hookenv import (
   log,
   CRITICAL,
   ERROR,
   WARNING,
   INFO,
   DEBUG,
   status_set,
   remote_unit
)

from charms.layer.jujuenv import JujuEnv

@when('hpcc-cluster.envxml.available')
def fetch_envxml(configure):
   log("# of conversation in this action: " + str(len(configure.conversations())), INFO)
   conv = configure.conversation(remote_unit())

   # if current node is dali skip

   log('stop hpcc first', INFO)
   log('get environment.xml from cluster manager', INFO)
   
   configure.result = 'envxml.available:OK' 
   conv.set_remote('result', configure.result)  
   status_set('active', JujuEnv.STATUS_MSG['CLUSTER_CONFIGURED'])
   configure.remove_state('hpcc-cluster.envxml.available')

@when('hpcc-cluster.envxml.available.dali')
def fetch_envxml_dali(configure):
   conv = configure.conversation(remote_unit())

   # if current node is not dali skip

   log('stop dali hpcc first', INFO)
   log('get environment.xml from cluster manager', INFO)
   
   configure.result = 'envxml.available.dali:OK' 
   conv.set_remote('result', configure.result)  
   status_set('active', JujuEnv.STATUS_MSG['NODE_CONFIGURED'])
   configure.remove_state('hpcc-cluster.envxml.available.dali')

@when('hpcc-cluster.dali.start')
def start_dali(configure):
   conv = configure.conversation(remote_unit())

   # if current node is not dali skip

   status_set('active', JujuEnv.STATUS_MSG['DALI_START'])
   log('start dali', INFO)
   
   configure.result = 'dali.start:OK' 
   conv.set_remote('result', configure.result)  
   configure.remove_state('hpcc-cluster.dali.start')

@when('hpcc-cluster.cluster.start')
def start_cluster(configure):
   conv = configure.conversation(remote_unit())

   # if current node is dali skip

   status_set('active', JujuEnv.STATUS_MSG['STARTING'])
   log('start cluster', INFO)
   
   configure.result = 'cluster.start:OK' 
   conv.set_remote('result', configure.result)  
   status_set('active', JujuEnv.STATUS_MSG['NODE_STARTED'])
   configure.remove_state('hpcc-cluster.cluster.start')
