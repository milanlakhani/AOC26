def add_invalid_ids(range_string):
    ranges = [r.split("-") for r in range_string.split(",")]
    invalid_id_total = 0
    for r in ranges:
        for id in range(int(r[0]), int(r[1])+1):
            str_id = str(id)
            if len(str_id) % 2 == 1:
                continue
            if str_id[:len(str_id)//2] == str_id[len(str_id)//2:]:
                invalid_id_total += id
    return invalid_id_total

def add_invalid_ids_2(range_string):
    ranges = [r.split("-") for r in range_string.split(",")]
    invalid_id_total = 0
    for r in ranges:
        for id in range(int(r[0]), int(r[1])+1):
            str_id = str(id)
            invalid = False
            for l in range(len(str_id)//2):
                repeat_length = l+1
                if len(str_id) % repeat_length != 0:
                    continue
                target_value = str_id[:repeat_length]
                invalid = True
                for i in range(1,int(len(str_id)/repeat_length)):
                    if str_id[i*repeat_length:(i+1)*repeat_length] != target_value:
                        invalid = False
                        break
                if invalid:
                    break
            if invalid:
                invalid_id_total += id
    return invalid_id_total

range_string = "269351-363914,180-254,79-106,771-1061,4780775-4976839,7568-10237,33329-46781,127083410-127183480,19624-26384,9393862801-9393974421,2144-3002,922397-1093053,39-55,2173488366-2173540399,879765-909760,85099621-85259580,2-16,796214-878478,163241-234234,93853262-94049189,416472-519164,77197-98043,17-27,88534636-88694588,57-76,193139610-193243344,53458904-53583295,4674629752-4674660925,4423378-4482184,570401-735018,280-392,4545446473-4545461510,462-664,5092-7032,26156828-26366132,10296-12941,61640-74898,7171671518-7171766360,3433355031-3433496616"
print(add_invalid_ids_2(range_string))