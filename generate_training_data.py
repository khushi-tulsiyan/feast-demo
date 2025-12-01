"""Script to demonstrate Feast offline (training) data retrieval."""

import pandas as pd
from datetime import datetime

from features import get_store


def main():
    store = get_store()

    # 1) Simple entity dataframe: which users, at what time
    entity_df = pd.DataFrame(
        {
            "user_id": [1, 2, 3],
            "event_timestamp": [
                datetime.fromisoformat("2025-11-30T10:30:00"),
                datetime.fromisoformat("2025-11-30T10:30:00"),
                datetime.fromisoformat("2025-11-30T10:30:00"),
            ],
        }
    )

    # 2) Ask Feast for historical features for training
    training_data = store.get_historical_features(
        entity_df=entity_df,
        features=[
            "user_stats:txn_amount",
            "user_stats:device_trust_score",
        ],
    ).to_df()

    print("\n=== Training dataset from Feast ===")
    print(training_data)


if __name__ == "__main__":
    main()