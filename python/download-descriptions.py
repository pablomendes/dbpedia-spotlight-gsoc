
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

ns = "http://spotlight.dbpedia.org/gsoc/vocab#"
objectProperty = ns + "tagged"
datatypeProperty = ns + "taggedString"
keyProperty = ns + "key"
nameProperty = ns + "name"
linkIdProperty = ns + "linkId"

urlPrefixSpotlight = "http://spotlight.dbpedia.org/rest/annotate?disambiguator=Document&support=-1&confidence=-1&text="
urlPrexfixLookup = "http://lookup.dbpedia.org/api/search.asmx/KeywordSearch?QueryString="




def ntLiteral(s, p, o):
    return "<"+s+"> <"+p+'> "'+o+'"@en .'

def ntObject(s, p, o):
    return "<"+s+"> <"+p+"> <"+o+"> ."

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

    print ntLiteral(ideasHtml, keyProperty, key)
    print ntLiteral(ideasHtml, nameProperty, name)
    print ntLiteral(ideasHtml, linkIdProperty, linkId)

#############################################
# tags
    for tag in tags:
        print ntLiteral(ideasHtml, datatypeProperty, tag)
        pass

#############################################
# disambiguated tags
    if len(tags) == 1:
        query = urllib.quote(tags[0])
        url = urlPrexfixLookup + query
        sys.stderr.write(url+"\n")
        contents = urllib2.urlopen(url).read()
        #sys.stderr.write(contents+"\n")
        m = re.search('<ArrayOfResult.*<URI>(.*?)</URI>,', contents)
        if not m:
            uris = []
        else: 
            uris = [m.group(0)]
    else:
        query = urllib.quote("[[" + "]], [[".join(tags) + "]]")
        url = urlPrefixSpotlight + query
        #sys.stderr.write(url+"\n")
        request = urllib2.Request(url, headers={"Accept": "application/json"})
        contents = urllib2.urlopen(request).read()
        uris = re.findall('"@URI": "(.*?)",', contents)

    for uri in uris:
        print ntObject(ideasHtml, objectProperty, uri)
        pass


