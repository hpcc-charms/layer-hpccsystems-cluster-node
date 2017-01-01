# Overview 

# Usage  

## General Usge  

# Build 

## Get Source from github 

## Setup buid environemnt 

## Build Charm 
1. cd to layer-hpccsystems-cluster-node directory and run charm build

# Implementation 

This charm inherit layer-hpccystems-cluster-base charm. This is desgined to use as a cluster node of HPCCSystems Platform with most supported HPCCSystems plugins and modules. The cluster is configured through cluster manager

- plugin : an interface provided by interface-hpccsystems-plugin
- modules: an interface provided by interface-hpccsystems-moduel
- cluster: an interface provided by intererface-hpccsystems-cluster
- http   : an interface provided by intererface-http

![alt Hierarchy Diagram] (images/layer-hpccsystems-cluster-node.jpg)



