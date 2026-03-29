def snake_to_camel(text: str) -> str:
    spilt_text = text.split("_")
    result = spilt_text[0]
    for word in spilt_text[1:]:
        first_letter = word[0].upper()
        rest_of_word = word[1:]
        result += first_letter + rest_of_word
    return result

print(snake_to_camel("a_b_c_d"))