var app = angular.module('unicornX', []);

app.controller("UnicornCtrl", ['$scope', '$http', function($scope, $http) {
    $scope.visibility = "";

    $scope.isVisible = function(x) {
    	return $scope.visibility == x;
    };

    $scope.message = "";
    $scope.query = "";

    $scope.left  = function() {return 100 - $scope.message.length;};
    $scope.clear = function() {$scope.message = "";};
    $scope.save  = function() {alert("Note Saved");};

    $scope.get_query = function(event) {
        event.preventDefault();
    	$http.get('/api/v1/jarvis?text=' + $scope.query + '&access_token='+window.authtoken)
            .then(function (resp) {
          var d = resp.data;
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

}]);