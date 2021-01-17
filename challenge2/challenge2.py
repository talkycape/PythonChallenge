import webbrowser
import urllib.request
import re

# use urllib library to grab source code
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
#print(html)

# pull out comments using regular expressions
#
# FAQ #1: Why '.*?' in the regular expression?
# ============================================
#
# From: https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
#
# Consider the input 101000000000100.
# Using 1.*1, * is greedy - it will match all the way to the end, and then backtrack until it can match 1, leaving you with 1010000000001.
# .*? is non-greedy. * will match nothing, but then will try to match extra characters until it matches 1, eventually matching 101.
#
# FAQ #2: What is re.DOTALL
# =========================
#
# From: https://docs.python.org/3/library/re.html
#
# (Dot.) In the default mode, this matches any character except a
# newline. If the DOTALL flag has been specified, this matches any
# character including a newline.
#

# pull out relevant comments sections
all_comments = re.findall("<!--(.*?)-->", html, re.DOTALL)

# but we only care about last comment section
comments = all_comments[-1]
#print(comments)

# let get the histogram of all characters
# get(c, 0) returns 0 if doesn't exist (instead of None) so we can do math on it
count = {}
for c in comments:
    count[c] = count.get(c, 0) + 1

# rare means single count, so let's just keep those
rare_keys = []
for k,v in count.items():
    if v==1:
        rare_keys.append(k) 
# print(rare_keys)

# use a join to make a string from the list
solution = ''.join(rare_keys)

# use the solution as the target url
target_url = 'http://www.pythonchallenge.com/pc/def/%s.html' % solution

# now print the solution and go to the next web page...
print("Solution is the following:")
print(target_url)
webbrowser.open(target_url, new=2)

