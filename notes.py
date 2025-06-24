def int_checked(f):
    assert int(f) == f
    return int(f)
print("Closest to a square (8/11):")
print(f"{int_checked(210/8 * 4)}:{int_checked(297/11 * 4)}") # "* 4" to round up to an integer to use in GIMP with selection aspect ratio
print("Less convenient fractions:")
def get_fraction(rows, cols):
    precision = 100000 # GIMP's precision: 6 digits
    frac = (210/cols)/(297/rows)
    return f"{int(frac * precision)}:{precision}"
def print_fraction(rows, cols):
    print(f"{rows=}, {cols=}, {get_fraction(rows, cols)}")
print_fraction(15, 8)
print_fraction(14, 8)
print_fraction(13, 8)
print_fraction(12, 8)
print_fraction(10, 8)
print_fraction(10, 10)
