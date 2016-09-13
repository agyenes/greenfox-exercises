var myNinjaApp = angular.module('myNinjaApp', ['ngRoute', 'ngAnimate']);

myNinjaApp.config(['$routeProvider', '$locationProvider' function($routeProvider, $locationProvider) {

  $locationProvider.html5mode(true);

  $routeProvider
    .when('/home', {
      templateUrl: 'views/home.html',
      controller: 'NinjaController'
    })
    .when('/contact', {
      templateUrl: 'views/contact.html',
      contact: 'ContactController'
    })
    .when('/contact-success', {
      templateUrl: 'views/contact-success.html',
      contact: 'ContactController'
    })
    .when('/directory', {
      templateUrl: 'views/directory.html',
      controller: 'NinjaController'
    }).otherwise({
      redirectTo: '/home'
    });
}]);

myNinjaApp.directive('randomNinja', [function() {
  return {
    restrict: 'E',
    scope: {
      ninjas: '=',
      title: '='
    },
    templateUrl: 'views/random.html',
    // controller function($scope) {
    //   $scope.random = Math.floor * (Math.random() * 4);
    // }
  };
}])

myNinjaApp.controller('NinjaController', ['$scope', '$http', function($scope, $http) {
  $scope.removeNinja = function(ninja) {
    var removedNinja = $scope.ninjas.indexOf(ninja);
    $scope.ninjas.splice(removedNinja, 1);
  }

  $scope.addNinja = function() {
    $scope.ninjas.push({
        name: $scope.newninja.name,
        colour: $scope.newninja.colour,
        rate: parseInt($scope.newninja.rate),
        available: true
    });

    $scope.newninja.name = "";
    $scope.newninja.colour = "";
    $scope.newninja.rate = "";
  }

  $http.get('data/ninjas.json').success(function(data) {
    $scope.ninjas = data;
  })
}]);

myNinjaApp.controller('ContactController', ['$scope', '$location', function($scope, $location) {

  $scope.sendMessage = function() {
    $location.path('/contact-success');
  };

}]);
