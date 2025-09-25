"""def hours_minutes(seconds):
  # Your code here
  minute = seconds//60
  hour = seconds // 3600
  return hour, minute

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
"""

def hours_minutes(seconds):
  # Your code here
  hours = seconds // 3600
  remaining_seconds = seconds % 3600
  minutes = remaining_seconds // 60
  return (hours, minutes)

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
