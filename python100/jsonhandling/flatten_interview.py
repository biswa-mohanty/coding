def flatten(input, parent_key="", temp_output = []):
    #temp_output = []
    # your code here

    for key, value in input.items():
        if (type(value) == str):
            temp_dict = {"key": (parent_key + "." + key), "value": value}
            temp_output.append(temp_dict)
        elif type(value) == dict:
            key = parent_key + "." + key
            flatten(value, key, temp_output)
        elif type(value) == list:
            index = 0
            try:
                for key_temp, value_temp in value:
                    key = parent_key + "." + key_temp + "[" + str(index) + "]."
                    flatten(value_temp, key, temp_output)
                    index += 1
            except:
                for key_temp, value_temp in enumerate(value):
                    key = parent_key + ".[" + key_temp + "]"
                    temp_dict = {"key": key, "value": value_temp}
                    temp_output.append(temp_dict)
        else:
            pass
    print(temp_output)
    return temp_output

sample_input = {
    "a": "aa",
    "b": {
        "bb1": "d",
        "bb2": "d2"
    },
    "c": [
        {
            "cc1": "d"
        },
        {
            "cc1": "d2",
            "cc2": [
                {
                    "e": "f"
                }
            ]
        }
    ],
    "g": ["h", "i"]
}

flatten(sample_input)