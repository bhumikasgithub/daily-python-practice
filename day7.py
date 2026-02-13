# Python program for converting number to words

def numtowords(n):
    
    ones = ["", "one ", "two ", "three ", "four ",
            "five ", "six ", "seven ", "eight ", "nine "]
    
    teens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
             "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    
    ntens = ["", "", "twenty ", "thirty ", "forty ",
             "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    
    result = ""   # IMPORTANT: initialize result
    
    if n == 0:
        return "zero"
    
    # Thousands
    if n >= 1000:
        result += ones[n // 1000] + "thousand "
        n = n % 1000
    
    # Hundreds
    if n >= 100:
        result += ones[n // 100] + "hundred "
        n = n % 100
    
    # Tens
    if n >= 20:
        result += ntens[n // 10]
        n = n % 10
    
    elif n >= 10:
        result += teens[n - 10]
        n = 0
    
    # Ones
    if n > 0:
        result += ones[n]
    
    return result.strip()


# Driver code
number = int(input("Enter a number: "))
print(numtowords(number))
