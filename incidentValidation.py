import xlwt


def incident_priority_validation(priority_num):
    if priority_num == '1' or priority_num == '2':
        p_style = xlwt.easyxf('font: color-index  red', num_format_str='#,##0.00')
        return p_style

    if priority_num == 3:
        p_style = xlwt.easyxf('font: color-index  black', num_format_str='#,##0.00')
        return p_style

