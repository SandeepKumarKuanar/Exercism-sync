def translate(text):
    def make(text):
        vowels = ['a', 'e', 'i', 'o', 'u']
        want = ''
        search = text.lower()
        # consonants are those which are not included
        # Rule 1
        if search[:2] == 'xr' or search[:2] == 'yt' or search[0] in vowels:
            want += search
            want += 'ay'
            return want
      
        else: 
            for i in range(len(text)):
            # Rule 3
                if search[i] == 'q' and search[i + 1] == 'u' :
                    move = search.index('qu')
                    want += search[move + 2:]
                    want += search[:move + 2]
                    want += 'ay' 
                    return want
        
            # Rule 4
                elif search[i] == 'y' and i != 0:
                    move = search.index('y')
                    want += search[move:]
                    want += search[:move]
                    want += 'ay'
                    return want
    
                elif search[i] in vowels:
                    put = search.index(search[i])
                    want += search[put:]
                    want += search[:put]
                    want += 'ay'
                    return want
    
    phrase = text.lower().split()
    get = [make(i) for i in phrase]
    return " ".join(get)
    

      