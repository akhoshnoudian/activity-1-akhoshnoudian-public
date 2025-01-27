def wordCount(t):
    word_dict = {}  
    
    try:
        with open(t, 'r') as file:
            
            for line_num, line in enumerate(file, 1):
                words = line.split()  # Split line into words
                
                for word in words:
                    # If the word is not in the dictionary, add it with the line number
                    if word not in word_dict:
                        word_dict[word] = [line_num]
                    else:
                        if line_num not in word_dict[word]:
                            word_dict[word].append(line_num)
                 
        
        return word_dict  # Return the dictionary with word occurrences
    
    except FileNotFoundError:
        print(f"The file '{t}' was not found.")
        return {}

print(wordCount("words.txt"))
