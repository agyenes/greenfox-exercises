'use strict';

const decrypt = (function() {

	function decryptor(str, amount, callback) {
		if (amount < 0)
			return decryptor(str, amount + 26);
		var output = '';
		for (var i = 0; i < str.length; i ++) {
			var char = str[i];
			if (char.match(/[a-z]/i)) {
				var code = str.charCodeAt(i);
				if ((code >= 65) && (code <= 90))
					char = String.fromCharCode(((code - 65 - amount) % 26) + 65);
				else if ((code >= 97) && (code <= 122))
					char = String.fromCharCode(((code - 97 - amount) % 26) + 97);
			}
			output += char;
		}
		return callback(output);
	};

	return {
    decryptor
	}
}());

module.exports = decrypt;
