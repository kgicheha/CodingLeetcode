const containsDuplicate = (nums) => {
  // 1. create empty hashmap
  // 2. iterate through the nums array
  // 3. if the number has not been seen, store it in the has
  // 4. if it is already in the hash, return true
  let seen = {};
  let i = 0;
  while (i < nums.length) {
    console.log(nums[i]);
    if (nums[i] in seen) {
      return true;
    } else {
      seen[nums[i]] = 1;
    }
    i++;
  }
  return false;
};

containsDuplicate([1, 2, 3, 1]);
// containsDuplicate([1,2,3,4])
// containsDuplicate([1,1,1,3,3,4,3,2,4,2])
