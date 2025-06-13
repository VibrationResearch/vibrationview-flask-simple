from flask import Blueprint, jsonify
from utils import get_channel_data
from vv_manager import with_vv_connection

channels_bp = Blueprint('channels', __name__)

@channels_bp.route('/channels', methods=['GET'])
@with_vv_connection
def get_channels(vv_instance):
    channels = vv_instance.Channel()
    return jsonify(channels)

@channels_bp.route('/channelstatus', methods=['GET'])
@with_vv_connection
def get_channel_status(vv_instance):
    field_keys = [
        'ChName','CH', 'ChSensitivity','CondSensitivity','AccelSensitivity', 'Unit', 'ChManufacturer',
        'ChModel', 'ChID','ChType','ChSerialNumber', 'ChDirection', 'ChAcp', 'ChOffset','NoiseRMS','ChDCInput'
    ]

    channels = get_channel_data(vv_instance, field_keys)
    return jsonify(channels)
