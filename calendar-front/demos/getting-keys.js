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
setTimeout(function() {
	var hello = $('span.evt-lk').not('.chip-caption'); 
	var hi = Array(); 
	var ids = Array();
	for (var i = 0; i < hello.length; i++) { 
		hi.push({ "title": $(hello.get(i)).text(), "id": getId($(hello.get(i)))}); 
	}
	requestBody = JSON.stringify(hi);

	//$.get("https://localhost/?query="+requestBody);

	for(var i = 0; i < hi.length; i++) {
		$($($('div.ca-evp'+hi[i]['id']).children().get(0)).children().get(0)).append("<div>xxx</div>");
	}
},200);