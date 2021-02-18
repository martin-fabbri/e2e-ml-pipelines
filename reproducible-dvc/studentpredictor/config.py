from pathlib import Path


class Config:
    RANDOM_SEED = 42
    ASSETS_PATH = Path("./reproducible-dvc/assets")
    ORIGINAL_DATASET_FILE_PATH = ASSETS_PATH / "original_dataset" / "udemy_courses.csv"
    DATASET_PATH = ASSETS_PATH / "data"
    FEATURES_PATH = ASSETS_PATH / "features"
    MODELS_PATH = ASSETS_PATH / "models"
    EVALUATION_PATH = ASSETS_PATH / "evaluation"
    METRICS_FILE_PATH = ASSETS_PATH / "evaluation" / "metrics.json"
