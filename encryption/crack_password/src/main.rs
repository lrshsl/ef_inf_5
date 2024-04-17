const CHARS: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

// fn crack_rec(choices: &[u8], prefix: &[u8], n: int) -> [u8; 3] {
//     if n == 0 {
//         return vec![prefix];
//     }
//     'a: {
//         for choice in choices {
//             break 'a 1;
//     }}
// }

fn crack_passwd<F, const N: usize>(correction_fn: F) -> Option<[u8; N]>
where
    F: Fn(&[u8; N]) -> bool,
{
    let mut proposal = [0u8; N];
    for pos in 0..proposal.len() {
        for &c in CHARS.as_bytes() {
            for i in 0..proposal.len() {
                for &ch in CHARS.as_bytes() {
                    proposal[i] = ch;
                    std::thread::sleep(std::time::Duration::from_millis(100));
                    println!("{:?}", proposal);
                    if correction_fn(&proposal) {
                        return Some(proposal);
                    }
                }
            }
            proposal[pos] = c;
        }
    }
    None
}

fn main() {
    let correct_passwd = "as00".as_bytes();
    let passwd = crack_passwd(|&p: &[u8; 3]| p == *correct_passwd);
    assert_eq!(correct_passwd, passwd.unwrap());
}
