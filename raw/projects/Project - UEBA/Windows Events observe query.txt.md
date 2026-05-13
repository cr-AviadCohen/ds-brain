# Windows Events observe query.txt

```
// =====================================================================
// Fortinet FortiGate Firewall - Aggregated Stats per User per 1h Window
// Raw numeric stats + arrays for categoricals, rate per hour
// =====================================================================

@windows_events_hourly <- @"main/Microsoft Windows Event (TF)" {

  // ----------- Normalize user_id -----------
  make_col user_id:string(xdm.principal.user.id)
  // make_col user_id:string(xdm.target.user.id)
  filter not is_null(user_id)
  // make_col user_id:string(concat_strings("target_", user_id))
  make_col user_id:string(concat_strings("principal_", user_id))

  make_col event_type:string(xdm.meta.product.event_type)
  make_col auth_mechanism:string(xdm.extensions.auth.mechanism)
  make_col action_result:string(xdm.result.actions)
  make_col file_path:string(xdm.principal.process.file.path)
  make_col group_display_name:string(xdm.target.group.group_display_name)
  make_col principal_windows_sid:string(xdm.principal.user.windows_sid)
  make_col target_windows_sid:string(xdm.target.user.windows_sid)
  
  // Principal IP object fields - correct address extraction
  make_col principal_address:string(xdm.principal.ip[0].address)
  make_col principal_port:int64(coalesce(xdm.principal.ip[0].port, 0))
  
  // Target IP object fields - correct address extraction
  make_col target_address:string(xdm.target.ip[0].address)
  make_col target_port:int64(coalesce(xdm.target.ip[0].port, 0))

  // ----------- Pick only needed columns early -----------
  pick_col
      observe_timestamp,
      user_id,
      event_type,
      auth_mechanism,
      action_result,
      file_path,
      group_display_name,
      principal_windows_sid,
      target_windows_sid,
      principal_address,
      principal_port,
      target_address,
      target_port

// Aggregate using timechart with 1h intervals
timechart options(empty_bins:true), bin_duration:1h, group_by(user_id),
    // Total event count
    agg_event_count:count(),
    
    // Categorical - full arrays for distribution calculations
    agg_auth_mechanism_array:array_agg(auth_mechanism),
    agg_file_path_array:array_agg(file_path),
    agg_principal_address_array:array_agg(principal_address),
    agg_target_address_array:array_agg(target_address),
    agg_principal_port_array:array_agg(principal_port),
    agg_target_port_array:array_agg(target_port),

    // Categorical - distinct only
    agg_event_type_array:array_agg_distinct(event_type),
    agg_group_display_name:array_agg_distinct(group_display_name),
    agg_principal_windows_sid:array_agg_distinct(principal_windows_sid),
    agg_target_windows_sid:array_agg_distinct(target_windows_sid)
    
  // ----------- Expose bucket start for joining ----------- 
  make_col bucket_start: _c_valid_from
}

<- @windows_events_hourly {}
```
