# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:46:02 2020

@author: Phuong Anh Vu
"""

import pandas as pd
import glassdoorscrapping as gs

df = gs.get_jobs("data analyst", 500, False,10)

df.to_csv("data.csv", index=False)