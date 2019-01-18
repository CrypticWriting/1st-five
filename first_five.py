#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:38:09 2019

@author: matiaspehkonen
"""

from googlesearch import search
import webbrowser


# List for search results
search_result = []

# Lets start by asking the search keyword
print("Enter your Google search")
google_search = input()


# Gets the first hits for search input() and appends them to search_result
for url in search(google_search, stop=5):
    search_result.append(url)


# Opening five of the search on chrome
# Seems like sometimes chrome needs to be open already...
    
for i in range(0, 5):
    webbrowser.get("chrome").open_new(search_result[i]) 


print("You have compleated your search: " + google_search)
print(search_result)





    