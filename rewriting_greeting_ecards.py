# -*- coding: utf-8 -*-
import re


def replace(S, dict):
    # result indicates the new string after replacement and will return at the end
    result = ""

    # using three pointers to represent different positions
    # left: the leftmost position when checking the undone part of old S
    # right: the rightmost position when checking the undone part of old S
    # cur: the current position when checking the undone part of old S
    left = 0
    right = 0
    cur = 0

    # using a flag hasMatch to indicate if the old substring matches
    hasMatch = True
    # while current point is in the boundary of the length of S, do
    while cur < len(S):
        cur_char = S[cur]
        # check if the current char is in the dictionary
        if cur_char in dict:
            # if in the dictionary, let the right pointer be the current pointer, namely, the first matching position of the substring
            right = cur
            # check each pair in the entry of dict[cur_char]
            for each_pair in dict[cur_char]:
                # compare each char of the old substring one by one to check if matches
                for j in range(len(each_pair[0])):
                    # if not match, reset the flag hasMatch and break
                    if S[right] != each_pair[0][j]:
                        hasMatch = False
                        break
                    # if match, move the right pointer forward by one position
                    right += 1
                # if match
                if hasMatch:
                    # add the previous part of the original string S and new substring to result
                    result += S[left:cur] + each_pair[1]
                    # move the current pointer to the right position
                    cur = right
                    # move the left pointer to the current position
                    left = cur
                    break
            # if not match
            if not hasMatch:
                # reset the hasMatch flag and move the current pointer forward by one position
                hasMatch = True
                cur += 1
        else:
            # the current char is not in the dictionary, then we should move the current pointer forward by one position
            cur += 1

    # check if the left pointer is less than the length of S
    # if so, means the last part of old S hasn't added to the result, so we need to add the last part to the result
    if left < len(S):
        result += S[left:]

    return result


if __name__ == "__main__":
    # Read the filenames of the user inputs
    print("Input:")
    filename_S = input("\tPlease enter the file name of S: ")
    filename_LS = input("\tPlease enter the file name of LS: ")
    LS = []
    try:
        with open(filename_LS, "r") as f_LS:
            # Read LS file line by line
            # Convert the string LS to list LS
            for each_line in f_LS:
                sublist = []
                for each in each_line.split(","):
                    each = re.sub(r'{|}|\"|”|“', '', each).strip()
                    if len(sublist) < 2:
                        sublist.append(each)
                    else:
                        LS.append(sublist)
                        sublist = []
                        sublist.append(each)
                LS.append(sublist)

            # using a dictionary/hashmap to restore the LS list
            # key: the first letter of the old substring of each pair in LS
            # value: a list consists of the relative pair in LS
            dict = {}
            for each in LS:
                # if there is no entry of the first letter in the dictionary, create a new list, and add the pair to the list
                if each[0][0] not in dict:
                    dict[each[0][0]] = [each]
                else:  # if there already exists an entry, append the new pair to the existing list
                    dict[each[0][0]].append(each)

        with open(filename_S, "r") as f_S:
            old_S = ""
            new_S = ""
            # Read S file line by line
            for each_line in f_S:
                # call function replace() to get the new S
                new_S += replace(each_line, dict)
                # get the old S for final display
                old_S += each_line

            # print the result to screen
            print("\nOutput:")
            print("\tThe old S: " + old_S)
            print("\tThe new S: " + new_S)

    # if there is no such file or the file cannot be opened, an error is raised
    except Exception as reason:
        print(reason)
