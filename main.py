# Nathaniel Vincent
# nav0135@arastudent.ac.nz

def load_sales(filename: str) -> list: # It should honestly probably be a pathlib object but eh
    with open(filename, 'r') as file:
        for index, line in enumerate(file.read()):
            if index == 0:
                



if __name__ == '__main__':
    load_sales('./car_sales.csv')