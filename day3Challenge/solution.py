import re

def read_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return lines 
        
#part 1 of challenge 
def sum_multiplication(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0 

    for line in memory:
        multiplications = re.findall(pattern, line)
        for x, y in multiplications:
            total += int(x) * int(y)
    return total


if __name__ == "__main__":
    testData = "}mul(620,236)where()*@}!&[mul(589,126)]&^]mul(260,42)when() when()$ ?{/^*mul(335,250)"
    memory = read_input("day3_data.txt")

    print(sum_multiplication(memory))