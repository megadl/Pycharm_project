def intersection(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    minL = min(len(nums1), len(nums2))
    common1 = []
    pointer1 = pointer2 = 0
    while pointer1 < minL and pointer2 < minL :
        if nums1[pointer1] == nums2[pointer2]:
            common1.append(nums1[pointer1])
        elif nums1[pointer1] > nums2[pointer2]:
            pointer2 += 1
        elif nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1
    return common1


if __name__ == '__main__':
    nums1 = [1,2,2,3,4]
    nums2 = [2,2]
    print(intersection(nums1, nums2))