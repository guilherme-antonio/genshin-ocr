from artifact import Artifact
from stats import Stats
from damage_calculator import DamageCalculator, DamageCalculatorArtifactInput
from ocr import OCR

ocr = OCR()

base_stats = ocr.read('hutao.png')
stats = Stats(base_stats)

first_artifact_stats = ocr.read('sands-1.png')
first_artifact = Artifact(first_artifact_stats)
first_artifact_input = DamageCalculatorArtifactInput(first_artifact, True)

second_artifact_stats = ocr.read('sands-2.png')
second_artifact = Artifact(second_artifact_stats)
second_artifact_input = DamageCalculatorArtifactInput(second_artifact, False)

calculator = DamageCalculator(stats, first_artifact_input, second_artifact_input)
calculator.show_dps()