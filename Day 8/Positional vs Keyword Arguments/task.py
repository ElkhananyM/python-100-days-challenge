def calculate_love_score(m_name, f_name):
    full_name = m_name + f_name
    true = "true"
    t_score = 0
    love = "love"
    l_score = 0
    total_score = ""
    for letter in full_name:
        for m_char in true:
            if m_char == letter:
                t_score += 1
        for f_char in love:
            if f_char == letter:
                l_score += 1
    total_score = f"{t_score}{l_score}"
    print(t_score, l_score, full_name)
    print(total_score)


calculate_love_score("Angela", "Jack")
