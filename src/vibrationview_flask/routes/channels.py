from flask import Blueprint, jsonify
from utils import get_channel_data, extract_com_error_info
from vv_manager import with_vibrationview

channels_bp = Blueprint('channels', __name__)

@channels_bp.route('/channels', methods=['GET'])
@with_vibrationview
def get_channels(vv_instance):
    channels = vv_instance.Channel()
    return jsonify(channels)

channels_bp = Blueprint('channels', __name__)
@channels_bp.route('/channelstatus', methods=['GET'])
@with_vibrationview
def get_channel_status(vv_instance):
    field_keys = [
        'ChName','CH', 'ChSensitivity','CondSensitivity','AccelSensitivity', 'Unit', 'ChManufacturer',
        'ChModel', 'ChID','ChType','ChSerialNumber', 'ChDirection', 'ChAcp', 'ChOffset','NoiseRMS','ChDCInput'
    ]

    channels = get_channel_data(vv_instance, field_keys)
    return jsonify(channels)

channels_bp = Blueprint('channels', __name__)
@channels_bp.route('/inputconfig', methods=['GET'])
@with_vibrationview
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