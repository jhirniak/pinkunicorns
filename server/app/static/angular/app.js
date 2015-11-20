var app = angular.module('unicornX', []);

app.controller("UnicornCtrl", ['$scope', '$http', '$sce', function($scope,$http,$sce) {
    $scope.visibility = "";

    $scope.isVisible = function(x) {
    	return $scope.visibility == x;
    }

    //$sce.trustAsResourceUrl("https://maps.googleapis.com/maps/api/directions/json");

    
    $scope.message = "";
    $scope.query = "";

    $scope.left  = function() {return 100 - $scope.message.length;};
    $scope.clear = function() {$scope.message = "";};
    $scope.save  = function() {alert("Note Saved");};

    $scope.get_query = function(event) {
        event.preventDefault();
    	$.get('/api/v1/jarvis?text=' + $scope.query + '&access_token='+window.authtoken, function (d) {
	      console.log(d);
	      alert(d["type"]);
	      if(d["type"] == "travel") {
	      	$scope.accomodation = d["accomodation"];
	      	$scope.travel = d["travel"];
	      	$scope.visibility = "travel";
	      	$scope.getRU = $sce.trustAsResourceUrl('https://maps.googleapis.com/maps/api/directions/json?origin='+$scope.travel['places'][0]['pos']+'&destination='+$scope.travel['places'][1]['pos']+'&key=AIzaSyAeLkV7n7z_Kt44uryKbPWuJ7ISHweKBqM');
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

        if ($scope.query.indexOf('travel') > -1) {
            switchToHotel();
        }

        console.log('cat is ', $scope.cat);
    };

    function switchToHotel() {
        $scope.cat['hotel'] = true;
        $.toaster({ priority : 'success', title : 'Title', message : 'Your message here'});
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