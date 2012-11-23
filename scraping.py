from spyder import Spyder
import pycurl

scrapers_type = {'spyder': Spyder}
scrapers_instances = []

#get urls and types
url_file = open("urls.txt", 'r')
m = pycurl.CurlMulti()
m.handles = []

for line in url_file:
    l = line.rstrip('\n').split(',')
    instance = scrapers_type[l[1]](l[0])
    instance.post_init()
    m.handles.append(instance.c)
    m.add_handle(instance.c)
    scrapers_instances.append(instance)

url_file.close()

# get data
num_handles = len(m.handles)
while num_handles:
    while 1:
        ret, num_handles = m.perform()
        if ret != pycurl.E_CALL_MULTI_PERFORM:
            break
    m.select(1.0)

# close handles
for c in m.handles:
    c.http_code = c.getinfo(c.HTTP_CODE)
    m.remove_handle(c)
    c.close()
m.close()

# get result
"""
for c in m.handles:
    data = c.body.getvalue()
    print "**********", c.url, "**********"
    print data
    print "%-53s http_code %3d, %6d bytes" % (c.url, c.http_code, len(data))
"""

for instance in scrapers_instances:
    #print instance.c.body.getvalue()
    instance.parser_events()
