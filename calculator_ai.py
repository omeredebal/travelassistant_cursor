class Calculator:
    def __init__(self):
        self.operations = {
            '1': ('Addition', lambda x, y: x + y),
            '2': ('Subtraction', lambda x, y: x - y),
            '3': ('Multiplication', lambda x, y: x * y),
            '4': ('Division', lambda x, y: x / y if y != 0 else "Error: Division by zero!")
        }

    def display_menu(self):
        print("Simple Calculator")
        for key, (operation, _) in self.operations.items():
            print(f"{key}. {operation}")

    def get_numbers(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2

    def calculate(self):
        while True:
            try:
                self.display_menu()
                choice = input("Select operation (1/2/3/4): ")
                
                if choice not in self.operations:
                    print("Invalid choice! Please select 1, 2, 3 or 4.")
                    continue
                
                num1, num2 = self.get_numbers()
                operation_name, operation = self.operations[choice]
                result = operation(num1, num2)
                
                print(f"Result: {result}")
                    
                continue_calc = input("Do you want to perform another calculation? (y/n): ")
                if continue_calc.lower() != 'y':
                    break
                    
            except ValueError:
                print("Error: Please enter a valid number!")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculate()
