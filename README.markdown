    Hang in there. We are writing a nice explanation. Meanwhile, here is the quick and dirty rundown:
    <ol>
        <li>Type-ahead suggestion is done via <a href="http://lookup.dbpedia.org/">DBpedia Lookup</a>.</li>
        <li>Suggestion of related concepts is done via <a href="http://wiki.dbpedia.org/Downloads37#wikipediapagelinks">DBpedia's wikiPageLinks</a> and using DBpedia Spotlight's notion of resource similarity.</li>
        <li>Retrieval of projects is done via a <a href="http://www.w3.org/TR/rdf-sparql-query/">SPARQL query</a> over annotated projects.</li>
        Projects were annotated with <a href="http://wiki.dbpedia.org/spotlight/usersmanual">DBpedia Spotlight's Web Service</a>.
        The resulting data was loaded to Virtuoso triple store, alongside wikiPageLinks dataset of DBpedia.
    </ol>
    <p>Chat with us on Freenode's #dbpedia-spotlight, or through our <a href="https://lists.sourceforge.net/lists/listinfo/dbp-spotlight-users">discussion list at SourceForge.net</a></p>

<p>Coming soon: <a href="http://www.google-melange.com/gsoc/homepage/google/gsoc2012">GSoC 2012 projects</a>!</p>
