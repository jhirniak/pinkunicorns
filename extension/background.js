/************************************************************************************
  This is your background code.
  For more information please visit our wiki site:
  http://docs.crossrider.com/#!/guide/scopes_background
*************************************************************************************/

appAPI.ready(function($) {

  // Place your code here (ideal for handling browser button, global timers, etc.)
  console.log('Lol');
});

appAPI.contextMenu.add("key1", "Analyze", function (data) {
    var sAlertText = 'pageUrl: ' + data.pageUrl + '\r\n' +
                     'linkUrl: ' + data.linkUrl + '\r\n' +
                     'selectedText:' + data.selectedText + '\r\n' +
                     'srcUrl:' + data.srcUrl;
    alert(sAlertText);
    alert(JSON.stringify(data, null, 2));
    
    appAPI.request.post({
        url: 'http://localhost:5000/extension/',
        // Data to post
        postData: {id:123, name:{first:'joe', last:'bloggs'}},
        onSuccess: function(response) {
            console.log("Succeeded in posting data");
            if (appAPI.utils.isObject(response)) {
                console.log('Response properties:');
                for (var p in response) {
                    console.log(response[p] + ': ' + p);
                }
            } else
                console.log('Response: ' + response);
        },
        onFailure: function(httpCode) {
            console.log('Failed to retrieve content. (HTTP Code:' + httpCode + ')');
        },
        contentType: 'application/json',
        responseDataType: 'application/json'
    });
}, ["all"]);