

int removeElement(int* nums, int numsSize, int val){
    int free_index = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            nums[free_index] = nums[i];
            free_index++;
        }
    }
    
    return free_index;
}