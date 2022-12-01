/*
58. Given a string s consisting of words and spaces,
return the length of the last word in the string.
*/

/*
EDGE CASES:
    empty string
    string that has only spaces

SOLUTION:
    create keep a counter variable
    start from the end and loop to the front
    if the character is a space or blank, move to the next character
    once you get to a character
        create another loop that increasres the count until you get to the next space or blank
    return lastWordCount


    TIME COMPLEXITY: O(N) because its one loop
    SPACE COMPLEXITY: O(1) because you're only creating an integer to store the word count
*/

const lengthOfLastWord = (s) => {
  let lastWordCount = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] !== " ") {
      for (let j = i; j >= 0; j--) {
        if (s[j] !== " ") {
            lastWordCount++;
        } else {

            console.log(lastWordCount);
            return lastWordCount;
        }
      }
      console.log(lastWordCount);
      return lastWordCount;
    }
  }

};

lengthOfLastWord("Hello World");
lengthOfLastWord("Hello World! ");
lengthOfLastWord(" ");
