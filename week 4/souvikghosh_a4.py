############################################
# The pattern is as below:
# Display number starts from 10000
# Deducted number starts from 100
# In each iteration of the loop:
# - deducted number is subtracted from display number
# - deducted number is in turn subtracted by 1
# - if deducted number is less than 10 reset it to 100
# - continue the loop till display number is greater than or equal to 0
############################################
display_num = 10000
deduct_num = 100
while display_num >= 0:
    print(display_num)
    display_num -= deduct_num
    deduct_num -= 1
    if deduct_num < 10:
        deduct_num = 100
