from datetime import timedelta

from feast import Entity, FeatureView, Field, FeatureStore
from feast.types import Int64, Float32
from feast.data_source import FileSource


# 1. Define data source (batch)
transactions_source = FileSource(
    path="data/transactions.csv",
    timestamp_field="event_timestamp",
)


# 2. Define entity
user = Entity(
    name="user_id",
    join_keys=["user_id"],
    description="Unique identifier for a user",
)


# 3. Define feature view
user_stats = FeatureView(
    name="user_stats",
    entities=[user],
    ttl=timedelta(hours=24),
    schema=[
        Field(name="txn_amount", dtype=Float32),
        Field(name="device_trust_score", dtype=Float32),
    ],
    online=True,
    source=transactions_source,
    tags={"team": "fraud-ml", "owner": "ml-platform"},
)


def get_store():
    """Helper to create a FeatureStore instance for scripts."""
    return FeatureStore(repo_path=".")