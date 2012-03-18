from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import re
import sys
import os


dir = sys.argv[1]


support="20"
confidence="0.2"
spotter="AtLeastOneNounSelector"
#spotter="CoOccurrenceBasedSelector"
#spotter="LingPipeSpotter"

ns = "http://spotlight.dbpedia.org/gsoc/vocab#"
objectProperty = ns + "tagged"
datatypeProperty = ns + "taggedString"

urlPostPrefixSpotlight = "http://spotlight.dbpedia.org/rest/annotate"


def ntObject(s, p, o):
    return "<"+s+"> <"+p+"> <"+o+"> ."


for f in os.listdir(dir):
    url = f
    c = open(dir+"/"+f).read()
    els = c.split("\n")
    url = els[0]
    plain = "\n".join(els[1:])

    norm = re.sub("\s+", " ", plain)
    finalClean = re.sub("<.*?>", "", norm)

    query = finalClean #urllib.quote(finalClean.encode('utf-8'))
    args = urllib.urlencode([("disambiguator", "Document"), ("support", support), ("confidence", confidence), ("text", query), ("spotter", spotter)])
    request = urllib2.Request(urlPostPrefixSpotlight, data=args, headers={"Accept": "application/json"})
    try:
        spotlightAnswer = urllib2.urlopen(request).read()

        uris = re.findall('"@URI": "(.*?)",', spotlightAnswer)
        sfs = re.findall('"@surfaceForm": "(.*?)",', spotlightAnswer)
        positions = [int(p) for p in re.findall('"@offset": "(.*?)",', spotlightAnswer)]
    except urllib2.HTTPError:
        sys.stderr.write("404!!!!!!!!!!!!!!!!!!\n")
    except urllib2.URLError:
        sys.stderr.write("Timeout!!!!!!!!!!!!!!\n")
       
    sys.stderr.write("len: " + str(len(finalClean)) + " ")
    sys.stderr.write(",".join(sfs)+"\n")
    #print spotlightAnswer

    if positions:
        print finalClean[positions[0]-20:positions[0]+20]


    for uri in uris:
        print ntObject(url, objectProperty, uri)
        pass
