def format_string(s, operations):
    def _uppercase(s):
        return s.upper()
    
    def _reverse(s):
        return s[::-1]
    
    def _capitalize(s):
        return s.title()
    
    operation_map = {
        'uppercase': _uppercase,
        'reverse': _reverse,
        'capitalize': _capitalize
    }
    
    for op in operations:
        if isinstance(op, str) and op in operation_map:
            s = operation_map[op](s)
        else:
            raise ValueError(f"Unsupported operation: {op}")
    
    return s

def main():
    s = input("s= ")
    operations_input = input("operations ( 'uppercase, reverse, capitalize' ): ")
    operations = [op.strip() for op in operations_input.split(',')]
    
    try:
        result = format_string(s, operations)
        print("Formatted string:", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
