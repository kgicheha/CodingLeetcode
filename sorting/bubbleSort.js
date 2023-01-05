/*
Bubble Sort
Works by repeatedly swapping the adjacent elements if they are in the wrong order
Not suitable for large data sets because its average and worst-case time complexity are quite high
Time Complexity: O(N)^2
Space Complexity: O(1)
Process:
	Starts with the very first two elements, comparing them to check which one is greater
	If the element current element is greater than the right, you swap them
	If the element current element is less than the right, you move to the next element


*/

function bubbleSort(arr){
    for(let i = arr.length - 1; i > 0; i--){
        for (let j = 0; j < i; j ++){
            if (arr[j] > arr[j+1]){
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
    return arr
}