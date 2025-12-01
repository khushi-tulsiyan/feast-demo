"""Script to demonstrate Feast online feature retrieval."""

from datetime import datetime
from features import get_store


def main():
    store = get_store()

    # Materialize into online store (for demo we just pick a recent time)
    print("Materializing features into online store...")
    store.materialize_incremental(end_date=datetime.utcnow())

    # Fetch online features for a single user
    feature_vector = store.get_online_features(
        features=[
            "user_stats:txn_amount",
            "user_stats:device_trust_score",
        ],
        entity_rows=[{"user_id": 1}],
    ).to_dict()

    print("\n=== Online feature vector for user_id=1 ===")
    for k, v in feature_vector.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()