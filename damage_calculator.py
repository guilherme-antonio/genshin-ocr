class DamageCalculatorArtifactInput():
    def __init__(self, artifact, is_current):
        self.artifact = artifact
        self.is_current = is_current

class DamageCalculator():
    def __init__(self, stats, first_artifact_input, second_artifact_input):
        if (first_artifact_input.is_current):
            self.remove_from_stats(stats, first_artifact_input.artifact)
        elif (second_artifact_input.is_current):
            self.remove_from_stats(stats, second_artifact_input.artifact)

        self.base_dps = self.calculate_base(stats)
        self.first_artifact_dps = self.calculate_artifact(stats, first_artifact_input.artifact)
        self.second_artifact_dps = self.calculate_artifact(stats, second_artifact_input.artifact)

    def show_dps(self):
        print(self.base_dps)
        print(self.first_artifact_dps)
        print(self.second_artifact_dps)

    def calculate_artifact(self, stats, artifact):
        atk = stats.total_atk + artifact.flat_atk
        atk += round(stats.base_atk * (artifact.scale_atk / 100))
        crit_rate = stats.crit_rate + artifact.crit_rate
        crit_damage = stats.crit_damage + artifact.crit_damage

        return self.calculate_dps(atk, crit_rate, crit_damage)

    def calculate_base(self, stats):
        return self.calculate_dps(stats.total_atk, stats.crit_rate, stats.crit_damage)
    
    def calculate_dps(self, atk, crit_rate, crit_damage):
        crit_rate_decimal = crit_rate / 100
        crit_damage_decimal = crit_damage / 100
        return ((1 - crit_rate_decimal) * atk) + (crit_rate_decimal * (atk * (1 + crit_damage_decimal)))
    
    def remove_from_stats(self, stats, artifact):
        stats.total_atk -= artifact.flat_atk
        stats.total_atk -= round(stats.base_atk * (artifact.scale_atk / 100))
        stats.crit_rate -= artifact.crit_rate
        stats.crit_damage -= artifact.crit_damage