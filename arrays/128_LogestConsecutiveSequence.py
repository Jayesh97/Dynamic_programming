nums = [100,1,23,2,3,4]
def longestseq(nums):
    longest_streak = 0
    num_set = set(nums)
    for i in num_set:
        if i-1 not in num_set:
            current_num = i
            current_streak = 1
            while current_num+1 in num_set:
                current_streak = current_streak+1
                current_num = current_num+1
            longest_streak = max(longest_streak,current_streak)
    return longest_streak

print(longestseq(nums))