var app = angular.module('unicornX', []);

app.controller("UnicornCtrl", ['$scope', '$http', function($scope) {

    $scope.cat = {
        'hotel': false
    };

    $scope.message = "";
    $scope.query = "";

    $scope.left  = function() {return 100 - $scope.message.length;};
    $scope.clear = function() {$scope.message = "";};
    $scope.save  = function() {alert("Note Saved");};

    $scope.get_query = function() {
    	$.get('/api/v1/jarvis?text=' + $scope.query + '&access_token='+window.authtoken, function (d) {
	      //$('#herestuff').html(d);
	      console.log(d);
	      if(d["type"] == "travel") {

	      } else if(d["type"] == "birthdays") {

	      } else if(d["type"] == "") {
	      	
	      }
	    });
    };

    $scope.quornuj = function () {
        console.log('Changed query to ' + $scope.query);

        if ($scope.query.indexOf('travel') > -1) {
            $scope.cat['hotel'] = true;
        }

        console.log('cat is ', $scope.cat);
    };

    console.log('Controller ready');

    var bc = this;
    bc.isLoaded = false;
    bc.likes = [];
    bc.name = '';
    bc.products = {};

    bc.stuff = function () {
        $http({
            method: 'GET',
            url: '/api/v1/jarvis?text=What+should+I+get+Konrad+for+his+birthday'
        }).then(function (response) {
            bc.likes = Object.keys(response.data.products);
            bc.name = response.data.name;
            bc.products = _.flatten(_.values(response.data.products));
            console.log(response);
            bc.isLoaded = true;
        });
    }
}]);