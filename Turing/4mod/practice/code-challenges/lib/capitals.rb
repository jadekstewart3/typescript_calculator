def capitals(word)
  characters = word.chars
  indecies = []
  characters.each_with_index  do |char, i|
    if char.match(/^[A-Z]+$/)
      indecies << i
    end
  end
  indecies
end