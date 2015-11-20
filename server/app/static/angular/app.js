var app = angular.module('unicornX', []);

app.controller("UnicornCtrl", ['$scope', '$http', '$sce', function($scope,$http,$sce) {
    $scope.visibility = "";

    $scope.isVisible = function (x) {
        return $scope.visibility == x;
    };

    $scope.loading = false;

    //$sce.trustAsResourceUrl("https://maps.googleapis.com/maps/api/directions/json");


    $scope.message = "";
    $scope.query = "";

    $scope.left = function () {
        return 100 - $scope.message.length;
    };
    $scope.clear = function () {
        $scope.message = "";
    };
    $scope.save = function () {
        alert("Note Saved");
    };

    $scope.get_query = function (event) {
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
            products = _.flatten(_.values(d.products));
            $scope.products = [];
            for (var i = 0; i < products.length; i++) {
            	if(products[i]["price"] != "" && products[i]["price"] > 0) {
            		$scope.products.push(products[i]);
            	}
            }
            $scope.visibility = "birthdays";

                } else if (d["type"] == "restaurant_booking") {
                    $scope.visibility = "restaurants";
                    $scope.restaurants = d["restaurants"];

                    var rect = {
                        latMin: $scope.restaurants[0]['lat'],
                        latMax: $scope.restaurants[0]['lat'],
                        lngMin: $scope.restaurants[0]['lng'],
                        lngMax: $scope.restaurants[0]['lng']
                    };

                    $scope.restaurants.forEach(function (restaurant) {
                        console.log('rest: ', restaurant);
                        rect.latMin = Math.min(rect.latMin, restaurant['lat']);
                        rect.latMax = Math.max(rect.latMax, restaurant['lat']);
                        rect.lngMin = Math.min(rect.lngMin, restaurant['lng']);
                        rect.lngMax = Math.max(rect.lngMax, restaurant['lng']);
                    });

                    console.log('Center rectangle: ', rect);
                    console.log('Center lat: ', rect.latMax);
                    console.log('Center lng: ', rect.lngMax);

                    var map = new google.maps.Map(document.getElementById('map'), {
                        zoom: 13,
                        center: new google.maps.LatLng( (rect.latMax + rect.latMin) / 2, (rect.lngMax + rect.lngMin) / 2),
                        mapTypeId: google.maps.MapTypeId.ROADMAP
                    });

                    var infowindow = new google.maps.InfoWindow();

                    var i = 0;

                    $scope.restaurants.forEach(function (restaurant) {
                        marker = new google.maps.Marker({
                            position: new google.maps.LatLng(restaurant['lat'], restaurant['lng']),
                            map: map
                        });

                        var contentString = "<h3>" + restaurant['name'] + "</h3>" +
                            "<h4>" + restaurant['address'] + "</h4>" +
                            "<p>Phone: " + restaurant['phone'] + "</p>" +
                            "<p><a href='" + restaurant['reserve_url'] + "'>Book a table</a></p>" +
                            "<img src='" + restaurant['image_url'] + "' />" +
                            "";

                        google.maps.event.addListener(marker, 'click', (function(marker) {
                            return function() {
                                infowindow.setContent(contentString);
                                infowindow.open(map, marker);
                            }
                        })(marker));
                    });

                } else if (d["type"] == "flights") {
                    $scope.visibility = "flights";
                }
            }
    );
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
    $.toaster({priority: 'success', title: 'Title', message: 'Your message here'});
}

$scope.toDollars = function toDollars(n) {
    return Array(n).join("$");
};

console.log('Controller ready');

}])
;