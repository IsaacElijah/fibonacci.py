# Import the NumPy library
# NumPy is a powerful library for numerical computations in Python.
import numpy as np

# Create a NumPy array
# This is a 1D array with elements [1, 2, 3, 4, 5].
np_array = np.array([1, 2, 3, 4, 5])
print("NumPy array:", np_array)

# Perform basic operations with NumPy arrays
# Adding 2 to each element of the array
print("Array + 2:", np_array + 2)
# Multiplying each element of the array by 3
print("Array * 3:", np_array * 3)

# Create a 2D array
# This is a 2x3 array (2 rows and 3 columns).
np_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", np_2d_array)

# Display array properties
# Shape: Returns the dimensions of the array (rows, columns).
print("Shape:", np_2d_array.shape)
# Dimensions: Returns the number of dimensions (2 for a 2D array).
print("Dimensions:", np_2d_array.ndim)
# Size: Returns the total number of elements in the array.
print("Size:", np_2d_array.size)

# Perform array manipulation
# Transpose: Swaps rows and columns of the array.
print("Transpose:\n", np_2d_array.T)
# Flatten: Converts the 2D array into a 1D array.
print("Flattened array:", np_2d_array.flatten())

# Instructions for running this script:
# 1. Ensure Python is installed on your system. You can check by running `python --version` in the terminal.
# 2. Install the NumPy library if not already installed. Use the command `pip install numpy`.
# 3. Save this script as `import.py` in your desired directory.
# 4. Open a terminal or command prompt, navigate to the directory containing this script, and run it using:
#    python import.py
#
# Expected Output:
# The script will display the NumPy array, results of basic operations, properties of the 2D array,
# and the results of array manipulations like transpose and flatten.