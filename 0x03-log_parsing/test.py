#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 22-01-2024
"""
from re import findall


search = '24.56.77.180 - [2024-01-22 23:17:04.348694] "GET /projects/260 HTTP/1.1" 200 824'
pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(\s\d{3}\s)'
print(findall(pattern, search))
