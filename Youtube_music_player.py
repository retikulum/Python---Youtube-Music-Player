#!/usr/bin/env python
import webbrowser
import urllib2
print "-------------\n YOUTUBE MUSIC OPENER\n-------------"
user_want=raw_input("What do you want me to play.\n")
user_want=list(user_want)
#Have to remove spaces because it gives error when program wants to view source code.
for char in user_want:
    if char==" ":
        user_want.remove(char)
user_want="".join(map(str,user_want))
youtube_link="https://www.youtube.com/results?search_query="
search_link=youtube_link+user_want
#view source code
request=urllib2.Request(search_link)
response=urllib2.urlopen(request)
ans=response.readlines()
#find wacth?v= in source code then program open first video in search page
for item in ans:
        if "watch?v=" in item:
            a= item[item.index("watch?v="):]
            break
youtube="https://www.youtube.com/"+a[0:19]
webbrowser.open_new_tab(youtube)
