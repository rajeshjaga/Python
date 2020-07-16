cont = {0:"This" ,
             1:"is", 
             2:"lab6", 
             3:"program" ,
             4:"dirt" ,
             5:"in" ,
             6:"python" ,
             7:"programing", 
             8:"subject" ,
             9:"abbey" 
             }
def Ordered(): 
    word = ' ' 
    for word in cont.values(): 
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1
        while i < l:          
            if (ord(word[i]) > ord(word[i+1])): 
                result = 'Word is not ordered'
                break
            else: 
                i += 1
        if (result == 'Word is ordered'): 
            print(word,': ',result) 
if __name__ == '__main__': 
    Ordered()
