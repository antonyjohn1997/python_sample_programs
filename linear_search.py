def linear_search(card_list,card):
    for i,element in enumerate(card_list):
        if element==card:
            #print("{} is at position {}".format(i+1,card))
            print("{1} is at position {0}".format(i+1,card))

            return
    print("{0} was not found".format(card))
    return

if __name__ == '__main__':
    heart_cards=["h-1","h-2","h-3","h-4","h-5","h-6","h-7","h-8","h-9","h-10","h-J","h-Q","h-K","h-A"]
    heart_king="h-A"
    linear_search(heart_cards,heart_king)
