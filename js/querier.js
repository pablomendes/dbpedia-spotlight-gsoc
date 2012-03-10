/**
 * Prototype for the Lodgets vision
 * TODO enable qNames besides full URIs
 * TODO treat @property and @rel cases for both text and images
 * TODO deal with multiple values. possibly allow user to specify if takes the first or all, or something else.
 * @author pablomendes
 */
(function( $ ){

  $.fn.querier = function( options ) {  

    var settings = {      
      'endpoint' : 'http://dbpedia.org/sparql',
      'default-graph-uri' : 'http://dbpedia.org',
    };

    // json is returned from the Ajax call
    function update(json) {
    
        // extract a map of (property => object) for all triples where subject==uri
//        var props = new Array();
//        $.each(json.results.bindings, function(element, index) {
//	    element = this;
//            if (element["s"]["value"]==uri) { 
//                var p = element["p"]["value"]; 
//                var o = element["o"]["value"]; 
//	        props[p]=o;
//            }
//        });

	//$.each(json.head.vars, function (v, index) {
	//	console.log(v);
	//});

       //console.log(props);

       // insert a table
       $(this).html(json);


    }

    // TODO ideally, the description of a URI should be obtained by querying that URI directly (dereference)
    //      however, it seems that dbpedia.org still does not support CORS. Meanwhile we use SPARQL DESCRIBE.
    function getUrl(sparql) {
        var query = settings.endpoint +
                        "?default-graph-uri="+encodeURIComponent(settings["default-graph-uri"]) +
                        "&query="+escape(sparql) +
                        "&format=json";
	//console.log(query);
        return query;
    }

    // iterates over all elements selected by the user. e.g. $('div').describe() will go over all divs in the doc
    return this.each(function() {        
        
        var url = getUrl(sparql);

        $.ajax(url, { 
                  'headers': {'Accept': 'application/sparql-results+json'},
                  'context': this,
      	          'success': update
      	        });
  	
    });

  };
})( jQuery );
