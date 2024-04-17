
use rand::thread_rng;

const MAX_ELEMENT: i32 = 10_000;
const N: usize = 100;


fn main() {
    let arr = [(); N].map(|_| thread_rng().gen_range(0..MAX_ELEMENT));
    shell_sort(&mut arr);
    println!("{:?}", arr);
}


// Procedural
fn shell_sort(arr: &mut [i32]) {
    let mut gap = arr.len() / 2;
    while gap > 0 {
        for i in gap..arr.len() {
            let mut j = i;
            while j >= gap && arr[j - gap] > arr[j] {
                arr.swap(j - gap, j);
                j -= gap;
            }
        }
        gap /= 2;
    }

}

// More rusty
fn shell_sort2(arr: &mut [i32]) {
    let mut gap;
    while {
        gap = arr.len() / 2;
        gap > 0
    } {
        arr[gap..].iter_mut().for_each(|x| {
        })
    }
}


