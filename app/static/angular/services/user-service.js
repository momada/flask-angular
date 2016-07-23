"use strict";
angular.module('myApp.userService', ['myApp.authUtils'])
  .service('userService', function($rootScope,$http, $location,$cookieStore, Base64) {


    this.doLogin = function(username, password) {
      var promise = $http({method: 'POST', url: '/api/user/authentication',
          data: {
            'username': username,
            'password': password
          }
        })
            .success(function(data) {
              $rootScope.globals.currentUser = data;
              var authdata = Base64.encode(username + ':' + password);
              $rootScope.globals.authdata=authdata;
              $http.defaults.headers.common['Authorization'] = 'Basic ' + authdata;
              $cookieStore.put('globals', $rootScope.globals);
              
            }).
            error(function() {
              console.log("failed to login");
            });
      return promise;
    };

  });
