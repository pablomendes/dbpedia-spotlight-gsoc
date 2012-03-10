
This is the source code for the little app we created that allows people to browse Google Summer of Code (GSoC) projects.

1. Type-ahead suggestion is done via <a href="http://lookup.dbpedia.org/">DBpedia Lookup</a>. This API takes in some phrase and searches the <a href="http://dbpedia.org">DBpedia</a> knowledge base to find possible meanings for this phrase. The client side javascript uses <a href="http://code.drewwilson.com/entry/autosuggest-jquery-plugin">AutoSuggest jQuery Plugin by Drew Wilson</a>.
2. Suggestion of related concepts is done via <a href="http://wiki.dbpedia.org/Downloads37#wikipediapagelinks">DBpedia's wikiPageLinks</a> and using DBpedia Spotlight's notion of resource relatedness.
3. Retrieval of projects is done via a <a href="http://www.w3.org/TR/rdf-sparql-query/">SPARQL query</a> over annotated projects. Projects were annotated with <a href="http://wiki.dbpedia.org/spotlight/usersmanual">DBpedia Spotlight's Web Service</a>. The resulting data was loaded to Virtuoso triple store, alongside wikiPageLinks dataset of <a href="http://dbpedia.org">DBpedia</a>.
4. Results are displayed by the <a href="http://datatables.net/">DataTables jQuery plugin</a>.

Chat with us on Freenode's #dbpedia-spotlight, or through our <a href="https://lists.sourceforge.net/lists/listinfo/dbp-spotlight-users">discussion list at SourceForge.net</a>.

Coming soon: <a href="http://www.google-melange.com/gsoc/homepage/google/gsoc2012">GSoC 2012 projects</a>!
