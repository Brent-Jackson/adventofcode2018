
def differ_by_one_char(this, other):
    '''Return true if two same-length codes differ by only one character'''
    if len(this) != len(other):
        return False

    num_diffs = 0
    for i in range(len(this)):
        if this[i] != other[i]:
            num_diffs += 1
            if num_diffs >= 2:
                return False
    return True
    
def test_differ():
    assert(differ_by_one_char("aaaa","aaab"))
    assert(differ_by_one_char("aaaa","aaba"))
    assert(differ_by_one_char("aaaa","abaa"))
    assert(differ_by_one_char("aaaa","baaa"))
    assert(differ_by_one_char("aaaa","aaaa"))
    assert(not differ_by_one_char("aaaa","baab"))
    assert(not differ_by_one_char("aaaa","aabb"))
    assert(not differ_by_one_char("aaaa","aaaaa"))

def solve(codes):
    
    for i in range(len(codes)):
        this = codes[i]
        print("codes[{}]:{}".format(i,this))
        for other in codes[i+1:]:
            print("{} =?= {}".format(this,other))
            if differ_by_one_char(this,other):
                print("similarity found!\n\t{}\n\t{}".format(this,other))
                return get_common_letters(this,other)
    return ""

def get_common_letters(this, other):
    common = ""
    for i in range(len(this)):
        if this[i] == other[i]:
            common += this[i]
    print(common)
    return common


def test_solve():

    assert(solve([
        "abcd",
        "abbb",
        "bbba",
        "a"
    ]) == "")

    assert(solve([
        "abcd",
        "abbb",
        "bbba",
        "a",
        "bbaa"
    ]) == "bba")


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()


# test_differ()
# test_solve()

print("Answer:",solve(lines))

