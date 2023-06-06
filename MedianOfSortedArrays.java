class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int n1p = 0;
        int n2p = 0;
        int total = (nums1.length + nums2.length);
        boolean isOdd = total % 2 == 1;

        int curr = Integer.MIN_VALUE;
        int next = Integer.MIN_VALUE + 1;

        while (n1p + n2p < total / 2 + 1) {

            curr = next;
            if (n1p == nums1.length) {
                next = nums2[n2p];
                n2p++;
            } else if (n2p == nums2.length) {
                next = nums1[n1p];
                n1p++;
            }else if (nums1[n1p] < nums2[n2p]) {
                next = nums1[n1p];
                n1p++;
            } else {
                next = nums2[n2p];
                n2p++;
            }
        }
        if (isOdd) {
            return next;
        } else {
            return  ((double) (curr + next) / 2);
        }
    }
}
