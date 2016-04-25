angular.module('myApp.login', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/api/user/login', {
    templateUrl: 'static/templates/login.html',
    controller: 'logCtrl'
  });
}])

.controller('logCtrl', ['$scope', '$log', '$http', '$location', '$rootScope',function($scope, $log, $http, $location,$rootScope) {
$scope.toggleVar = true;
$scope.getResults = function() {

    $log.log("test");

    // get the URL from the input
    //var userInput = $scope.url;
    var email= $scope.email;
    var password= $scope.password;


    // fire the API request
    $http.post('/api/user/login', {"email": email, "password": password}).
      success(function(results) {
      var dt=results;
      $scope.msg= dt["message"];
      if(dt["error"]=="1"){
        	$scope.toggleVar = false;
      }
      else{
      		$scope.toggleVar = false;
      		$rootScope.user= dt["data"]["user"]["id"];
      		$log.log($rootScope.user);
      		$location.path('/api/thumbnail/process');
      }
        $log.log(results);
      }).
      error(function(error) {
        $log.log(error);
      });

  };

}]);
