import json

unflat_json = {
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


def flatten_json(y):
    out = {}

    def flatten(x, name=''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Driver code
print(flatten_json(unflat_json))