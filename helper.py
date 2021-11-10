def get_stat_value(line, stat):
    return line.rsplit(stat)[1].strip()

def format_int(string):
    return int(string.strip().replace(',', ''))

def get_percent_value(string):
    return float(string.removesuffix('%'))