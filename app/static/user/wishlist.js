angular.module('myApp.wishlist', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/api/user/:id/wishlist', {
    templateUrl: 'static/templates/wishlist.html',
    controller: 'wishCtrl'
  });
}])

.controller('wishCtrl', ['$scope', '$log', '$http', '$location', '$rootScope',function($scope, $log, $http, $location,$rootScope) {

$scope.toggleVar = true;
if ($rootScope.user == null){
	$location.path('/api/user/login');
}

var usr= $rootScope.user;


    $log.log(usr);

    // get the URL from the input
    //var userInput = $scope.url;
    var email= $scope.email;
    var password= $scope.password;


    // fire the API request
   $http.get('/api/user/' + usr + '/wishlist').
      success(function(results) {
        //$log.log(results);
        var dt=results;
        $scope.wishes=dt["data"]["wishes"]
        $log.log(dt);
        $log.log($scope.wishes);
       
        
      }).
      error(function(error) {
        $log.log(error);
      });

$scope.go= function(){

	$location.path('/api/thumbnail/process');
};

  

}]);
