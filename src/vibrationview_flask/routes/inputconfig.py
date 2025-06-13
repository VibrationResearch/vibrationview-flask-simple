from flask import Blueprint, jsonify
from vv_manager import extract_com_error_info, with_vv_connection

inputconfig_bp = Blueprint('inputconfig', __name__)

@inputconfig_bp.route('/inputconfig', methods=['GET'])

@with_vv_connection
def get_vv_inputconfig(vv_instance):
    try:
    
        channel_count = vv_instance.GetHardwareInputChannels()
        field_keys = [
            'ChName','CH', 'ChSensitivity', 'Unit', 'ChManufacturer',
            'ChModel', 'ChSerialNumber', 'ChDirection', 'ChAcp', 'ChOffset'
        ]

        # Collect all fields per channel
        field_data = {
            key: [vv_instance.ReportField(f'{key}{i + 1}') for i in range(channel_count)]
            for key in field_keys
        }

        # Combine into list of dicts per channel
        channels = []
        for i in range(channel_count):
            channel_info = {
                key: field_data[key][i] for key in field_keys
            }
            channels.append(channel_info)

        return jsonify(channels)

    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500

