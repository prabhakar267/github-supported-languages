# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-19 16:32:44
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-06-19 16:41:42

# from urllib import request

# url = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'
# request.urlopen(url).read(1000)

languages_list = []

with open('languages.yml') as fp:
	print_flag = False
	for line in fp:
		# if line.strip() == line:
		line = line.strip()

		if print_flag:
			line = line[:len(line)-1]
			# print line
			languages_list.append(line)
			print_flag = False
		if line == '':
			print_flag = True


print languages_list