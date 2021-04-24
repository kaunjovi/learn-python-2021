# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    # print (arr)
    length = len(arr)
    pos_count = 0 
    neg_count = 0 
    zero_count = 0

    for n in arr : 
        if n > 0 : 
            pos_count+= 1 
        elif n < 0 : 
            neg_count+= 1 
        else : 
            zero_count+= 1 
    
    # print(f'{length}, {pos_count}, {neg_count}, {zero_count}')
    # print(f'{length}, {pos_count / length}, {neg_count/ length}, {zero_count/ length}')

    print("{:.6f}".format(pos_count / length));
    print("{:.6f}".format(neg_count/ length));
    print("{:.6f}".format(zero_count/ length));

    # Write your code here

if __name__ == "__main__":
    print ('Hello')