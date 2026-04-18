def findMax(numbers):
    max_value = numbers[0]
    index_start = 0
    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            index_start = i
    return index_start
def evenOrOdd(number_list, string_list):
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            string_list.append("even")
        else:
            string_list.append("odd")
number_list = [56, 77, 23, 12, 88, 59, 97, 33, 38, 64]
string_list = []
max_index = findMax(number_list)
evenOrOdd(number_list, string_list)
print("The largest value in the list is " + str(number_list[max_index]) + " located at index position " + str(max_index) + ".")
print("The numbers were:")
for i in range(len(number_list)):
    print("Number " + str(number_list[i]) + " is " + string_list[i])
       
            
    

