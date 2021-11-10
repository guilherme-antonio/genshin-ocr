import helper

class Stats():
    def __init__(self, base_stats):
        if (base_stats is None):
            return

        for line in base_stats:
            if 'ATK' in line:
                stat_value = helper.get_stat_value(line, 'ATK')
                self.set_atack(stat_value)
            if 'CRIT Rate' in line:
                stat_value = helper.get_stat_value(line, 'CRIT Rate')
                self.crit_rate = helper.get_percent_value(stat_value)

            if 'CRIT DMG' in line:
                stat_value = helper.get_stat_value(line, 'CRIT DMG')
                self.crit_damage = helper.get_percent_value(stat_value)

    def set_atack(self, stat_value):
        splited_atk = stat_value.split('+')

        base_atack = helper.format_int(splited_atk[0])
        bonus_atack = helper.format_int(splited_atk[1].rsplit(' ')[0])

        self.base_atk = base_atack
        self.total_atk = bonus_atack + base_atack

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
