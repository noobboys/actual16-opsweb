


def fmt_db_data(data):
    fields, values = [], []
    for k, v in data.items():
        fields.append(k)
        if k == 'password':
            values.append("'%s'" % encryption(v) )
        else:
            values.append("'%s'" % v)

    format_fields = ', '.join(fields)
    format_values = ', '.join(values)
    return format_fields, format_values


def fmt_update_data(data):
    values = []
    for k, v in data.items():
        values.append("%s='%s'" % (k, v))
    return ', '.join(values)

