#!/usr/bin/env python

import pandas as pd
import re
from pytrends.request import TrendReq
from datetime import datetime


pytrend = TrendReq()
trendingtoday = pytrend.today_searches(pn='US')
now = datetime.now()
filename = 'trending_' + now.strftime("%Y-%m-%dT%H_%M_%S") + '.txt'
with open(filename, 'w') as file:
		for item in trendingtoday:
			term = re.split(r'=|\&', item)[1]
			trending_term = term.replace('+',' ')
			file.write(f'{trending_term}\n')
