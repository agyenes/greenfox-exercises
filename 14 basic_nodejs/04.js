'use strict';

function Car(type, color, balance) {
    this.type = type;
    this.color = color;
    this.balance = balance;
    this.id = Car.currentCarId++;
    this.enterDate = 0;
}

Car.currentCarId = 0;

Car.prototype.enter = function(enterDate) {
  this.enterDate = enterDate;
};

Car.prototype.getEnterDate = function() {
  return this.enterDate;
};

Car.prototype.leave = function(price) {
  this.balance -= price;
};

Car.prototype.getStats = function() {
  return 'Type: ' + this.type + ', Color: ' + this.color + ', Balance: ' + this.balance;
};

module.exports.Car = Car;

function CarPark(income, startTime) {
  this.income = income;
  this.time = startTime;
  this.cars = [];
}

CarPark.prototype.carEnter = function(car) {
  car.enter(this.time);
  this.cars.push(car);
};

CarPark.prototype.carLeave = function(carId) {
  var _this = this;
  this.cars = this.cars.filter(function(car) {
    if (car.id === carId) {
      _this.pay(car);
      return false
    }
    return true;
  });
};

CarPark.prototype.pay = function(car) {
  var HOURLY_PRICE = 40;
  var HOUR = 60 * 60 * 1000;
  var elapsedHours = Math.floor((this.time - car.getEnterDate()) / HOUR);
  var price = HOURLY_PRICE * elapsedHours;
  car.leave(price);
};

CarPark.prototype.elapseTime = function(time) {
  this.time += time;
};

// CarPark.prototype.getStats = function() {
//   console.log('Cars: ' + this.number_of_cars + ' Time: ' + this.color + ' Income: ' + this.income)
// };
//
// CarPark.prototype.getParkingCarsSince = function(hour) {
//   cars_in_park.forEach(function(e) {
//     if (e.this.elapsed_time > hour) {
//       parkingCarsSince ++;
//       }
//     })
//   };

module.exports.CarPark = CarPark;
