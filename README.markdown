This is the source code for the little app we created that allows people to browse Google Summer of Code (GSoC) projects.

<p>If you are curious about how we implemented this app, feel free to check our <a href="https://github.com/pablomendes/dbpedia-spotlight-gsoc">source code</a>.
    <ol>
<li>Type-ahead suggestion is done via <a href="http://enable-cors.org">CORS-enabled</a> Ajax queries to <a href="http://lookup.dbpedia.org/">DBpedia Lookup</a>. This API takes in some phrase and searches the <a href="http://dbpedia.org">DBpedia</a> knowledge base to find possible meanings for this phrase. Once you pick one of those meanings, we store its unique identifier (URI) from DBpedia. The client side javascript uses <a href="http://code.drewwilson.com/entry/autosuggest-jquery-plugin">AutoSuggest jQuery Plugin by Drew Wilson</a>.<li>Suggestion of related concepts is done via <a href="http://wiki.dbpedia.org/Downloads37#wikipediapagelinks">DBpedia's wikiPageLinks</a> and using <a href="http://wiki.dbpedia.org/spotlight/isem2011">DBpedia Spotlight's notion of resource relatedness</a>. For each of the URIs you have selected in step 1, we find all concepts linked to them via DBpedia properties. We add to that any other concepts that are "topically similar" according to DBpedia Spotlight.<li>Retrieval of projects is done via a <a href="http://www.w3.org/TR/rdf-sparql-query/">SPARQL query</a> over annotated projects stored in our <a href="http://spotlight.dbpedia.org/sparql">SPARQL endpoint</a>. Projects were annotated with <a href="http://wiki.dbpedia.org/spotlight/usersmanual">DBpedia Spotlight's Web Service</a>. The resulting data was loaded to <a href="http://virtuoso.openlinksw.com">Virtuoso triple store</a>, alongside wikiPageLinks dataset of <a href="http://dbpedia.org">DBpedia</a>.<li>Results are displayed by the <a href="http://datatables.net/">DataTables jQuery plugin</a>.
   </ol>

<p>DBpedia Spotlight <a href="http://www.google-melange.com/gsoc/org/google/gsoc2012/dbpediaspotlight">has been selected as an organization</a> for GSoC2012. If you have <a href="http://wiki.dbpedia.org/gsoc2012/ideas">project ideas</a> involving DBpedia Spotlight, please let us know. Chat with us on Freenode's #dbpedia-spotlight, or through our <a href="https://lists.sourceforge.net/lists/listinfo/dbp-spotlight-developers">discussion list at SourceForge.net</a>.</p>

## Server Side

This demo relies on three Web services.

### DBpedia Lookup

http://lookup.dbpedia.org

### DBpedia Spotlight's rel8 ###

Testing the deployed demo

     curl -H "application/json" "http://spotlight.dbpedia.org/related/?uri=Berlin"

Getting the code 

    https://github.com/dbpedia-spotlight/dbpedia-spotlight/wiki/Installation
    
Starting the server

      mvn scala:run -DmainClass="org.dbpedia.spotlight.web.rest.RelatedResources"

Using the server

      curl -H "application/json" "http://localhost:2222/related/?uri=Berlin"

### SPARQL server ###

We also use a SPARQL endpoint to query data about GSoC projects. So you first need access to a SPARQL server. We will use Apache Jena's Fuseki as an example:

http://jena.apache.org/documentation/serving_data/index.html#download-fuseki

Download data:

    wget https://raw.github.com/pablomendes/dbpedia-spotlight-gsoc/master/data/gsoc-projects-2011.nt
    wget https://raw.github.com/pablomendes/dbpedia-spotlight-gsoc/master/data/gsoc-projects-2012.nt

Start Fuseki:

    ./fuseki-server --update --mem /gsoc

Load data into the server:

    ./s-put http://localhost:3030/gsoc/data default Data/gsoc-projects-2011.nt
    ./s-put http://localhost:3030/gsoc/data default Data/gsoc-projects-2012.nt    
    
The command below uses cURL to execute a SPARQL query that retrieves all GSoC projects tagged with the string "css".

    http://localhost:3030/gsoc/query
    
You can try that also with our public endpoint.

    curl http://spotlight.dbpedia.org/sparql/ -d "query=select * where { ?s  <http://spotlight.dbpedia.org/gsoc/vocab#taggedString> \"css\"@en } limit 5"
