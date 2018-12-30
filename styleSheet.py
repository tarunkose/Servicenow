import xlwt

def set_style(name, height, bold=False, center=True):
    style = xlwt.XFStyle()  # ?????

    font = xlwt.Font()  # ???????
    font.name = name  # 'Times New Roman'
    font.bold = False
    font.color_index = 0
    font.height = height

    # style.borders = borders
    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font

    style.width = 50 * 256
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_LEFT
    if center == True:
        style.alignment = alignment
    return style