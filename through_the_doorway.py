dim_a = input()
dim_b = input()
dim_c = input()
dim_x = input()
dim_y = input()

def fit_door_width(dim):
    count = 0
    if dim_a <= dim:
        count += 1
    elif dim_b <= dim:
        count += 1
    elif dim_c <= dim:
        count += 1
    else:
        count = 0
    return count


def fit_door_height(dim):
    count = 0
    if dim_a <= dim:
        count += 1
    elif dim_b <= dim:
        count += 1
    elif dim_c <= dim:
        count += 1
    else:
        count = 0
    return count


if fit_door_height(dim_y) + fit_door_width(dim_x) >= 2:
    print("The box can be carried")
else:
    print("The box cannot be carried")
