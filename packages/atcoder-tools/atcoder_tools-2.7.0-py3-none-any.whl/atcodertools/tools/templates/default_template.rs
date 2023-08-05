use io::*;
use std::*;

{% if mod %}
const MOD: i64 = {{ mod }};
{% endif %}
{% if yes_str %}
const YES: &'static str = "{{ yes_str }}";
{% endif %}
{% if no_str %}
const NO: &'static str = "{{ no_str }}";
{% endif %}
{% if prediction_success %}
fn solve({{ formal_arguments }}) {

}
{% endif %}

// Generated by {{ atcodertools.version }} {{ atcodertools.url }}  (tips: You use the default template now. You can remove this line by using your custom template)
fn main() {
    let con = read_string();
    let mut scanner = Scanner::new(&con);
    {% if prediction_success %}
    {{input_part}}
    // In order to avoid potential stack overflow, spawn a new thread.
    let stack_size = 104_857_600; // 100 MB
    let thd = std::thread::Builder::new().stack_size(stack_size);
    thd.spawn(move || solve({{ actual_arguments }})).unwrap().join().unwrap();
    {% else %}
    // Failed to predict input format
    {% endif %}
}

pub mod io {
    use std;
    use std::str::FromStr;

    pub struct Scanner<'a> {
        iter: std::str::SplitWhitespace<'a>,
    }

    impl<'a> Scanner<'a> {
        pub fn new(s: &'a str) -> Scanner<'a> {
            Scanner {
                iter: s.split_whitespace(),
            }
        }

        pub fn next<T: FromStr>(&mut self) -> T {
            let s = self.iter.next().unwrap();
            if let Ok(v) = s.parse::<T>() {
                v
            } else {
                panic!("Parse error")
            }
        }

        pub fn next_vec_len<T: FromStr>(&mut self) -> Vec<T> {
            let n: usize = self.next();
            self.next_vec(n)
        }

        pub fn next_vec<T: FromStr>(&mut self, n: usize) -> Vec<T> {
            (0..n).map(|_| self.next()).collect()
        }
    }

    pub fn read_string() -> String {
        use std::io::Read;

        let mut s = String::new();
        std::io::stdin().read_to_string(&mut s).unwrap();
        s
    }

    pub fn read_line() -> String {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_right().to_owned()
    }
}
