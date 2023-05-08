def findDifference(nums1, nums2):
    answer = [[], []]
    for i in nums1:
        if i not in nums2 and i not in answer[0]:
            answer[0].append(i)
    for j in nums2:
        if j not in nums1 and j not in answer[1]:
            answer[1].append(j)
    return answer