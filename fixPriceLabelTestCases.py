from fixPriceLabel import fix_price_label

# Test01: When a price reduction is higher than the original, it should remove that reduction from the label
assert fix_price_label("Was £10, then £8, then £11, now £6") == "Was £11, now £6"

# Test02: When a price reduction is equal to a previous price, it should remove that reduction from the label
assert fix_price_label("Was £10, then £8, then £8, now £6") == "Was £10, then £8, now £6"

# Test03: When a price reduction is equal or lower that the now price, it should be removed from the label
assert fix_price_label("Was £10, then £6, then £4, now £8") == "Was £10, now £8"

# Test04: When a price reduction is equal or lower that the now price, it should be removed from the label
assert fix_price_label("Was £10, then £6, then £4, then £3, then £2, then £1, now £2") == "Was £10, then £6, then £4, then £3, now £2"

# Test05: When a price increase is in the label, it should be removed
assert fix_price_label("Was £40, then £50, then £40, then £30, then £15, then £10, now £5") == "Was £50, then £40, then £30, then £15, then £10, now £5"

# Test06: Original price format should be maintained in the fixed label
assert fix_price_label("Was £10.50, then £8.99, now £6.25") == "Was £10.50, then £8.99, now £6.25"
