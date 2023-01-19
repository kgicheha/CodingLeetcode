'''
1418. Display Table of Food Orders in a Restaurant

Given the array orders,
which represents the orders that customers have done in a restaurant.
 More specifically orders[i]=[customerNamei,tableNumberi,foodItemi]
 where customerNamei is the name of the customer,
 tableNumberi is the table customer sit at,
 and foodItemi is the item customer orders.

Return the restaurant's “display table”.
The “display table” is a table whose row entries denote
how many of each food item each table ordered.
The first column is the table number and the remaining columns
correspond to each food item in alphabetical order.
The first row should be a header whose first column is “Table”,
followed by the names of the food items.
Note that the customer names are not part of the table.
Additionally, the rows should be sorted in numerically increasing order.
'''

'''
Example 1:

Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],
            ["David","3","Fried Chicken"],["Carla","5","Water"],
            ["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
            ["3","0","2","1","0"],
            ["5","0","1","0","1"],
            ["10","1","0","0","0"]]
Explanation:
The displaying table looks like:
Table,Beef Burrito,Cevaiche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito".
'''

def displayTable(orders):
    food_items = []
    table_nums = []
    map_orders = {}

    for order in orders:
        if order[2] not in food_items:
            food_items.append(order[2])
        if int(order[1]) not in table_nums:
            table_nums.append(int(order[1]))
        new_order = (int(order[1]), order[2])
        if new_order not in map_orders:
            map_orders[new_order] = 1
        else:
            map_orders[new_order] += 1

    food_items.sort()
    table_nums.sort()
    food_items.insert(0, 'Table')

    answer = []
    answer.append(food_items)

    for i in range(len(table_nums)):
        new_entry = []
        for j in range(len(food_items)):
            if j == 0:
                new_entry.append(str(table_nums[i]))
            else:
                entry_tuple = (table_nums[i], food_items[j])
                if entry_tuple in map_orders:
                    new_entry.append(str(map_orders[entry_tuple]))
                else:
                    new_entry.append('0')

        answer.append(new_entry)
        new_entry = []

    return answer

    print(orders)


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

print(displayTable(orders))