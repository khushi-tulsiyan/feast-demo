# Feast Fraud Demo (Local Live Demo)

This is a minimal, **ready-to-run** Feast demo that you can use for a live walkthrough
with leadership.

It shows:

- Defining an entity and feature view for a `fraud detection` style use case
- Loading a small CSV as a batch (offline) data source
- Generating a **training dataset** from Feast
- Fetching **online features** for real-time inference

> Note: You need Feast installed in your Python environment.
> This layout roughly follows the Feast local quickstart; adjust config if your Feast
> version differs.

## 1. Install dependencies

```bash
pip install feast pandas
```

## 2. Project layout

```
feast_fraud_demo/
  feature_store.yaml      # Feast project config
  features.py             # Entity + FeatureView definitions
  generate_training_data.py  # Offline demo
  online_demo.py          # Online (real-time) demo
  data/
    transactions.csv      # Dummy batch data
```

## 3. Initialize Feast registry

From inside `feast_fraud_demo/`:

```bash
feast apply
```

This registers the entity + feature view in the Feast registry.

## 4. Generate training data (offline demo)

```bash
python generate_training_data.py
```

You should see a small training dataset printed with:

- `user_id`
- `event_timestamp`
- `txn_amount`
- `device_trust_score`

Explain to leadership:

- This is **point-in-time correct** historical data
- It can be joined with labels (fraud/not fraud) for model training

## 5. Online demo (real-time features)

```bash
python online_demo.py
```

This will:

1. Materialize recent data into the online store
2. Fetch the online feature vector for `user_id=1`
3. Print it out

Explain to leadership:

- The **same features** used for training are now served online
- APIs or services can query Feast and send these features into a model
- This removes training/serving skew and centralizes feature logic