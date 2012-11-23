#! /usr/bin/env python
import os, sys
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
import pycurl

class Spyder(object):
    def __init__(self, url):
        super(Spyder, self).__init__()
        self.c = pycurl.Curl()
        # save info in standard Python attributes
        self.c.url = url.rstrip()
        self.c.body = StringIO()
        self.c.http_code = -1
        self.c.setopt(self.c.URL, self.c.url)
        self.c.setopt(self.c.WRITEFUNCTION, self.c.body.write)

    def post_init(self):
        pass
