var app = angular.module('unicornX', []);

app.controller("UnicornCtrl", [
    '$scope',
    '$http',
    function($scope) {

    $scope.cat = {
        'travel': false,
        'meeting': false
    };

    $scope.visibility = "";

    $scope.isVisible = function(x) {
    	return $scope.visibility == x;
    }

    $scope.message = "";
    $scope.query = "";

    $scope.left  = function() {return 100 - $scope.message.length;};
    $scope.clear = function() {$scope.message = "";};
    $scope.save  = function() {alert("Note Saved");};

    $scope.get_query = function(event) {
        event.preventDefault();
    	$.get('/api/v1/jarvis?text=' + $scope.query + '&access_token='+window.authtoken, function (d) {
	      console.log(d);
	      if(d["type"] == "travel") {
	      	$scope.accomodation = d["accomodation"];
	      	$scope.travel = d["travel"];
	      	$scope.visibility = "travel";
	      } else if(d["type"] == "birthdays") {
	      	$scope.likes = Object.keys(d.products);
            $scope.name = d.name;
            $scope.products = _.flatten(_.values(d.products));
            $scope.visibility = "birthdays";
	      } else if(d["type"] == "") {
	      	
	      }
	    });
    };

    $scope.quornuj = function () {
        console.log('Changed query to ' + $scope.query);

        switchToHotel($scope.query.indexOf('travel') > -1);
        switchToMeeting($scope.query.indexOf('meeting') > -1);

        console.log('cat is ', $scope.cat);
    };

    function switchToHotel(mode) {
        $scope.cat['hotel'] = mode;
        if (mode) { $.toaster({ priority : 'success', title : 'Title', message : 'Your message here'}); }
    }

    function switchToMeeting(mode) {
        $scope.cat['meeting'] = mode;
        if (mode) { $.toaster({ priority : 'success', title : 'Title', message : 'Your message here'}); }
    }

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