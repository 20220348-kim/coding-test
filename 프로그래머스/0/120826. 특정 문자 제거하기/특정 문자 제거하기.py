def solution(my_string, letter):
    # split() 괄호 추가 및 letter를 기준으로 쪼개기
    answer = my_string.split(letter)
    # 쪼갠 문자열들을 공백 없이 다시 합치기
    my_string = "".join(answer)
    return my_string