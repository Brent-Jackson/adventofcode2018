def solve(lines):

    occurances_to_track = [2,3]




    total_occurances_counts = {}
    for i in occurances_to_track:
        total_occurances_counts[i] = 0




    for code in lines:
        


        seen_occurances = {}
        for i in occurances_to_track:
            seen_occurances[i] = 0

        chars = {}
        print("code:",code)
        for ch in code.strip():
            if ch not in chars:
                chars[ch] = 1
            else:
                chars[ch] += 1
                occurances = chars[ch]
                if occurances in occurances_to_track:
                    seen_occurances[occurances] += 1
                    idx = occurances_to_track.index(occurances)
                    if idx - 1 >= 0:
                        seen_occurances[occurances_to_track[idx - 1]] -= 1
                # there should actually be an else clause here. If we were tracking the 2x and 4x occurances instead of 2 and 3, the 2 count wouldn't be properly decremented since the new count upon increasing to 3 is not being tracked.
                
            print("chars["+str(ch)+"]:"+str(chars[ch]))                        
        print("seen_occurances:",seen_occurances)


        for i in occurances_to_track:
            if seen_occurances[i] >= 1:
                total_occurances_counts[i] += 1
    print("total_occurances:",total_occurances_counts)

    running_product = 1
    for j in total_occurances_counts:
        running_product *= total_occurances_counts[j]
    print("checksum:",running_product)
    return running_product


def test():
    lines = [
        "aabbcc",
        "abbbc",
        "aaabbbccc",
        "abc",
        "ababa"
    ]
    solve(lines)

fname = "input.txt"

with open(fname) as f:
    lines = f.readlines()

# test()
solve(lines)




        



