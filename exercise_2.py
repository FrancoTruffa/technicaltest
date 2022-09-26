def annograms(word):  
  word = sorted(word)
  words = [w.rstrip() for w in open('WORD.lst')]
  anagramas = []
  for palabra_of_lst in words:
     if word == sorted(palabra_of_lst):
        anagramas.append(palabra_of_lst)
  return anagramas

if __name__ == "__main__":
    print(annograms("train"))
    print('--')
    print(annograms('drive'))
    print('--')
    print(annograms('python'))
    
