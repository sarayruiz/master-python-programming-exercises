def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here 
    hr1 = 3600 * hr1
    min1 = 60 * min1
    total1 = hr1 + min1 + sec1
    hr2 = 3600 * hr2
    min2 = 60 * min2
    total2 = hr2 + min2 + sec2

    return total2 - total1


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
print(two_timestamp(1,2,30,1,3,20))