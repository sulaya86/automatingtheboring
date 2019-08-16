    """
    This script is the implementation of the module https://pypi.org/project/filesplit/
    to split files into multiple chunks in a windows local machine.
    """
    
    def split_big_file(filepath, split_size, output_dir):
    """
    This function split files of any size into
    multiple chunks, the split is based on the
    new line character in the file. The file split
    is numbered from 1 to n as follows
    filename]_1.ext, [filename]_2.ext, …., [filename]_n.ext
    """
    
    file_to_split = FileSplit(file=filepath, splitsize=split_size, output_dir=output_dir)
    file_to_split.split(include_header=True)

if __name__ == "__main__":

    FILEPATH_TO_SPLIT = "C:\\YourPath\\yourfile.ext"
    SPLIT_SIZE = 500000000
    OUTPUT_DIR = "C:\\YourPath\\Desktop\\splitted\\"

    #“splitsize” should be given in byte and output directory is optional(default current)
    split_big_file(FILEPATH_TO_SPLIT, SPLIT_SIZE, OUTPUT_DIR)
    
