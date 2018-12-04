#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import netifaces as ni

for i in ni.interfaces():
    config = ni.ifaddresses(i)
    if ni.AF_INET in config:
        for link in config[ni.AF_INET]:
            if 'addr' in link and 'peer' not in link:
                print(link['addr'])
