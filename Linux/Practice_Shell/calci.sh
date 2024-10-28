#!/bin/bash


echo "Enter first number: "
read x
echo "Enter second number: "
read y

echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "Enter your choice: "
read choice

if [ $choice -eq 1 ]; then
    z=$((x+y))
    echo "Sum: $z"
elif [ $choice -eq 2 ]; then
    z=$((x-y))
    echo "Difference: $z"
elif [ $choice -eq 3 ]; then
    z=$((x*y))
    echo "Product: $z"
elif [ $choice -eq 4 ]; then
    z=$((x/y))
    echo "Quotient: $z"
else
    echo "Invalid choice."
fi

# Output
# Enter first number:
# 10
# Enter second number:
# 20
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Enter your choice:
# 1
# Sum: 3