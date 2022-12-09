/*
QUESTION:
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Example
 magazine= "attack at dawn"  note= "Attack at dawn"

The magazine has all the right words, but there is a case mismatch. The answer is .

Function Description

Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .
*/
/*
inputs: string

EDGE CASES:
    1. if magazine has few words that note: return "No"


STEPS:
Case Sensitive

1. create empty hashmap
2. save each word in the "magazine" string to a hashmap
return "Yes" or "No"
*/

const checkMagazine = (magazine, note) => {
    const seen = {};

    if (magazine.length < note.length) {
        console.log("No");
        return;
    }

    for (let i = 0; i < magazine.length; i++) {
        let word = magazine[i];
        if (word in seen) {
            seen[word] += 1;
        } else {
            seen[word] = 1;
        }
    }


    for (let i = 0; i <note.length;i++) {
        let word = note[i];
        if (seen[word]) {
            seen[word] -= 1;
        } else {
            console.log("No");
            return;
        }
    }

    for (const word in seen) {
        if (seen[word] < 0) {
            console.log("No");
            return;
        }
    }

    console.log("Yes");
};



let magazine = ["Attack", "At", "Dawn"];
let note = ["Attack", "At", "Dawn"];
checkMagazine(magazine, note);
