#Paint_area_calculator
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round = math.ceil(num_cans)
    print(f"You'll need {round} cans of paint.")

test_h = float(input("Write the height: "))
test_w = float(input("Write the width: "))
coverage = 5

paint_calc(test_h,test_w,coverage)

