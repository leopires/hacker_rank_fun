from array_manipulation import array_manipulation_bf, array_manipulation, read_input_test_case

if __name__ == '__main__':
    input = read_input_test_case(file_path='array_manipulation_test_case_07.txt')
    print(f"Array Size: {input['n']}; Total Queries: {len(input['queries'])}")
    result = array_manipulation(input['n'], input['queries'])
    print(f"Result: {result}. Expected: 2497169732")
