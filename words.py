import Word as w

salut = w.Word(["hi"], "salut")
bonjour = w.Word(["hello"], "bonjour")
cava = w.Word(["how are you"], "Ça va")
comment = w.Word(["how", "when"], "comment")

words = [salut, bonjour, cava, comment]

def CheckForWord(word : str):
    for i in range(len(words)):
        for x in range(len(words[i].getEnglish())): 
            comparingWord = words[i].getEnglish()[x]
            
            if comparingWord == word:   return True
        
    return False