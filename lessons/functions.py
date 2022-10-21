def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  
  elif row_number < 30:
    location = 'middle'
  
  else:
    location = 'back'
  
  return location
