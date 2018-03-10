var verses = require('./verses.json');

exports.getRandomOne = function() {
  var totalAmount = verses.length;
  var rand = Math.floor(Math.random() * totalAmount);
  return verses[rand];
}
