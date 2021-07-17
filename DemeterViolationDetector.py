from pathlib import Path

def search_line(line):
    parentheses, brackets=0,0
    dots=[0]
    for char in line:
        if char=='[':
            dots.append(0)
            brackets+=1
        elif char==']':
            dots.pop()
            brackets-=1
        elif char=='(':
            dots.append(0)
            parentheses+=1
        elif char==')':
            dots.pop()
            parentheses-=1
        elif char in ',+-/*?:><=!&^|':
            dots[-1]=0
        elif char=='.':
            dots[-1]+=1
            if dots[-1]>1:
                return True
    return False

def is_line_bad(line):
    return not line.startswith('using') and not line.startswith('namespace') and search_line(line)

def search_lines(lines):
    return (i for i, line in enumerate(lines) if is_line_bad(line.strip()))

def get_paths(base, suffix):
    return (str(path) for path in Path(base).rglob('*.'+suffix))

def get_file(path):
    with open(path) as f:
        return [line for line in f]

def result(base, suffix):
    for path in get_paths(base, suffix):
        lines=get_file(path)
        lines[0]=''
        errors=list(search_lines(lines))
        if len(errors)>0:
            print(path, len(errors), 'errors occured:')
            for i in errors:
                print(i+1, ':', lines[i].strip())
            print('-'*60)
            input()

result(input('Enter searched directory: '), input('Enter searched suffix: '))
