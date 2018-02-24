#Main Function
def lol() :
     item = int(raw_input("Enter a number 1 - 10 : "))
     numbers = range(1,11)
     min = 0
     max = len(numbers) - 1
     found = False
     while not found :
      if item < 10 :
       while not found :
         mid = int((max + min) // 2)
         if numbers[mid] == item :
             found = True
         else :
             if item <= numbers[mid] :
                 max = mid - 1
             elif item >= numbers[mid] :
                 min = mid + 1
      else :
          print("Enter a valid number")
          break ;
     return found


print(lol())







