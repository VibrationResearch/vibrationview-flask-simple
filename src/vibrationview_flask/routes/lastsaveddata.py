from flask import Blueprint, jsonify, send_file
from utils import DecodeStatusColor, GenerateReportFromVV
from vv_manager import with_vv_connection

lastsaveddata_bp = Blueprint('lastsaveddata', __name__)
@lastsaveddata_bp.route('/lastsaveddata', methods=['GET'])

@with_vv_connection
def lastsaveddata(vv_instance):
    try:
        filename = vv_instance.ReportField('LastData')
        if not filename:
            return jsonify({'Error': 'No saved file in VibrationVIEW'}), 204

        out_path = GenerateReportFromVV(filename, 'Test report.txt', 'report.txt')

        return send_file(
            out_path,
            as_attachment=True,
            download_name=out_path,
            mimetype='application/octet-stream'
        )
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
