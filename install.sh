#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

mkdir -p /usr/share/sni-qt/icons
cp ./$1/* /usr/share/sni-qt/icons/
