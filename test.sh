#!/bin/bash
#
# Feedback Test Runner
# The following shell script is designed to test Feedback for both Python2
# and Python3. 

# Local Python path
PYTHON_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Dummy script
DUMMY_SCRIPT="/tmp/feedback_test.py"

do_sed_string() {
	
	# Retrieve 'input string' argument
    INPUT_STRING="$1"

    # Process SED metacharacters
    SED_META1="${INPUT_STRING//\//\\/}"
    SED_META2="${SED_META1//\^/\\^}"
    SED_META3="${SED_META2//\./\\.}"
    SED_META4="${SED_META3//\*/\\*}"
    SED_META5="${SED_META4//\$/\\$}"
    SED_META6="${SED_META5//\+/\\+}"
    SED_META7="${SED_META6//\[/\\[}"
    SED_META8="${SED_META7//\]/\\]}"
    SED_META9="${SED_META8//\</\\<}"
    SED_META10="${SED_META9//\>/\\>}"
    SED_META11="${SED_META10//\@/\\@}"

    # Define SED friendly string
    SED_STRING="$SED_META11"

    # Echo SED friendly string
    echo "$SED_STRING"
	
}

do_rm() {
    FILE=$1
    echo -e "Removing file: $FILE"
    rm -f $FILE
}

do_update_python_path() {
    
    # Target file / Python path
    TARGET_FILE=$1
    PYTHON_PATH=$2
    
    # Update the Python path
    sed -i "s/{PYTHON_PATH}/$(do_sed_string "$PYTHON_PATH")/g" $TARGET_FILE
}

do_setup() {
    TEST_SCRIPT="$1"
    
    # Create the test script and update the Python path
    cp $TEST_SCRIPT $DUMMY_SCRIPT && chmod +x $TEST_SCRIPT
    do_update_python_path "$DUMMY_SCRIPT" "$PYTHON_PATH"
    echo "Creating dummy test script: $DUMMY_SCRIPT"
}

do_tests() {
    $1 $DUMMY_SCRIPT
}

do_cleanup() {
    
    # Remove dummy files
    echo -e "Removing dummy test files..."
    do_rm $DUMMY_SCRIPT
}

# Run Python2 tests
do_py2() {
    echo -e "---------------------------------------------------------------"
    echo -e "Running Python2 tests..."
    echo -e "---------------------------------------------------------------"
    do_setup "tests/feedback.py2.py"
    do_tests "/usr/bin/python"
    do_cleanup
    echo -e "---------------------------------------------------------------"
    echo -e "Python2 tests complete!"
    echo -e "---------------------------------------------------------------"
}

# Run Python3 tests
do_py3() {
    echo -e "Running Python3 tests..."
    echo -e "---------------------------------------------------------------"
    do_setup "tests/feedback.py3.py"
    do_tests "/usr/bin/python3"
    do_cleanup
    echo -e "---------------------------------------------------------------"
    echo -e "Python3 tests complete!"
    echo -e "---------------------------------------------------------------"
}

do_py2
do_py3
exit 0