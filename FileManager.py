
class FileManager:
    #return every pair of from node and to node as tuple and store in an array
    @staticmethod
    def readfile(file):
        result = []
        directory = file
        if directory != '':
            with open(directory, 'r') as file1:
                # ignore first 4 lines
                lines = file1.readlines()

                lines = [item.rstrip("\n") for item in lines]
                # replace tab with space
                lines = [item.replace("\t", " ") for item in lines]
                for line in lines:
                    # add as tuple into array
                    temp = line.split(" ")
                    result.append((temp[0], temp[1]))
            return result
        else:
            return ''






