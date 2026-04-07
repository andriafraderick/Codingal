function palindrome(myString) {
    // in case if any special characters or spaces are given in input that has to be removed.
    var input = myString.replace(/[^A-Z0-9]/ig, "").toLowerCase();

    // to check palindrome or not the string needs to be reversed so we are reversing it by splitting and joining it
    var reversedInput = input.split('').reverse().join('');

    // checking for palindrome
    if (input === reversedInput) {
        document.write("<div>" + myString + " is a palindrome <div>");
    } else {
        document.write("<div>" + myString + " is not a palindrome <div>");
    }
}

// invoking function
palindrome("madam")
