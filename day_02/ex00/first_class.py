class Must_read:
    with open('data.csv', 'r') as f: # open(path_to_file, mode)
        print(f.read())

if __name__ == '__main__':
    Must_read()