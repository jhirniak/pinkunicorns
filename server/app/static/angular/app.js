var app = angular.module('unicornX', ['ui.bootstrap']);

app.controller("UnicornCtrl", ['$scope', '$http', '$sce', function($scope,$http,$sce) {
    $scope.visibility = "";

    $scope.isVisible = function(x) {
    	return $scope.visibility == x;
    };

    $scope.loading = false;

    //$sce.trustAsResourceUrl("https://maps.googleapis.com/maps/api/directions/json");

    $scope.message = "";
    $scope.query = "";

    $scope.left  = function() { return 100 - $scope.message.length; };
    $scope.clear = function() { $scope.message = ""; };
    $scope.save  = function() { alert("Note Saved"); };

    $scope.get_query = function(event) {
        event.preventDefault();
        $scope.loading = true;
    	$http.get('/api/v1/jarvis?text=' + $scope.query + '&access_token='+window.authtoken)
            .then(function (resp) {
                $scope.loading = false;
          var d = resp.data;
	      console.log(d);
	      if(d["type"] == "travel") {
            if(_.has(d, 'accomodation')) {
              $scope.longTravel = true;
              console.log('Long');
            } else {
              $scope.shortTravel = true;
              console.log('short');
            }

	      	$scope.accomodation = d["accomodation"];
            $scope.accomodation.result = _.map($scope.accomodation.result, function (item) {
                item.rating = _.range(Math.floor((Math.random() * 5) + 1));
                return item;
            });

	      	$scope.travel = d["travel"];
	      	$scope.visibility = "travel";
	      	$scope.getRU = $sce.trustAsResourceUrl('https://www.google.com/maps/embed/v1/directions?origin='+$scope.travel['places'][0]['pos']+'&destination='+$scope.travel['places'][1]['pos']+'&key=AIzaSyAeLkV7n7z_Kt44uryKbPWuJ7ISHweKBqM' + '&zoom=3');
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

}]);