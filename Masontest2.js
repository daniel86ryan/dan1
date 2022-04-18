var mostFrequentLetter = function (string) {
 var most = 0, // count
     mostChar = ''; // holds most frequent char
  string.split('').forEach(function(char){ // 
    if(string.split(char).length > most) {
        most = string.split(char).length;
        mostChar = char;
     }
  });
  return mostChar;
};

console.log(mostFrequentLetter("apple")); // "p"
console.log(mostFrequentLetter("banana")); // "a"
console.log(mostFrequentLetter("What about a longer string?")); // " "