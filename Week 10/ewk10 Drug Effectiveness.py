def compute_shelf_life(monthlyLoss, acceptablePotency) :
    month = 0
    done = False
    if 0 > monthlyLoss or 100 < monthlyLoss or 0 > acceptablePotency or 100 < acceptablePotency:
        return ("One of the values is out of range. Please enter numbers between the ranges of 0-100 for each paramater.")
    remaininguse = 100
    monthlyLoss = monthlyLoss / 100
    while not done:
        month = month + 1
        remaininguse = remaininguse - (monthlyLoss * remaininguse)
        if remaininguse < acceptablePotency:
            done = True
    return month - 1



print(compute_shelf_life(4.0, 50.0))
