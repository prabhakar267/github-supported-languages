# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-19 16:32:44
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-06-19 16:56:50

import requests

url = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'

response = requests.get(url)
response_line_list = response.content.splitlines()

languages_list = []

print_flag = False
for line in response_line_list:
	line = line.strip()
	if print_flag:
		line = line[:len(line)-1]
		languages_list.append(line)
		print_flag = False
	if line == '':
		print_flag = True


print languages_list
