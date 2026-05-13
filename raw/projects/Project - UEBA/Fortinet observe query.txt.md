# Fortinet observe query.txt

```
// =====================================================================
// Fortinet FortiGate Firewall - Aggregated Stats per User per 1h Window
// Raw numeric stats + arrays for categoricals, rate per hour
// =====================================================================

@fortinet_hourly <- @"main/Fortinet FortiGate Firewall (TF)" {

  // ----------- Normalize user_id -----------
  make_col user_id:string(xdm.principal.user.id)
  // make_col user_id:string(xdm.target.user.id)
  filter not is_null(user_id)
  // make_col user_id:string(concat_strings("target_", user_id))
  make_col user_id:string(concat_strings("principal_", user_id))

  // ----------- Original extracted fields -----------
  make_col event_type:string(xdm.meta.product.event_type)
  make_col bytes_received:int64(coalesce(xdm.network.received_bytes, 0))
  make_col bytes_sent:int64(coalesce(xdm.network.sent_bytes, 0))
  make_col user_agent:string(xdm.network.http.user_agent)
  make_col app_protocol:string(xdm.network.application_protocol)
  make_col rule_name:string(xdm.result.rule.name)
  make_col result_summary:string(xdm.result.summary)

  // Use actions field as requested
  make_col action:string(xdm.result.actions)

  // Principal IP object fields
  make_col principal_address:string(xdm.principal.ip[0].address)
  make_col principal_port:int64(coalesce(xdm.principal.ip[0].port, 0))
  make_col principal_geo_country_or_region:string(xdm.principal.ip[0].location.country_or_region)

  // Target IP object fields
  make_col target_address:string(xdm.target.ip[0].address)
  make_col target_port:int64(coalesce(xdm.target.ip[0].port, 0))
  make_col target_geo_country_or_region:string(xdm.target.ip[0].location.country_or_region)

  make_col file_name:string(xdm.principal.file.name)

  // ----------- Pick only needed columns early -----------
  pick_col
    observe_timestamp,
    user_id,
    event_type,
    bytes_received,
    bytes_sent,
    user_agent,
    app_protocol,
    rule_name,
    result_summary,
    action,
    principal_address,
    principal_port,
    principal_geo_country_or_region,
    target_address,
    target_port,
    target_geo_country_or_region,
    file_name

  // ----------- Aggregate per user per 1h -----------
  timechart options(empty_bins:true), bin_duration:1h, group_by(user_id),

    // Total event count
    agg_event_count:          count(),
    agg_summary_count:        count(result_summary),

    // Raw numeric aggregations - bytes_received (sum, sum_sq, count)
    agg_bytes_received_sum:   sum(bytes_received),
    agg_bytes_received_sum_sq:sum(pow(float64(bytes_received), 2)),
    agg_bytes_received_count: count(bytes_received),

    // Raw numeric aggregations - bytes_sent (sum, sum_sq, count)
    agg_bytes_sent_sum:       sum(bytes_sent),
    agg_bytes_sent_sum_sq:    sum(pow(float64(bytes_sent), 2)),
    agg_bytes_sent_count:     count(bytes_sent),

    // Categorical - full arrays for distribution calculations
    agg_user_agent_array:     array_agg(user_agent),
    agg_app_protocol_array:   array_agg(app_protocol),
    agg_principal_address_array: array_agg(principal_address),
    agg_target_address_array:    array_agg(target_address),
    agg_principal_port_array:    array_agg(principal_port),
    agg_target_port_array:       array_agg(target_port),
    agg_principal_geo_country_array: array_agg(principal_geo_country_or_region),
    agg_target_geo_country_array:    array_agg(target_geo_country_or_region),

    // Categorical - distinct only
    agg_event_type_array:     array_agg_distinct(event_type),
    agg_file_name_array:      array_agg_distinct(file_name),
    agg_rule_name_array:      array_agg_distinct(rule_name),

    // Simple UEBA counts from action / result_summary
    agg_action_array:         array_agg(action)

  // ----------- Boolean flags from aggregated fields -----------
  make_col agg_has_file:    bool(array_length(agg_file_name_array) > 0)
  make_col agg_has_rule:    bool(array_length(agg_rule_name_array) > 0)
  make_col agg_has_summary: bool(agg_summary_count > 0)

  // ----------- Expose bucket start for joining ----------- 
  make_col bucket_start: _c_valid_from
}

<- @fortinet_hourly {}
```
