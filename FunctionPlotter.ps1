# To run the program use the following command:
# .\FunctionPlotter.ps1 run

# To test the program use the following command:
# .\FunctionPlotter.ps1 test

if ($args[0] -eq "run") {
    echo "Running the program..."
    python Main.py
} elseif ($args[0] -eq "test") {
    echo "Testing the program..."
    pytest Test.py
} else {
    echo "Invalid argument. Please use 'run' or 'test'."
}