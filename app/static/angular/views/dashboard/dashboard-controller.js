"use strict";
angular.module('myApp.dashboard',['ui.bootstrap','components'])
  .controller('DashboardController',
    function($rootScope, $scope, $location,$cookieStore,$http) {

      $scope.currentUser = $rootScope.globals.currentUser;
      $scope.avatorImg = "img/"+$rootScope.globals.currentUser.avator;
      console.log($scope.avatorImg);
      var mobileView = 992;

      $scope.getWidth = function() {
          return window.innerWidth;
      };

      $scope.$watch($scope.getWidth, function(newValue, oldValue) {
          if (newValue >= mobileView) {
              if (angular.isDefined($cookieStore.get('toggle'))) {
                  $scope.toggle = ! $cookieStore.get('toggle') ? false : true;
              } else {
                  $scope.toggle = true;
              }
          } else {
              $scope.toggle = false;
          }

      });

      $scope.toggleSidebar = function() {
          $scope.toggle = !$scope.toggle;
          $cookieStore.put('toggle', $scope.toggle);
      };

      window.onresize = function() {
          $scope.$apply();
      };
      $scope.logout = function(){
        console.log("logout")
        $rootScope.globals = {};
        $cookieStore.remove('globals');
        $http.defaults.headers.common.Authorization = 'Basic';
      }


    }

  );
