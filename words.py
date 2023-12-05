import Word

salut = Word.Word("hi", "salut")
bonjour = Word.Word("hello", "bonjour")

words = [salut, bonjour]

def CheckForWord(word : str):
    for i in range(len(words)):
        if words[i].getEnglish() == word:
            return True
    
    return False