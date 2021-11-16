def solve(s:str):
    string = s.split(' ')
    return ' '.join((word.capitalize() for word in string))
# string.title() won't work because we only want the first litter to be capital
# with title(), somthing like 20g will be 20G


if __name__ == '__main__':
    solve(input())
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = solve(s)

    # fptr.write(result + '\n')


