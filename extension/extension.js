  /************************************************************************************
  This is your Page Code. The appAPI.ready() code block will be executed on every page load.
  For more information please visit our docs site: http://docs.crossrider.com
*************************************************************************************/

appAPI.ready(function($) {

    // Place your code here (you can also define new functions above this scope)
    // The $ object is the extension's jQuery object

    //alert("My new Crossrider extension works! The current page is: " + document.location.href);

  /** DOM */
  $("body").append("<div id='fbhack'></div>");
  $("#fbhack").css({
  	'z-index': 1000,
    'position': 'fixed',
    'width': '50px',
    'height': '50px',
    'right': '50px',
    'bottom': '50px',
    'border-radius': '100%',
    'background-color': '#0BB2FF'
  });
  
  $("#fbhack").append("<div id='fbhack-menu'></div>");
  $("#fbhack-menu").css({
  	'z-index': 1010,
  	'position': 'absolute',
  	'bottom': '50px',
  	'background-color': 'green',
  	'height': '200px',
  	'width': '50px',
  	'display': 'none'
  });
  
  /** Actions */
  
  $("#fbhack").mouseenter(function (){
    $(this).css({
      'background-color': '#1560BD'
    });
  });

  $("#fbhack").mouseleave(function (){
    $(this).css({
      'background-color': '#0BB2FF'
    });
  });
  
  $("#fbhack").hover(function(){
    $("#fbhack-menu").slideToggle();
  }, function(){
    $("#fbhack-menu").slideToggle();
  });
  
  var counter = -1;
  $("#fbhack").click(function(){
  	console.log(++counter);
  });
  
  /** Facebook inject */
	window.fbAsyncInit = function() {
	  FB.init({
	    appId      : '478020999044437',
	    cookie     : true,  // enable cookies to allow the server to access 
	                        // the session
	    xfbml      : true,  // parse social plugins on this page
	    version    : 'v2.2' // use version 2.2
	  });
	
	  // Now that we've initialized the JavaScript SDK, we call 
	  // FB.getLoginStatus().  This function gets the state of the
	  // person visiting this page and can return one of three states to
	  // the callback you provide.  They can be:
	  //
	  // 1. Logged into your app ('connected')
	  // 2. Logged into Facebook, but not your app ('not_authorized')
	  // 3. Not logged into Facebook and can't tell if they are logged into
	  //    your app or not.
	  //
	  // These three cases are handled in the callback function.
	
	  FB.getLoginStatus(function(response) {
	    statusChangeCallback(response);
	  });
	
	};

	(function(d, s, id) {
	    var js, fjs = d.getElementsByTagName(s)[0];
	    if (d.getElementById(id)) return;
	    js = d.createElement(s); js.id = id;
	    js.src = "//connect.facebook.net/en_US/sdk.js";
	    fjs.parentNode.insertBefore(js, fjs);
	  }(document, 'script', 'facebook-jssdk'));
	
	injectFacebookLoginBtn($("#fbhack-menu"));

});

function injectFacebookLoginBtn(elem) {
	elem.append("<fb:login-button scope=\"public_profile,email\" onlogin=\"checkLoginState();\"></fb:login-button>");
}

function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      testAPI();
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }
  
  // Here we run a very simple test of the Graph API after login is
	  // successful.  See statusChangeCallback() for when this call is made.
	  function testAPI() {
	    console.log('Welcome!  Fetching your information.... ');
	    FB.api('/me', function(response) {
	      console.log('Successful login for: ' + response.name);
	      document.getElementById('status').innerHTML =
	        'Thanks for logging in, ' + response.name + '!';
	    });
	}