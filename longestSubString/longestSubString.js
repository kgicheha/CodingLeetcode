/*
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring without repeating characters.
*/

/*
STEPS:
SLIDING WINDOW TECHNIQUE
1. create empty object to keep track of frequency of the character
    if character appears more that once in subarray, then move on to the next subarray
2. Create a variable that keeps track of the max number of characters
    increase this number until you get a character thats already in the substring
3. create two pointers
    one pointer stays on current character
    the other pointer moves up in the string
4. traverse string
    one pointer stays at the current character as the other pointer move forward in string
    add the character in the empty object
        if the character doesnt exist, add 1 as its value
        else increase its count by 1

    while any of the characters in object has a count thats more than 1:
        i. set the first pointer to the current character
        ii. reduce the count by 1 or delete the character from object if the character count is equal to 0
        iii. compare the current length of substring to the current max length
            if the current length is more than the max string
                set it as the new max length
                since the problem wants us to returnt the length, we can to add 1
                    reminder: indexes start from 0, which is why we want to add 1

5. return the maxLength

*/

const lengthOfLongestSubstring = (s) =>{
    let maxLength = 0,
        windowStart = 0,
        soFar = {}

    for(let windowEnd = 0; windowEnd < s.length; windowEnd++){
        let rightChar = s[windowEnd];

        soFar[rightChar] = soFar[rightChar] + 1 || 1;

        while(soFar[rightChar] > 1){
            let leftChar = s[windowStart]

            soFar[leftChar] > 1  ? soFar[leftChar]-- : delete soFar[leftChar];

            windowStart++
        }

        maxLength = Math.max(maxLength, (windowEnd - windowStart) + 1)
    }
    console.log(maxLength)
}

lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")