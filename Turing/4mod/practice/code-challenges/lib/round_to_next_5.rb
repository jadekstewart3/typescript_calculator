def round_to_next(int)
 remainder = int % 5
  if remainder > 0 
  int + (5- remainder)
  else 
    int
  end
end