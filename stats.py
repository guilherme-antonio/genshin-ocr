import helper

class Stats():
    def __init__(self, base_stats):
        if (base_stats is None):
            return

        for line in base_stats:
            if 'ATK' in line:
                stat_value = helper.get_stat_value(line, 'ATK')

                splited_atk = stat_value.split('+')

                self.base_atk = int(splited_atk[0].strip())
                self.total_atk = int(splited_atk[1].rsplit(' ')[0].strip()) + self.base_atk

            if 'CRIT Rate' in line:
                stat_value = helper.get_stat_value(line, 'CRIT Rate')
                self.crit_rate = float(stat_value.removesuffix('%'))

            if 'CRIT DMG' in line:
                stat_value = helper.get_stat_value(line, 'CRIT DMG')
                self.crit_damage = float(stat_value.removesuffix('%'))

    def show_stats(self):
        print(f'Base ATK {self.base_atk}')
        print(f'Total ATK {self.total_atk}')
        print(f'CRIT Rate {self.crit_rate}%')
        print(f'CRIT DMG {self.crit_damage}%')
        print(f'Base DPS {self.get_base_damage_per_second()}')

    def get_base_damage_per_second(self):
        decimal_crit_rate = self.crit_rate / 100
        decimal_crit_damage = self.crit_damage / 100
        dps = ((1 - decimal_crit_rate) * self.total_atk) + (decimal_crit_rate * (self.total_atk * (1 + decimal_crit_damage)))
        
        return dps
