import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 NumPy array
    matrix = np.array(lst).reshape(3, 3)
    
    # Build and return the calculations dictionary
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),      # Mean of each column
            matrix.mean(axis=1).tolist(),      # Mean of each row
            matrix.mean().item()               # Mean of all elements
        ],
        'variance': [
            matrix.var(axis=0).tolist(),       # Variance of each column
            matrix.var(axis=1).tolist(),       # Variance of each row
            matrix.var().item()                # Variance of all elements
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),       # Std deviation of each column
            matrix.std(axis=1).tolist(),       # Std deviation of each row
            matrix.std().item()                # Std deviation of all elements
        ],
        'max': [
            matrix.max(axis=0).tolist(),       # Max of each column
            matrix.max(axis=1).tolist(),       # Max of each row
            matrix.max().item()                # Max of all elements
        ],
        'min': [
            matrix.min(axis=0).tolist(),       # Min of each column
            matrix.min(axis=1).tolist(),       # Min of each row
            matrix.min().item()                # Min of all elements
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),       # Sum of each column
            matrix.sum(axis=1).tolist(),       # Sum of each row
            matrix.sum().item()                # Sum of all elements
        ]
    }

    return calculations
