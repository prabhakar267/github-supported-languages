# -*- coding: utf-8 -*-
# @Author: prabhakar, QzSG
# @Date:   2016-06-19 16:32:44
# @Last Modified by:   Prabhakar Gupta, QzSG
# @Last Modified time: 2016-06-19 17:17:09

import requests
import sys

GITHUB_LINGUIST_URL = 'https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml'

def main():
    try:
        response = requests.get(GITHUB_LINGUIST_URL)
        response_line_list = response.content.split("---")[-1].splitlines()

        languages_list = []

        for line in response_line_list:
            if line[:2] != '  ':
                if line.strip() != '':
                    line = line[:len(line)-1]
                    languages_list.append(line)
                
        if(len(sys.argv) > 1):
            for i in languages_list:
                print i
        else:
            print languages_list
    
    except requests.exceptions.ConnectionError:
        print "There is a problem with your internet connectivity or DNS resolution."
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print "It took too long for the server to respond, please try again!"
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print "There was a critical error"
        print e


if __name__ == "__main__":
    main()
