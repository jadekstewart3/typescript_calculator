def increment_string(string)
  # int_array = []
  # extracted_ints = string.chars.each do |char|
  #   if char =~ /[0-9]$/

  #     int_array << char
  #   end
  # end
  # require 'pry'; binding.pry
  # if int_array.empty?
  #   string + "1"
  # else
  #   extracted_ints.join + "#{(int_array.join.to_i + 1)}"
  # end
  int_match = string.match(/(\d+)$/)
  if int_match
    numeric_part = int_match[0]
    incremented_numeric_part = (numeric_part.to_i + 1).to_s.rjust(numeric_part.length, "0")
    #rjust == right justify pads a string with a character to reach a specified length
    string.sub("#{numeric_part}", "#{incremented_numeric_part}")
  else
    string << "1"
  end
end