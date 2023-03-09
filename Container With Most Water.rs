
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut res = 0;
        let (mut left, mut right) = (0, height.len() - 1);
        while left < right {
            let area = (right - left) * std::cmp::min(height[left] as usize, height[right] as usize);
            res = res.max(area);
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        res as i32
    }
}
