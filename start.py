#!/usr/bin/python
# -*- coding: utf-8 -*-
#Programmed by Kaan AKŞİT
try:
  import sys
  from lib import main
except ImportError, err:
	print "couldn't load module. %s" % (err)
	sys.exit()

try:
  main.main()
except KeyboardInterrupt:
  sys.exit()
