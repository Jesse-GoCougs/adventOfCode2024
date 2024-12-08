def check_if_level_safe(level):
    is_decreasing = level[0] > level[1]
    n = len(level)-1

    if n < 2:
        return True
   
    for index in range(n):
        difference = abs(level[index] - level[index+1])
        if is_decreasing: #decreasing_level
            if level[index] <= level[index+1]: #rule_1
                return False
        else: #increasing_level
            if level[index] >= level[index+1]: #rule_1
                return False
        #rule 2: check if difference is in bounds 
        if difference < 1 or difference >3:
            return False    
    return True

def read_input(input_file_dir):
    result = []
    with open(input_file_dir, "r") as file:
        for line in file:
            row = list(map(int, line.split()))
            result.append(row)
    return result       

def unsafe_level_exception(level):
    if check_if_level_safe(level):
        return True 

    n = len(level)
    for index in range(n):
        # Create a new list with the ith element removed
        modified_level = level[:index] + level[index + 1 :]
        if check_if_level_safe(modified_level):
            return True 
    return False


if __name__ == "__main__":
    safeLevelCount = 0 
    result = read_input("data.txt")

    for level in result:
        if unsafe_level_exception(level):
            safeLevelCount +=1
    
    print("safe_level_count: ", safeLevelCount)