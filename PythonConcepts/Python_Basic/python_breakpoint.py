def calculate_sum(a, b):
    result = a + b
    breakpoint()  # Program will pause here
    """
    Execution stops at breakpoint().
        You’ll enter the interactive debugger (Pdb).
        You can type commands like:
        n → next line
        c → continue
        s → step into function
        p result → print variable
        q → quit debugger
    """
    return result

x = 10
y = 5
sum_val = calculate_sum(x, y)
print(f"The sum is: {sum_val}")