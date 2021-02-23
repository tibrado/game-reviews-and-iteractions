# Text file cleaner 
# Imports 
import csv
import string

class TextCleaner:
    def __init__(self, path):
        self.data = []
        try:
            self.file = open(path, 'r')
        except:
            print(f'Did not find file at path {path}')

    
    def level_1(self, strip, split = None):
        # rating, date, # comments, name
        row = [None, None, None, None]
        index = 0

        for line in self.file:
            line = f'{line.strip(strip)}'

            if line != '-':
                row[index] = line
                index += 1
            
            # Check if row data has been full collected 
            if (split in line) | (index > 3):
                # has max index been reached 
                if index <= 3: 
                    row[3] = row[2]
                    row[2] = 0
                self.data.append(row)

                # reset row and index
                row = [None, None, None, None]
                index = 0
        
        self.file.close()


    def save_csv(self, file, header = None):
        file = open(file, 'a+', newline = '')

        with file:
            write = csv.writer(file)

            # Write header if given 
            if header:
                write.writerow(header)
            write.writerows(self.data)
        
        file.close()
