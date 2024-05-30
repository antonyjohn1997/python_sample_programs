def binary_search(card_list,card):
    low=0
    high=len(card_list)-1
    print(high)
    while low<=high:
        mid=(low+high)//2
        print(mid)
        print(card_list[mid])
        if card_list[mid]==card:
            print("{1} at postion {0}".format(mid+1,card))
            return
        elif card_list[mid] < card:
             low=mid+1
        else:
             high=mid-1
    #print("{0},{1},{2},{3} is not found".format("h",card,"gg","fff"))
    print("{0} is not found".format(card))
         
             
    return        

if __name__ == '__main__':
    heart_cards=[1,2,4,8,15,16,27,28,29,30,41,42,43]
    heart_eight=8
    binary_search(heart_cards,heart_eight)
