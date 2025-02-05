import argparse
import os
import warnings, sys

def calculate_equation(x1: float, x2: float) -> float:
    """
    Calculate the result of an equation using two input variables.
    Returns: (x1^2 + x2^2 + 2*x1*x2) / 2
    """
    result_1 = (x1**2 + x2**2 + 2*x1*x2) / 2
    result_2 = (x1**1 + x2**3 + 5*x1*x2) / 2
    return float(result_1), float(result_2)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Calculate equation with two variables')
    parser.add_argument('x1', type=float, help='First input variable')
    parser.add_argument('x2', type=float, help='Second input variable')
    parser.add_argument('--output', type=str, help='Output file path', default="output.txt")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Calculate and print result
    outputs = calculate_equation(args.x1, args.x2)

    # current file directory
    file_dir = os.path.dirname(os.path.realpath(__file__))

    with open(args.output, "w") as f:
        f.write(f"{outputs[0]},{outputs[1]}")
        
    # # throw a warning with the current working directory
    # warnings.warn(f"Output file saved at {args.output}", UserWarning)