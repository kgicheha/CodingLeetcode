/*
Effiecient for small data values
	Appropriate for data sets which are already partially sorted
Time Complexity: O(N)^2
Space Complexity: O(1)
Process
	Iterate from second element in the array to the last element
	Compate the current element to its predecessor
	If the key element is smaller than its predecessor, compare it to the elements before
Move the greater element one position up to make space for the swapped element

*/

function instertionSort(arr){
    let temp

    for(let i = 1; i < arr.length; i++){
        temp = arr[i]

        for (var j = i - 1; arr[j] > temp && j > -1; j--){
            arr[j + 1] = arr[j]
        }
        arr[j + 1] = temp
    }
    return arr
}

console.log(instertionSort([4,2,6,5,1,3]))