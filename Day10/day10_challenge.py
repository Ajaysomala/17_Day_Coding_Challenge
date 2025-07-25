# DAY 10 Challenge 

## --------- lambda shortener app ----------- ##
# >>>> Where it converts lambda function to list comprehension <<<<

def lambda_shortener(code_str):
    if "map" in code_str:
        # Example: "map(lambda x: x + 1, nums)"
        expr = code_str.split("lambda")[1]
        body, iterable = expr.split(":")[1].split(",", 1)
        var = expr.split(":")[0].strip().split()[0]
        iterable = iterable.strip(" )\n")
        return f"[{body.strip()} for {var} in {iterable}]"
    
    elif "filter" in code_str:
        # Example: "filter(lambda x: x % 2 == 0, nums)"
        expr = code_str.split("lambda")[1]
        condition, iterable = expr.split(":")[1].split(",", 1)
        var = expr.split(":")[0].strip().split()[0]
        iterable = iterable.strip(" )\n")
        return f"[{var} for {var} in {iterable} if {condition.strip()}]"

    else:
        return "Only supports map() and filter() for now!"

# 🔍 Try:
print(lambda_shortener("map(lambda x: x * 2, nums)"))
print(lambda_shortener("filter(lambda x: x > 10, my_list)"))
print(lambda_shortener("reduce(lambda x, y: x + y, my_list)"))