import java.util.*;
class Duplicate {


    static int j=0;


       public static int[] containsDuplicate(int[] nums) {
        int len=nums.length;
        result=new int[len];
        Arrays.sort(nums);
        for(int i=0;i<len-1;i++){
            if(nums[i]!=nums[i+1])
              result[j++]=nums[i];
        }
        return result;
    }

static int result[];

    public static void main(String[] args) {
        int arr[]={0,1,1,1,1,2,5,6,2,2,2,2,7,7,7,8,5,8,5,8,5,9,6,9,6};
        containsDuplicate(arr);

        for(int i=0;i<result.length;i++){
            System.out.print(result[i]);
        }

    }

}

