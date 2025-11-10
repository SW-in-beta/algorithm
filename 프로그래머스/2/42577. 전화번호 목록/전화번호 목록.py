def solution(phone_book):
    s = '9' * 21
    for p in sorted(phone_book):
        if len(p) <= len(s) or not p.startswith(s):
            s = p
            continue
        return False
    return True