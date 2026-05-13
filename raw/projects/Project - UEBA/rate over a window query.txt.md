# rate over a window query.txt

```
// Raw data from your dataset
@user_buckets <- @"main/Fortinet FortiGate Firewall (TF)" {
  // Filter your time range if needed
  // Then aggregate per user

  make_col user_id:string(xdm.principal.user.id)
// make_col user_id:string(xdm.target.user.id)
filter not is_null(user_id)
//make_col user_id:string(concat_strings("target_", user_id))
make_col user_id:string(concat_strings("principal_", user_id))

make_col event_type:string(xdm.meta.product.event_type)
make_col bytes_received:int64(coalesce(xdm.network.received_bytes, 0))
make_col bytes_sent:int64(coalesce(xdm.network.sent_bytes, 0))

// Start here

  timechart 5m,
    rate_per_sec: rate(bytes_received),
    bucket_value: avg(bytes_received),
    volatility:   stddev(bytes_received),
    group_by(user_id)
}


@user_agg <- @user_buckets {
  // 1) Per-user EWMA of bucket_value over a trailing 24h window
  make_col
    ema: window(
           ewma(bucket_value, 3),
           group_by(user_id),
           order_by(_c_valid_from),
           frame(back: 15m)
         )

  // 2) Deviation from baseline in this bucket
  make_col residual: bucket_value - ema

  // 3) Optional: also compute rate across buckets per user
  make_col bucket_rate: window(
           rate(bucket_value),
           group_by(user_id),
           order_by(_c_valid_from),
           frame(back: 3m)
         )
}

<- @user_agg {}
```
