angular.module('app', [])
  .controller('BirthdayCtrl', function($http) {
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
  });
