import re

def sum_multiplication(buffer):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = 0

    multiplications = re.findall(pattern, buffer)
    for x, y in multiplications:
        print(f"Processing: mul({x}, {y})")
        total += int(x) * int(y)
    return total

def process_file(input_file):
    with open(input_file) as file:
        line = file.read().strip()
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line)
    print(matches)
    enabled = True
    ans = 0

    for match in matches:
        if match[2] == "" and enabled:
            ans += int(match[0]) * int(match[1])
        else:
            if match[2] == "do()":
                enabled = True
            else:
                 enabled = False
    return ans



if __name__ == "__main__":
    input_file = "day3_data.txt"
    print("Total sum of enabled multiplications:", process_file(input_file))