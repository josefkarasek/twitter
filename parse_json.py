#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json



data = []
with open('one.txt') as f:
    for line in f:
        data.append(json.loads(line))
print data[0]
