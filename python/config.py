# -*- coding: utf-8 -*-
import configparser
import os

c = configparser.RawConfigParser()
c.read(r"./config/%s.conf"%(os.getenv('APP_ENV', 'development')))
bitwala = dict(c.items("bitwala"))
