pub fn reverse(input: &str) -> String {
    let original = input;
    let reversed: String = original.chars().rev().collect();
    // Correctly keeps the accent on the 'a'
    // little advanced for me this days
    // let reversed: String = complex_string.graphemes(true).rev().collect()
    reversed
}
