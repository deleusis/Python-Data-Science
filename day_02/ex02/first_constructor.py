import sys

class Research:
    def __init__(self, path_):
        self.path_ = path_
    
    def file_reader(self):
        with open(self.path_, 'r') as f: 
            return(f.read())

def check_args(path_):
    with open(path_, 'r') as f: 
        line = f.readlines() # file.readlines() cчитывает из файла все строки в список и возвращает его.
        # first_line = line[0].split(',')
        # print(first_line)
        # if len(first_line) != 2:
        #     raise Exception('Error in first line')
        # if first_line[0].isspace or first_line[1].isspace:
        #     raise Exception('Header error')
        if len(line) < 2 or (len(line[0].split(',')) != 2 or (line[0].split(',')[1] == '\n')):
            raise Exception('Argument error')
        # if line[0].split(',')[1].isspace or  line[0].split(',')[0].isspace:
        #     raise Exception('Header error')
        for i in range(1, len(line) -1):
            if line[i] != '0,1\n' and line[i]!= '1,0\n':
                raise Exception('Argument error')


if __name__ == '__main__':
    if len(sys.argv) != 2 or check_args(sys.argv[1]):
        raise Exception('Argument error')
    print(Research(sys.argv[1]).file_reader())
# import sys

# class Research:
#     def __init__(self, path):
#         self.path = path

#     def file_reader(self):
#         with open(self.path, 'r') as input_file:
#             lines = input_file.readlines()
        
#         # first_line = lines[0].split(',')
#         if len(lines) != 2 or len(lines) < 2:
#             raise Exception('Error in first string')
#         # rest_line = lines[1:]
#         # if len(rest_line) == 0:
#         #     raise Exception('There is no data')
#         for line in lines:
#             if line != '0,1' and line != '1,0':
#                 raise ValueError('Error in strings')
#         return lines


# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         print(Research(sys.argv[1]).file_reader())
        # print(research.file_reader())