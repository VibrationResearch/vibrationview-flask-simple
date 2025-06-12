def ParseVvTable(dict_table):
    """Parse VibrationVIEW table format"""
    # Implementation depends on the actual format returned
    # This is a placeholder for your existing implementation
    pass

def DecodeStatusColor(status):
    color_map = {
        0: 'healthy',
        1: 'yellow',
        2: 'critical'
    }
        # Convert string to integer if needed

    return_color_code = status['stop_code_index'] >> 12
    return color_map.get(return_color_code, 'unknown')


def get_channel_data(vv_instance, field_keys):
    """
    Common function to get channel data for multiple routes
    
    Args:
        vv_instance: VibrationVIEW instance
        field_keys: List of field keys to retrieve for each channel
        
    Returns:
        List of dictionaries with channel data
    """
    if not vv_instance:
        return None
        
    channel_count = vv_instance.GetHardwareInputChannels()
    
    # Collect all fields per channel
    field_data = {
        key: [vv_instance.ReportField(f'{key}{i + 1}') for i in range(channel_count)]
        for key in field_keys
    }

    # Combine into list of dictionaries per channel
    channels = []
    for i in range(channel_count):
        channel_info = {
            key: field_data[key][i] for key in field_keys
        }
        channels.append(channel_info)
        
    return channels
