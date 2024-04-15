def convert_unix_path(path: str) -> str:
    elements = path.split('/')
    final_path = []
    for element in elements:
        if element == '.':
            continue
        if len(element) > 1 and element[:2] == '..':
            for _ in range(len(element)-1):
                final_path.pop()
        else:
            final_path.append(element)
    result = f"{'/'.join(final_path)}"
    if len(result) == 0:
        return '/'
    return result

def convert_unix_path_fast(path: str) -> str:
    if not path:
        raise ValueError
    final_path = []
    idx = 0
    for char in path:
        if idx == 0:
            idx += 1
            continue
        if char != '/':
            idx += 1
            continue
        prev_idx = idx-1
        prev_char = path[prev_idx]
        while prev_char != '/':
            prev_idx -= 1
            prev_char = path[prev_idx]
        prev_string = path[prev_idx+1:idx]
        if prev_string == '.':
            continue
        if len(prev_string) > 1 and prev_string[:2] == '..':
            for _ in range(len(prev_string)-1):
                final_path.pop()
        else:
            final_path.append(prev_string)
        idx += 1
    result = f"/{'/'.join(final_path)}"
    return result or '/'











TEST_CASES = [
    ('/etc/foo/../bar/baz.txt', '/etc/bar/baz.txt'),
    ('/etc/foo/./bar/baz.txt', '/etc/foo/bar/baz.txt'),
    ('/etc/..', '/'),
    ('/', '/')
]



if __name__ == '__main__':
    for string, expected_result in TEST_CASES:
        result = convert_unix_path_fast(string)
        assert result == expected_result, result
    print('ok')
