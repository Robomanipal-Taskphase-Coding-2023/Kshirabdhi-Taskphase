import re

def parse_encoded_string(encoded_string):
    pattern = r'(.+?)0+(.+?)0+(\d+)'
    match = re.match(pattern, encoded_string)

    if match:
        first_name, last_name, id = match.groups()
        result = {
            "first_name": first_name,
            "last_name": last_name,
            "id": id
        }
        return result
    else:
        return None
encoded_string = "prachi000aree0003455"
parsed_data = parse_encoded_string(encoded_string)

if parsed_data:
    print(parsed_data)
else:
    print("Invalid encoded string format.")

___________________________

