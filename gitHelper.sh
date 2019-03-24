#!/bin/sh
#sh gitHelper "[insert message here]"
git pull
git add .
git commit -am $1
echo $1
git push -u origin master