import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> map = new HashMap<>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++){
            // x + nums[i] = target
            // target - nums[i] = x

            int x = target - nums[i];

            if(map.containsKey(x)){
                res = new int[]{map.get(x), i};
                break;
            }

            map.put(nums[i], i);
        }
        return res;
    }
}