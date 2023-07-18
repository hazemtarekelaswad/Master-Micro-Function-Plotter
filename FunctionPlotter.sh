# To run the program use the following command:
# ./FunctionPlotter.sh run

# To test the program use the following command:
# ./FunctionPlotter.sh test

if [ "$1" = "run" ]; then
    echo "Running the program..."
    python Main.py
elif [ "$1" = "test" ]; then
    echo "Testing the program..."
    pytest Test.py
else
    echo "Invalid argument. Please use 'run' or 'test'."
fi


