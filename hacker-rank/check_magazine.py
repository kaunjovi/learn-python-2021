def checkMagazine(magazine, note):
    for word in note : 
        try : 
            magazine.remove(word)
        except ValueError : 
            return 'No' 
    return 'Yes'
    

if __name__ == "__main__":
    print('Hello.')
    # https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=arcesium