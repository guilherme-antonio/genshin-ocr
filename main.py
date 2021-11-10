from artifact import Artifact
from stats import Stats
from ocr import OCR

ocr = OCR()

base_stats = ocr.read('hutao.png')
print(base_stats)
stats = Stats(base_stats)
stats.show_stats()

first_artifact_stats = ocr.read('sands-1.png')
first_artifact = Artifact(first_artifact_stats)
first_artifact.show_stats()

second_artifact_stats = ocr.read('sands-2.png')
second_artifact = Artifact(second_artifact_stats)
second_artifact.show_stats()