def main():
    count = 101
    sum_of_digits = 0 
    sum_of_number = 1  #This is the sum of 100! (Not the digits added together)
    
    while(count != 1):
        count -= 1
        sum_of_number *= count

    sum_of_number = str(sum_of_number)

    for digit in sum_of_number:
        sum_of_digits += int(digit)

    print(sum_of_digits)
main()
