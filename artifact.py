import helper

class Artifact():
    def __init__(self, stats):
        self.scale_atk = 0
        self.flat_atk = 0
        self.crit_rate = 0
        self.crit_damage = 0

        for line in stats:
            if 'by' in line:
                continue
            if 'ATK' in line:
                stat_value = helper.get_stat_value(line, 'ATK')

                if (stat_value.endswith('%')):
                    self.scale_atk = float(stat_value.removesuffix('%'))
                else:
                    self.flat_atk = int(stat_value)

            if 'CRIT Rate' in line:
                stat_value = helper.get_stat_value(line, 'CRIT Rate')
                self.crit_rate = float(stat_value.removesuffix('%'))

            if 'CRIT DMG' in line:
                stat_value = helper.get_stat_value(line, 'CRIT DMG')
                self.crit_damage = float(stat_value.removesuffix('%'))

    def show_stats(self):
        print(f'Flat ATK {self.flat_atk}')
        print(f'Scale ATK {self.scale_atk}%')
        print(f'CRIT Rate {self.crit_rate}%')
        print(f'CRIT DMG {self.crit_damage}%')