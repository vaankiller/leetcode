#!/bin/sh

cat file.txt | egrep "^(\([0-9]{3}\)\s|[0-9]{3}-)[0-9]{3}-[0-9]{4}$"

# Tips : cat file.txt | egrep "(\([0-9]{3}\)\s|[0-9]{3}-)[0-9]{3}-[0-9]{4}"
# [[:anything:]] is in shell regex
