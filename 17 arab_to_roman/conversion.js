'use strict';

var conversion = (function() {
  function isInt(number) {
    return !isNaN(number) && (function(x) { return (x | 0) === x; })(parseFloat(number));
  }

  function checkInput(number) {
    if (isInt(number)) {
      if (number < 4000 && number > 0) {
        return true;
      } else {
        throw 'Number to convert is out of range';
      }
    } else {
    throw 'Input is not an integer';
    }
  }

  function convertToRoman(number) {
    var result = '';
    var arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    var roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
    for (var i = 0; i <= arab.length; i++) {
      while (number % arab[i] < number) {
        result += roman[i];
        number -= arab[i];
      }
    }
    return result;
  }

  return {
    checkInput: checkInput,
    convertToRoman: convertToRoman
  };
})();

module.exports = conversion;
