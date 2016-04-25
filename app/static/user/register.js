angular.module('myApp.register', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/api/user/register', {
    templateUrl: 'static/templates/register.html',
    controller: 'regCtrl'
  });
}])

.controller('regCtrl', ['$scope', '$log', '$http', '$location',function($scope, $log, $http, $location) {
$scope.toggleVar = true;
$scope.getResults = function() {

    $log.log("test");

    // get the URL from the input
    //var userInput = $scope.url;
    var email= $scope.email;
    var password= $scope.password;
    var username= $scope.username;

    // fire the API request
    $http.post('/api/user/register', {"email": email, "password": password, "username": username}).
      success(function(results) {
        $log.log(results);
        var dt = results;
        $scope.msg= dt["message"];
        if(dt["error"]=="1"){
        	$scope.toggleVar = false;
      		}
      	else{
      		$scope.toggleVar = false;
      		$location.path('/api/user/login');
      		}
      }).
      error(function(error) {
        $log.log(error);
      });

  };

}]);
