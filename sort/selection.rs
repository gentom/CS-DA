fn selection_sort(array: &mut [i32]) {
 
    let mut min;
 
    for i in 0..array.len() {
 
        min = i;
 
        for j in (i+1)..array.len() {
 
            if array[j] < array[min] {
                min = j;
            }
        }
 
        let tmp = array[i];
        array[i] = array[min];
        array[min] = tmp;
    }
}


// TODO: add exchange counter
// TODO: add turnover counter
// TODO: add random num array generator
// TODO: add sorted array in ascending
// TODO: add sorted array in desending
fn sort<T: PartialOrd>(source: &mut [T]) {
    for i in 0..(source.len() - 1) {
        let mut k = i;
        for j in (i + 1)..source.len() {
            if source[j] < source[k] {
                k = j;
            }
        }
        if k != i {
            source.swap(i, k);
        }
    }
}
 
fn main() {
 
    let mut array = [ 9, 4, 8, 3, -5, 2, 1, 6 ];
    println!("The initial array is {:?}", array);
 
    selection_sort(&mut array);
    println!(" The sorted array is {:?}", array);
}