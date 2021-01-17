import webbrowser

print("hello world")
solution = 2**38
target_url = 'http://www.pythonchallenge.com/pc/def/%s.html' % solution
print("The value of 2**38 is: " + str(solution))
print("The target URL is therefore: %s" % target_url)

# If new is 0, the url is opened in the same browser window if possible.
# If new is 1, a new browser window is opened if possible.
# If new is 2, a new browser page ("tab") is opened if possible.

# finish by opening up webpage of next step of challenge
webbrowser.open(target_url, new=2)
