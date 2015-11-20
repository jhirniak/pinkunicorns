function getId(element) {
	var classList = $(element).attr('class').split(/\s+/);
	for(var i = 0; i < classList.length; i++){
	    if(classList[i].lastIndexOf("ca-elp", 0) === 0) {
	    	return classList[i].split('ca-elp')[1];
	    }
	}
}

var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);
setTimeout(200, function() {
	var x = $('span.evt-lk').not('.chip-caption'); 
	var y = Array(); 
	var ids = Array();
	for (var i = 0; i < x.length; i++) { 
		y.push({ "title": $(x.get(i)).text(), "id": getId($(x.get(i)))}); 
	}
	requestBody = JSON.stringify(y);

	for(var i = 0; i < y.length; i++) {
		$('div.ca-evp'+y[i]['id']).append('<div>Hello!</div>');
	}
});
//$().get request