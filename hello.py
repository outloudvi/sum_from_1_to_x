# coding: utf-8

import locale

LANGLIB = {
    'zh_CN': {
        "You need to input an integer": u'您需要输入一个整数',
        "You need to input an integer larger than zero": u'您需要输入一个正数',
        "Input the number: ": u'输入数字：',
        "Failed to write to stdout": u'写入到 stderr 失败'
    }
}

LANGLIB['zh_HK'] = LANGLIB['zh_CN']

LANG = locale.getdefaultlocale()[0]


def _(string, lang=LANG):  # i18n
    if lang == 'en_US' or lang == 'en_UK':
        return string
    else:
        return LANGLIB[lang][string]


def sum_from_one_to_x(sum_all):
    __doc__ = """                                                                          
    Fuck it.
    """                                                                                    # Easy-to-read doc
    if type(sum_all) != type(1):  # Type check
        raise TypeError(_('You need to input an integer'))
    if sum_all <= 0:  # Number check
        raise NotImplementedError(
            _("You need to input an integer larger than zero"))
    return int(sum_all * (sum_all + 1) / 2)  # Algorithm


def print_sum_from_one_to_x(sum_all):  # Packed function with print()
    try:
        print(sum_from_one_to_x(sum_all))
    except IOError:  # stdout check
        from sys import stderr
        stderr.write(_("Failed to write to stdout"))


if __name__ == "__main__":
    print_sum_from_one_to_x(int(input(_('Input the number: '))))
