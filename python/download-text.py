
import os
from BeautifulSoup import BeautifulSoup
import csv
import re
import urllib
import urllib2
import sys
import justext
from django.utils.encoding import smart_str, smart_unicode


csvInput = sys.argv[1]

skippedFirst = False
for els in csv.reader(open(csvInput), delimiter=",", quotechar='"'):

    if not skippedFirst:
        skippedFirst = True
        continue

    key = els[0]
    name = els[1]
    linkId = els[2]
    tags = [t.replace("_", " ").strip() for t in els[3:-1][0].split(",")]
    ideasHtml = els[-1]

    if ideasHtml.strip():
        p = "output-html/"+linkId
        #if os.path.exists(p):
        #    continue
        sys.stderr.write(ideasHtml+"\n")
        try: 
            #for html
            if os.path.exists(p):
                html = open(p,"r").read()
                sys.stderr.write("From local.")
            else:
                html = urllib2.urlopen(ideasHtml).read()
                open(p, "w").write(ideasHtml+"\n"+html)
                sys.stderr.write("From URL...")
            #for text within html tags
            paragraphs = justext.justext(html, justext.get_stoplist('English'))
            f = open("output-text/"+linkId, "w")
            f.write(ideasHtml+"\n")
            for paragraph in paragraphs:
                if paragraph['class'] == 'good':
                    try:
                        text = smart_str(paragraph['text']) # http://www.saltycrane.com/blog/2008/11/python-unicodeencodeerror-ascii-codec-cant-encode-character/
                        f.write(text+"\n")
                    except UnicodeEncodeError:
                        sys.stderr.write("UTF8 error. Ignoring\n")
            sys.stderr.write("OK!\n")
            f.close()
        except urllib2.HTTPError:
            sys.stderr.write("404!!!!!!!!!!!!!!!!!!\n")
        except urllib2.URLError:
            sys.stderr.write("Timeout!!!!!!!!!!!!!!\n")
