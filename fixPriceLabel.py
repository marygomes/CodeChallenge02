import re


def fix_price_label(label) -> str:
    price_list = [str(s) for s in re.findall(r'-?\d+\.?\d*', label)]
    final_price_list = []
    final_price_label = ''
    final_price_list.append(price_list[-1])
    i = len(price_list)-1
    while i > 0:
        if float(final_price_list[-1]) < float(price_list[i-1]):
            final_price_list.append(price_list[i-1])
        i -= 1
    final_price_list.reverse()
    for j in range(1, len(final_price_list)+1):
        final_price_label += ("{}{}".format('Was £' if j == 1 else ', then £'
                if j < len(final_price_list) else ', now £', final_price_list[j-1]))
    return final_price_label
