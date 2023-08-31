#!/bin/bash
#Script to send request to given url and displa the
#+bodyy size of the response

curl -s "$1" | wc -c
