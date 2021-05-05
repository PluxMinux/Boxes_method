def encrypt(key,msg): 
    msg_split = msg.split()
    msg_join = ''.join(msg_split)
    msg_join_list = list(msg_join)
    row1 = len(msg_join) / len(key)
    place_number = -len(msg_join)

    point_number = [int(row1)+.1 ,int(row1)+.2,int(row1)+.3,int(row1)+.4,
                    int(row1)+.5,int(row1)+.6,int(row1)+.7,
                    int(row1)+.8,int(row1)+.9]

    #Identify if the message are matrix.
    #if not add ' ' or space to be matrix.
    #key: space             | key: red
    #msg: tommorow are quiz | msg: kill the bug
    #Output: tommo          | Output: kil
    #        rowar          |         lth
    #        equiz          |         ebu
    #                       |         g**   <--- The * represent space or ' '
    if (round(row1,1) in point_number) == True:
        plus_one = int(row1) + 1
        space_add = len(key) * plus_one
        space_add -= len(msg_join)
        for i in range(space_add):
            msg_join_list.append(" ")
        row1 += 1

    encrypt_list = []
    temp_list = []
    #Encryption process.
    loop1 = 0
    while(loop1 <= len(key)):
        loop = 0
        while (loop < (int(row1))):
            first_column = msg_join_list[place_number]
            temp_list.append(first_column)
            loop += 1
            place_number += len(key)
            end = (int(row1)) - 1
            if loop == end:
                encrypt_list.append(temp_list)
        temp_list = []
        place_number = -len(msg_join_list) + loop1
        loop1 += 1
    encrypt_list.pop(0)
    keylist = list(key)
    mydict = {}
    for i in range(len(key)):
        mydict[keylist[i]] = encrypt_list[i]
    sort = [value for (key, value) in sorted(mydict.items())]
    #Display encrypted message.
    mylist_inside_index = []
    i = 0
    while True:
        display_by_index = sort[i]
        join_index_list = ''.join(display_by_index)
        mylist_inside_index.append(join_index_list)
        i += 1
        if i >= len(sort):
            break
    display_encrypt = ' '.join(mylist_inside_index)
    return display_encrypt


def decrypt(key,msg):
    msg_split = msg.split()
    msg_join = ''.join(msg_split)
    row = len(msg_join) / len(key)
    row_addone = [row]
    decrypted_list = []

    point_number = [int(row)+.1 ,int(row)+.2,int(row)+.3,int(row)+.4,
                        int(row)+.5,int(row)+.6,int(row)+.7,
                        int(row)+.8,int(row)+.9]
    #Identify if the row are rational number: len(key) / len(msg)
    if (round(row,1) in point_number) == True:
        for i in range(len(msg_split)):
            if int(row) == len(msg_split[i]):
                index_e_msg_split = msg_split[i]
                msg_split.insert(i,index_e_msg_split+"x")
                msg_split.pop(i+1)
            if (len(msg_split)-1) == i:
                row_addone.insert(0,(row_addone[0]+1))
                row_addone.pop(1)
    #List of list.
    for i in range(0,len(key)):
        d_list_split_index = msg_split[i].split()
        d_list_join_index = ' '.join(d_list_split_index)
        d_list_index_list = list(d_list_join_index)
        decrypted_list.append(d_list_index_list)
    #Decryption process.
    mydict = {}
    list_key = list(key)
    sorted_key = sorted(key)
    for i in range(len(key)):
        insert_dict = sorted_key.index(list_key[i])
        mydict[list_key[i]] = decrypted_list[insert_dict]
    mydict_to_list = list(mydict.values())

    temp_list = []
    row = len(msg_join) / len(key)
    for i in range(int(row_addone[0])):
        for j in range(len(key)):
            temp_list.append(mydict_to_list[j][i])
    if len(temp_list) != len(msg_join):
        for i in range(len(temp_list)-len(msg_join)):
            temp_list.pop(-1)
    display_decrypt = ''.join(temp_list)
    return display_decrypt
    

