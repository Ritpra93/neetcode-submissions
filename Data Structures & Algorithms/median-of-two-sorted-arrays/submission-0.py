class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) //2
            #fiure out median of smaller array
            j = half - i - 2
            #we know we can use that to figure out where to start the bigger array

            Aleft = A[i] if i >= 0 else float("-infinity")
            #float infinity comes before array
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            #partition is now good case
            if Aleft <= Bright and Bleft <= Aright:
                #odd case
                if total % 2:
                    return min(Aright, Bright)
                #even    
                return (max(Aleft, Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            


    
        