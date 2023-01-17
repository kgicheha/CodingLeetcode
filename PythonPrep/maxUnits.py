'''
1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto one truck.
You are given a 2D array boxTypes,
where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize,
which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the
number of boxes does not exceed truckSize.

'''

'''
EXAMPLE 1
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
'''

'''
GIVEN:
    2D array: stores the number of boxes, and the units each box contains
    truckSize
STEPS:
    sort the boxTypes based on the units that each box contains
        sort in descending order
    create a variably that keeps track of max units(how many boxes you've put in the truck so far)
        initialize variable as 0

    loop through the sorted box types
        if the box is less than the truckSize
            increase the max units by the (box * units of the box)
            reduce the truckSize by the number of boxes we just put in the truck
        else: if the number of boxes > truckSize
            return the max_units + (truckSize * unit)

RETURN: the maximum total number of units that can be put on the truck


TIME COMPLEXITY: O(N log N)
    because the sort function takes O(n log n), which is the worst case scenario
    for loop takes O(n)
SPACE COMPLEXITY: 0(1)
'''

def maximumUnits(boxTypes, truckSize):

   boxTypes.sort(key = lambda x: x[1], reverse = True)

   max_units = 0

   for box, unit in boxTypes:
        if box <= truckSize:
            max_units += (box * unit)
            truckSize -= box
        else:
            return max_units + (truckSize * unit)

   return max_units

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 4

print(maximumUnits(boxTypes, truckSize))