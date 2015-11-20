var app = angular.module("unicornX", []);

app.controller("unicornCtrl", function($scope) {
    $scope.message = "";
    $scope.query = "";
    $scope.left  = function() {return 100 - $scope.message.length;};
    $scope.clear = function() {$scope.message = "";};
    $scope.save  = function() {alert("Note Saved");};
    $scope.get_query = function() {
    	$.get('/api/v1/jarvis?text=' + $scope.query, function (d) {
	      $('#herestuff').html(d);
	      console.log(d);
	    });
    };

    $scope.quornuj = function () {
        alert('Changed', $scope.query);
    };

});