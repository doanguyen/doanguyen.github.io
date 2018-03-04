---
layout:     post
title:      Vnexpress like booster
date:       2015-08-11 3:53:19
summary:    Tự động like comment trên vnexpress.net
permalink:	vnexpress-like-booster
tags: index
---
Using this minor python script to automatically like a comment in vnexpress.net.

You must modify two varialbes _commentid_ and _articleid_ to match with your comment.

{% highlight python lineanchors %}
import cookielib, urllib, urllib2, random
commentid = 
ariticleid = 
for x in xrange(1,200):
	cookies = cookielib.CookieJar()
	ccid = ''.join(random.choice('0123456789abcdef') for i in range(16))
	opener = urllib2.build_opener(urllib2.HTTPRedirectHandler(),urllib2.HTTPHandler(debuglevel=0),urllib2.HTTPSHandler(debuglevel=0))
	link = "http://usi.saas.vnexpress.net/index/liketoggle?callback=jQuery17108126057917810726_1439286733587&commentid=%s&status=1&article_id=%s&objecttype=1&cookie_aid=%s&_=1439286756703" %(commentid,ariticleid,ccid)
	response = opener.open(link)
	cookies = "none"
	pass
print "Finished!"

{% endhighlight %}

Use it your way, don't abuse it!

Update 24/11/2015: With demo is better.

<iframe width="560" height="315" src="https://www.youtube.com/embed/S2PE2uRuFjg" frameborder="0" allowfullscreen></iframe>
