import argparse


def attr_flag(s):
    """
    Parse attributes parameters.
    """
    if s == "*":
        return s
    attr = s.split(',')
    assert len(attr) == len(set(attr))
    attributes = []
    for x in attr:
        if '.' not in x:
            attributes.append((x, 2))
        else:
            split = x.split('.')
            print(split)
            assert len(split) == 2 and len(split[0]) > 0
            assert split[1].isdigit() and int(split[1]) >= 2
            attributes.append((split[0], int(split[1])))
    return sorted(attributes, key=lambda x: (x[1], x[0]))


parser = argparse.ArgumentParser(description='Simple tutorial to understand arg types')

parser.add_argument("--attr", type=attr_flag, default="Gender,Daylight,CSK.3",
                    help="Attributes to classify")
parser.add_argument("--img_size", type=int, default=256,
                    help="Image sizes (images have to be squared)")

params = parser.parse_args()

#convert from argparse.Namespace to dict

dict_params = vars(params)
for k, v in dict_params.items():
    print(k, v)
