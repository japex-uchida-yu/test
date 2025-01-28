def add_numbers(a: int, b: int) -> int:
    """2つの数値を足し算する関数
    
    Args:
        a (int): 1つ目の数値
        b (int): 2つ目の数値
    
    Returns:
        int: 計算結果
    """
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    """2つの数値を引き算する関数
    
    Args:
        a (int): 1つ目の数値
        b (int): 2つ目の数値
    
    Returns:
        int: 計算結果
    """
    return a - b

def multiply_numbers(a: int, b: int) -> int:
    """2つの数値を掛け算する関数
    
    Args:
        a (int): 1つ目の数値
        b (int): 2つ目の数値
    
    Returns:
        int: 計算結果
    """
    return a * b

def divide_numbers(a: int, b: int) -> int:
    """2つの数値を割り算する関数
    
    Args:
        a (int): 1つ目の数値
        b (int): 2つ目の数値
    
    Returns:
        int: 計算結果
    """
    return a / b

def main():
    # テスト用の数値
    num1 = 10
    num2 = 5
    
    # 足し算のテスト
    result_add = add_numbers(num1, num2)
    print(f"足し算: {num1} + {num2} = {result_add}")
    
    # 引き算のテスト
    result_sub = subtract_numbers(num1, num2)
    print(f"引き算: {num1} - {num2} = {result_sub}")
    
    # 掛け算のテスト
    result_multiply = multiply_numbers(num1, num2)
    print(f"掛け算: {num1} × {num2} = {result_multiply}")

    # 割り算のテスト
    result_divide = divide_numbers(num1, num2)
    print(f"割り算: {num1} ÷ {num2} = {result_divide}")

if __name__ == "__main__":
    main()
