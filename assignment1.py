# Name: Suhrob Hasanov
# OSU Email:
# Course:       CS261 - Data Structures
# Assignment: Assignment 1
# Due Date: 1/30/23
# Description: Python programming practice 


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    # Setting min and max to first number in array
    minNum = arr[0]
    maxNum = arr[0]
    # print(f'array value-- {arr[0]} --')
    # Iterating through numbers to compare the first number to rest
    for i in range(0, arr.length()):
        if(minNum > arr[i]):
            minNum = arr[i]
        if(maxNum < arr[i]):
            maxNum = arr[i]
    return (minNum, maxNum)
     
    

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    newArray = StaticArray(arr.length())
    
    for i in range(0, arr.length()):
        
        if(arr[i] % 3 == 0 and arr[i] % 5 == 0):
            newArray.set(i, "fizzbuzz")
        elif(arr[i] % 3 == 0):
            newArray.set(i, "fizz")
        elif(arr[i] % 5 == 0):
            newArray.set(i, "buzz")
        else:
            newArray.set(i, arr[i])
    return newArray

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    # Even array
    if(arr.length() % 2 == 0):
      loopRange = int(arr.length() / 2)
      #print("loopRange", loopRange)
      for i in range(0, loopRange):
        # print(i)
        # print(arr[arr.length() - 1 - i])
        temp = arr[i]
        arr[i] = arr[arr.length() - 1 - i]
        arr[arr.length() - 1 - i] = temp
    # Odd array
    else:
      loopRange = int(arr.length() // 2) 
      for i in range(0, loopRange):
        temp = arr[i]
        arr[i] = arr[arr.length() - 1 - i]
        arr[arr.length() - 1 - i] = temp

    #return arr

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    newArray = StaticArray(arr.length())
    stepsNegative = False

    if(steps == 0):
      newArray = arr
      return newArray
  
    if(steps < 0):
      # not sure if I am allowed to use abs() method
      steps = steps * (-1)
      stepsNegative = True
      if(steps > arr.length()):
        # print("steps", steps)
        steps = steps % arr.length()
    else:
      if(steps > arr.length()):
        steps = steps % arr.length()
    # print("Remainder", steps % arr.length()) # if bigger than 6 
        
    if(stepsNegative):
      for i in range(0, (arr.length() - steps)):
         newArray[i] = arr[steps + i]
      for i in range(0, steps):
        newArray[arr.length() - steps + i] = arr[i]
    else:
      for i in range(0, (arr.length() - steps)):
        newArray[steps + i] = arr[i]
      for i in range(0, steps):
        newArray[i] = arr[arr.length() - steps + i]

    return newArray

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    

      
    if( start < end):
      if(start < 0 and end >= 0):
        loopRange = end - start
        newArraySize = loopRange + 1
        newArray = StaticArray(newArraySize)
      else:   
        loopRange = abs(end - start)
        newArraySize = loopRange + 1
        newArray = StaticArray(newArraySize)
      for i in range(0, loopRange):
        newArray[i + 1] = start + i + 1
      newArray[0] = start
      newArray[newArraySize - 1] = end
      
    elif(start > end):
      if(start < 0):
        loopRange = abs(abs(end) - abs(start))
        newArraySize = loopRange + 1
        newArray = StaticArray(newArraySize)
      elif(start >= 0):
        loopRange = abs(start - abs(end))
        newArraySize = loopRange + 1
        newArray = StaticArray(newArraySize)
      for i in range(0, loopRange):
        newArray[i + 1] = start - i - 1  # Maybe + 1 somewhere else? 
        newArray[0] = start
        newArray[newArraySize - 1] = end
        
    elif(start == end):
      newArray = StaticArray(1)
      newArray[0] = start
      return newArray

    return newArray

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    accending = None
    decending = None
    
    if(arr.length() == 1):
      # print("Array of 1")
      return 1
      
    for i in range(0, arr.length() - 1):
      
      
      if(arr[i] < arr[i + 1]): # first is smaller then next
        if(decending):
          return 0
        accending = True
        
      elif(arr[i] > arr[i + 1]):
        if(accending):
          return 0
        decending = True
      else:
        return 0

    if accending:
      return 1
    return -1
# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    mode = arr[0]
    frequency = 1
    tempFrequency = 1

    if(arr.length() == 2):
      if(arr[0] == arr[1]):
         mode = arr[0]
         frequency = 2
         return (mode, frequency) 
      
    for i in range(0, arr.length() - 1):
      if(arr[i] == arr[i + 1]):
        if(mode == arr[i]):
          frequency += 1
        elif(mode == arr[0] and frequency == 1):
          mode = arr[i]
          frequency += 1
        elif(mode != arr[i]):
          tempFrequency += 1
        if(frequency < tempFrequency):
          frequency = tempFrequency
          mode = arr[i]
      else:
        tempFrequency = 1
      
    
        
      
    return (mode, frequency)
# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    if(arr.length() == 1):
      newArray = StaticArray(1)
      newArray[0] = arr[0]
      return newArray
 
    counter = 0   # count of unique numbers
    for i in range(0, arr.length() - 1):
      if(arr[i] != arr[i + 1]):
        counter += 1
    counter += 1 # for last number
    #print("counter", counter)

    newArray = StaticArray(counter)

    arrayOrder = 0
    prevNumber = None
    for i in range(0, arr.length()):
      if(arr[i] != prevNumber or prevNumber == None):
        newArray[arrayOrder] = arr[i]
        arrayOrder += 1
     
      prevNumber = arr[i] 
    return newArray
    
       


  
# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    minMaxValues = min_max(arr)
    min = minMaxValues[0]
    max = minMaxValues[1]
    #print("min", min)
    #print("max", max)

    negativeNumbers = False
    
    if(min < 0):
        
        numbersRange = abs(max - min)
        numbersRange += 1
        #print("range", numbersRange)
        negativeNumbers = True
        for i in range(0, arr.length()):
            #make new array here
           # arr[i] += numbersRange # Will it always make it pos? 
            arr[i] += min * (-1)
        #print("arr after range added", arr)
        # min += numbersRange
        # max += numbersRange
        min += min * (-1)
        max += min * (-1)
        #print("new min man", min, max)
    else:
        numbersRange = abs(max - min)
        numbersRange += 1
        #print("range", numbersRange)

    if(numbersRange > arr.length()):
        count_array = StaticArray(numbersRange)
    else:
        count_array = StaticArray(arr.length())

    for i in range(count_array.length()):
      count_array[i] = 0

        

  
    for i in range(0, arr.length()):
        if(min == 0):
            countIndex = arr[i]
            # #print("Count index", countIndex)
            count_array[countIndex] += 1
            ##print("count_array after 1 added", count_array)
        elif(min > 0 and not negativeNumbers):
            countIndex = arr[i] - min
            ##print("Count index", countIndex)
            count_array[countIndex] += 1
            ##print("count_array after 1 added", count_array)
        elif(negativeNumbers):
            # subtracting from each number in order to make the countIndex 0
            ##print("Pow")
            
            countIndex = arr[i]
            ##print("Count index", countIndex)
            ##print(min)
            count_array[countIndex] += 1
            #count_array[0] = 1
            ##print("count_array after 1 added", count_array)

    for i in range(1, count_array.length()):
        count_array[i] = count_array[i - 1] + count_array[i]
    ##print("Count array after additions", count_array)
    
    newArray = StaticArray(arr.length())
    ##print("new array length", newArray.length())
    for i in range(0, newArray.length()):
        if(min >= 0):
            if(negativeNumbers):
                
                newArrayIndex = count_array[arr[arr.length() - 1 - i]] - 1 
                #                              [ 7          - 1 -  1]
                #print("Bang!")
                #print("i", i)
                #print("new array index", newArrayIndex)
                #print("min", min)
                newArray[newArray.length() - 1 - newArrayIndex] = arr[arr.length() - 1 - i] - (minMaxValues[0] * (-1))
                #print("new array", newArray)
                count_array[arr[arr.length() - 1 - i]] -= 1
            else:
                #print("Bing!")
             
                #print("i", i)
                #print("min", min)
                newArrayIndex = count_array[arr[arr.length() - 1 - i] - min ] - 1
                #print("new array index", newArrayIndex)
                newArray[newArray.length() - 1 - newArrayIndex] = arr[arr.length() - 1 - i]
                #print("new array", newArray)
                count_array[arr[arr.length() - 1 - i] - min ] -= 1
        else:
            newArrayIndex = count_array[arr[arr.length() - 1 - i]] - 1
            newArray[newArray.length() - 1 - newArrayIndex] = arr[arr.length() - 1 - i]
            
            #print("new array", newArray)
            # decrementing the count of the element by one
            count_array[arr[arr.length() - 1 - i]] -= 1

    for i in range(0, arr.length()):
        if(minMaxValues[0] < 0):
            arr[i] -= minMaxValues[0] * (-1)
            

    return newArray

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    oddArray = False
    
    newArray = StaticArray(arr.length())
    # Array of 1 elem
    if(arr.length() == 1):
        newArray[0] = arr[0]*arr[0]
        return newArray
    # array of 2 elem
    elif(arr.length() == 2):
        if(abs(arr[0]) < abs(arr[1])):
            newArray[0] = arr[0] * arr[0]
            newArray[1] = arr[1] * arr[1]
        else:
            newArray[0] = arr[1] * arr[1]
            newArray[1] = arr[0] * arr[0]
    
    if(arr.length() % 2 == 0):
        loopRange = arr.length() / 2
    elif(arr.length() % 2 != 0):
        loopRange = arr.length() // 2
        oddArray = True
    
    # if first elem is zero
    if(arr[0] >= 0):
        for i in range(0, newArray.length()):
            newArray[i] = arr[i]*arr[i]
    # if last elem is zero
    elif(arr[arr.length() - 1] == 0):
        for i in range(0, newArray.length()):
            newArray[newArray.length() - 1 - i] = arr[i]*arr[i]
    # If first number is negative
    else:
        incrementStep = 0
        for i in range(0, int(loopRange)):
            if(abs(arr[i]) == abs(arr[arr.length() - 1 - i])):
                newArray[newArray.length() - 1 - incrementStep] = arr[i] * arr[i]
                newArray[newArray.length() - 2 - incrementStep] = arr[i] * arr[i]
                incrementStep += 2
                
            elif(abs(arr[i]) > abs(arr[arr.length() - 1 - i])):
                newArray[newArray.length() - 1 - i] = arr[i] * arr[i]
                newArray[i] = arr[arr.length() - 1 - i] * arr[arr.length() - 1 - i]
                if (newArray[1] != None):
                    if(newArray[i] > newArray[i + 1]):
                        temp = newArray[i] 
                        newArray[i] = newArray[i + 1]
                        newArray[i + 1] = temp
                #incrementStep += 2
                
            # elif(abs(arr[i]) < abs(arr[arr.length() - 1 - i])):
            #     newArray[newArray.length() - 1 - incrementStep] = arr[arr.length() - 1 - i] * arr[arr.length() - 1 - i]
            #     newArray[newArray.length() - 2 - incrementStep] = arr[i] * arr[i]
                
            if(i == loopRange - 1 and oddArray and arr[i + 1] == 0):
                newArray[0] = arr[i + 1]
            else:
                newArray[i + 1] = arr[i + 1] * arr[i + 1]
                

    return newArray
# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print('\n# min_max example 1')
    # arr = StaticArray(5)
    # for i, value in enumerate([7, 8, 6, -5, 4]):
    #     arr[i] = value
    # print(arr)
    # result = min_max(arr)
    # if result:
    #     print(f"Min: {result[0]: 3}, Max: {result[1]}")
    # else:
    #     print("min_max() not yet implemented")

    # print('\n# min_max example 2')
    # arr = StaticArray(1)
    # arr[0] = 100
    # print(arr)
    # result = min_max(arr)
    # if result:
    #     print(f"Min: {result[0]}, Max: {result[1]}")
    # else:
    #     print("min_max() not yet implemented")

    # print('\n# min_max example 3')
    # test_cases = (
    #     [3, 3, 3],
    #     [-10, -30, -5, 0, -10],
    #     [25, 50, 0, 10],
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr)
    #     result = min_max(arr)
    #     if result:
    #         print(f"Min: {result[0]: 3}, Max: {result[1]}")
    #     else:
    #         print("min_max() not yet implemented")

    # print('\n# fizz_buzz example 1')
    # source = [_ for _ in range(-5, 20, 4)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr[i] = value
    # print(fizz_buzz(arr))
    # print(arr)

    # print('\n# reverse example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # reverse(arr)
    # print(arr)
    # reverse(arr)
    # print(arr)

    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
    #     space = " " if steps >= 0 else ""
    #     print(f"{rotate(arr, steps)} {space}{steps}")
    # print(arr)

    # print('\n# rotate example 2')
    # array_size = 1_000_000
    # source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr[i] = value
    # print(f'Started rotating large array of {array_size} elements')
    # rotate(arr, 3 ** 14)
    # rotate(arr, -3 ** 15)
    # print(f'Finished rotating large array of {array_size} elements')

    # print('\n# sa_range example 1')
    # cases = [
    #     (1, 3), (-1, 2), (0, 0), (0, -3),
    #     (-95, -89), (-89, -95)]
    # for start, end in cases:
    #     print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    # print('\n# is_sorted example 1')
    # test_cases = (
    #     [-100, -8, 0, 2, 3, 10, 20, 100],
    #     ['A', 'B', 'Z', 'a', 'z'],
    #     ['Z', 'T', 'K', 'A', '5'],
    #     [1, 3, -10, 20, -30, 0],
    #     [-10, 0, 0, 10, 20, 30],
    #     [100, 90, 0, -90, -200],
    #     ['apple']
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     result = is_sorted(arr)
    #     space = "  " if result and result >= 0 else " "
    #     print(f"Result:{space}{result}, {arr}")

    # print('\n# find_mode example 1')
    # test_cases = (
    #     [-820, -449, -435, -435, 24, 24, 473, 959],
    #     [-820, -449, -435, -435, 24, 24, 24, 473, 959],
    #     [-820, -820, -820, -449, -435, -435, 24, 24, 24, 473, 959],
    #     [1, 20, 30, 40, 500, 500, 500],
    #     [2, 2, 2, 2, 1, 1, 1, 1],
    #     ["zebra", "sloth", "otter", "otter", "moose", "koala"],
    #     ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
        
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value

    #     result = find_mode(arr)
    #     if result:
    #         print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
    #     else:
    #         print("find_mode() not yet implemented\n")

    # print('# remove_duplicates example 1')
    # test_cases = (
    #     [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
    #     [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr)
    #     print(remove_duplicates(arr))
    # print(arr)

    # print('\n# count_sort example 1')
    # test_cases = (
    #     [1, 2, 4, 3, 0],[1, 2, 4, 3, 0, 4],
    #     [1, 2, 4, 3, 5], [5, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
    #     [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
    #     [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     before = arr if len(case) < 50 else 'Started sorting large array'
    #     print(f"Before: {before}")
    #     result = count_sort(arr)
    #     after = result if len(case) < 50 else 'Finished sorting large array'
    #     print(f"After : {after}")
    #     print("----------------------------------------------")
    # print('\n# count_sort example 2')
    # array_size = 5_000_000
    # min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    # max_val = min_val + 998
    # case = [random.randint(min_val, max_val) for _ in range(array_size)]
    # arr = StaticArray(len(case))
    # for i, value in enumerate(case):
    #     arr[i] = value
    # print(f'Started sorting large array of {array_size} elements')
    # result = count_sort(arr)
    # print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [-6, -5, -3, 1, 2],
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-4, -3, -2, -1, 0, 1, 2, 3, 4],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)
        print("------------------------------")

    # print('\n# sorted_squares example 2')
    # array_size = 5_000_000
    # case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    # arr = StaticArray(len(case))
    # for i, value in enumerate(sorted(case)):
    #     arr[i] = value
    # print(f'Started sorting large array of {array_size} elements')
    # result = sorted_squares(arr)
    # print(f'Finished sorting large array of {array_size} elements')
