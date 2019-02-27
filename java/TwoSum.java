package leetcode;

import java.util.HashMap;

/**
 * Created by huxiaoman on 2019/2/27 3:01 PM.
 * E-mail: charlotte77_hu@sina.com
 */
public class TwoSum {

    /**
     * time : O(n)
     * space : O(n)
     * @params: nums
     * @params: target
     * @return
     */

    public int[] twoSum(int[] nums, int target){
        int[] result = new int[2];
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(target-nums[i])){
                result[0] = map.get(target-nums[i]);
                result[1] = i;
                break;
            }
            map.put(nums[i],i);
        }
        return result;

    }

}

    public static void main(String[] args){
        TwoSum([2,7,11,15],9])
    }