thai_number = ("ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า")
unit = ("", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน")


def unit_process(val):
    length = len(val) > 1
    result = ''

    for index, current in enumerate(map(int, val)):
        if current:
            if index:
                result = unit[index] + result

            if length and current == 1 and index == 0:
                result += 'เอ็ด'
            elif index == 1 and current == 2:
                result = 'ยี่' + result
            elif index != 1 or current != 1:
                result = thai_number[current] + result

    return result


def thai_num2text(number):
    str_num = str(number)
    all_num = str_num.split('.')
    s_number = all_num[0][::-1]
    s1_number = all_num[1][::-1]
    n_list = [s_number[i:i + 6].rstrip("0") for i in range(0, len(s_number), 6)]
    n_list2 = [s1_number[i:i + 6].rstrip("0") for i in range(0, len(s1_number), 6)]
    result = unit_process(n_list.pop(0))
    result2 = unit_process(n_list2.pop(0))
    for i in n_list:
        result = unit_process(i) + 'ล้าน' + result
    final = '{}บาท'.format(result)
    if result2 != '':
        final = '{}{}สตางค์'.format(final, result2)
    else:
        final = '{}ถ้วน'.format(final)

    return final
