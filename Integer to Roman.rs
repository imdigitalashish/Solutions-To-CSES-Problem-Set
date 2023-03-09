impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let sym_list = vec![
            ("I", 1),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("L", 50),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("D", 500),
            ("CM", 900),
            ("M", 1000),
        ];
        let mut res = String::new();
        for (sym, val) in sym_list.iter().rev() {
            if num / *val > 0 {
                let count = num / *val;
                res += &(*sym).repeat(count as usize);
                num %= *val;
            }
        }
        res
    }
}
