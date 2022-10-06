def format_address(address_string):
    # Declare variables
    street_number = ""
    street_name = []

    # Separate the address string into parts
    full_address = address_string.split()

    # Traverse through the address parts
    for i, data in enumerate(full_address):
        # Determine if the address part is the
        # house number or part of the street name
        if i == 0:
            street_number = data
        else:
            street_name.append(data)

    # Does anything else need to be done
    # before returning the result?
    street_name = " ".join(street_name)

    # Return the formatted string
    return f"house number {street_number} on street named {street_name}"


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
