import numpy as np
import pandas as pd
from config import Config
from sklearn.model_selection import train_test_split

np.random.seed(Config.RANDOM_SEED)

Config.DATASET_PATH.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(str(Config.ORIGINAL_DATASET_FILE_PATH))

df_train, df_test = train_test_split(
    df,
    test_size=0.2,
    random_state=Config.RANDOM_SEED,
)

df_train.to_csv(str(Config.DATASET_PATH / "train.csv"), index=None)
df_test.to_csv(str(Config.DATASET_PATH / "test.csv"), index=None)
