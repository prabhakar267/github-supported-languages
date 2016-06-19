# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-19 16:32:44
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-06-19 17:08:50

import requests
import sys

GITHUB_LINGUIST_URL = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'

def main():
    response = requests.get(GITHUB_LINGUIST_URL)
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
    
    if(len(sys.argv) > 1):
        print languages_list
    else:
        for i in languages_list:
            print i


if __name__ == "__main__":
    main()
