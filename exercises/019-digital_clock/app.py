def digital_clock(n):
  hours= n//60
  minutes=n%60

  return hours,minutes

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(150))