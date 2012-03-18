from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import re
import sys
import os


dir = sys.argv[1]


support="20"
confidence="0.2"
#spotter="AtLeastOneNounSelector"
#spotter="CoOccurrenceBasedSelector"
spotter="LingPipeSpotter"

ns = "http://spotlight.dbpedia.org/gsoc/vocab#"
objectProperty = ns + "tagged"
datatypeProperty = ns + "taggedString"

urlPostPrefixSpotlight = "http://spotlight.dbpedia.org/rest/annotate"


def ntObject(s, p, o):
    return "<"+s+"> <"+p+"> <"+o+"> ."


for f in os.listdir(dir):
    c = open(dir+"/"+f).read()
    els = c.split("\n")
    url = els[0]
    html = "\n".join(els[1:])

    soup = BeautifulSoup(html)
    plain = ''.join(soup.findAll(text=True))
    norm = re.sub("\s+", " ", plain)
    finalClean = re.sub("<.*?>", "", norm)

    query = urllib.quote(finalClean.encode('utf-8'))
    args = urllib.urlencode([("disambiguator", "Document"), ("support", support), ("confidence", confidence), ("text", query), ("spotter", spotter)])
    request = urllib2.Request(urlPostPrefixSpotlight, data=args, headers={"Accept": "application/json"})
    spotlightAnswer = urllib2.urlopen(request).read()

    uris = re.findall('"@URI": "(.*?)",', spotlightAnswer)
    sfs = re.findall('"@surfaceForm": "(.*?)",', spotlightAnswer)
    positions = [int(p) for p in re.findall('"@offset": "(.*?)",', spotlightAnswer)]

    sys.stderr.write("len: " + str(len(finalClean)) + " ")
    sys.stderr.write(",".join(sfs)+"\n")
    #print spotlightAnswer

    if positions:
        print finalClean[positions[0]-20:positions[0]+20]


    for uri in uris:
        print ntObject(url, objectProperty, uri)
        pass
