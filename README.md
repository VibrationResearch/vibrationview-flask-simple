# VibrationVIEW API

A Flask-based REST API for controlling and monitoring VibrationVIEW software. This API provides programmatic access to VibrationVIEW's core functionality including test control, channel management, data acquisition, and system status monitoring.

## Features

- **System Status**: Monitor VibrationVIEW system status and hardware information
- **Channel Management**: Configure and monitor input channels
- **Test Control**: Start, stop, and manage vibration tests
- **Data Acquisition**: Retrieve frequency, time history, and waveform data
- **File Operations**: Upload and open test files
- **TEDS Support**: Access transducer electronic data sheet information
- **Logging**: Retrieve system events and logs

## API Endpoints

### System Status
- `GET /status` - Get VibrationVIEW system status, serial number, version, and hardware info

### Channel Operations
- `GET /channels` - Get basic channel information
- `GET /channelstatus` - Get detailed channel status including sensitivity, units, and configuration
- `GET /inputconfig` - Get hardware input channel configuration
- `GET /channelpretest` - Get channel pretest information including SNR and limits

### Test Control
- `PUT /starttest` - Start a vibration test
- `PUT /stoptest` - Stop a running test
- `PUT /opentest?filename=<name>` - Upload and open a test file (binary data in request body)

### Data Retrieval
- `GET /datafreq` - Get frequency domain data
- `GET /datahistory` - Get time history data
- `GET /datatime` - Get waveform/time domain data

### TEDS (Transducer Electronic Data Sheet)
- `GET /inputteds` - Get TEDS information for all input channels

### Logging
- `GET /log` - Get system events and log entries

### Saved Data
- `GET /lastsaveddata` - Get information about the last saved data

## Installation

1. **Prerequisites**
   - Python 3.7+
   - VibrationVIEW software installed and licensed
   - Flask and required dependencies

2. **Install Dependencies**
   ```bash
   pip install flask
   # Additional dependencies as specified in your requirements.txt
   ```

3. **Setup**
   - Ensure VibrationVIEW is properly installed and configured
   - Configure the VibrationVIEW API connection settings
   - Set up the Flask application

## Usage

### Starting the API Server

```bash
python app.py
```

The API will be available at `http://localhost:5000` (or your configured host/port).

### Example Requests

#### Get System Status
```bash
curl -X GET http://localhost:5000/status
```

#### Start a Test
```bash
curl -X PUT http://localhost:5000/starttest
```

#### Upload and Open Test File
```bash
curl -X PUT "http://localhost:5000/opentest?filename=mytest.vvw" \
     -H "Content-Type: application/octet-stream" \
     --data-binary @mytest.vvw
```

#### Get Channel Status
```bash
curl -X GET http://localhost:5000/channelstatus
```

#### Retrieve Frequency Data
```bash
curl -X GET http://localhost:5000/datafreq
```

## Response Format

All endpoints return JSON responses. Successful responses contain the requested data, while error responses include error details:

```json
{
  "Status": "Ready",
  "Color": "Green",
  "SerialNumber": "12345",
  "Version": "2024.1"
}
```

Error responses:
```json
{
  "Error": "Description of the error",
  "Code": "Error code if available"
}
```

## File Upload Limits

- Maximum file size for test uploads: 10 MB (configurable)
- Supported file types: VibrationVIEW test files (.vvw, .vvs, etc.)

## Error Handling

The API includes comprehensive error handling:
- COM/VibrationVIEW connection errors
- File upload validation
- Test execution errors
- Data retrieval errors

All errors are returned with appropriate HTTP status codes and descriptive error messages.

## Architecture

The API is built using Flask with a modular blueprint structure:

- `status.py` - System status endpoints
- `channels.py` - Channel management endpoints
- `testcontrol.py` - Test control endpoints
- `vectordata.py` - Data acquisition endpoints
- `opentest.py` - File upload and test opening
- `teds.py` - TEDS information endpoints
- `log.py` - Logging endpoints
- `pretest.py` - Pretest functionality

## Dependencies

- **Flask**: Web framework (BSD-3-Clause license)
- **VibrationVIEW**: Licensed vibration control and analysis software (Proprietary license)
- VibrationVIEW automation option (VR9604) - OR - VibrationVIEW may be run in Simulation mode without any additional hardware or software

**Note**: While this example code is released under CC0 (public domain), each dependency has its own license terms that must be respected. Users are responsible for ensuring compliance with all third-party library licenses. A valid VibrationVIEW software license is required to use this API, as it interfaces with the licensed VibrationVIEW application.
- **Custom utilities**: Error handling, data parsing, and VibrationVIEW management

## Configuration

Configure the following settings in your application:

- VibrationVIEW installation path
- API server host and port
- File upload directories
- Maximum file size limits
- Timeout settings for test operations

## Security Considerations

- Implement authentication/authorization as needed
- Validate all file uploads
- Sanitize input parameters
- Use HTTPS in production environments
- Limit access to trusted networks

## Troubleshooting

### Common Issues

1. **VibrationVIEW Connection Failed**
   - Ensure VibrationVIEW is installed and licensed
   - Check that no other applications are using VibrationVIEW
   - Verify COM interface is properly registered

2. **File Upload Errors**
   - Check file size limits
   - Verify file format is supported
   - Ensure sufficient disk space

3. **Test Control Issues**
   - Verify hardware connections
   - Check channel configurations
   - Review test parameters

## Contributing

This is example software provided for demonstration purposes. This repository is not actively monitored by Vibration Research (VR). 

If you wish to contribute improvements or modifications:
1. Fork the repository
2. Create a feature branch
3. Make your changes

Please note that contributions may not be reviewed or merged in a timely manner as this is not an official VR maintained project.

## License

CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

To the extent possible under law, Vibration Research Corporation has waived all copyright and related or neighboring rights to this work. This work is published from: United States.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

For more information, see: https://creativecommons.org/publicdomain/zero/1.0/

## Support

For issues and questions:
- Check the troubleshooting section
- Review VibrationVIEW documentation
- Contact technical support

---

**Note**: This API requires VibrationVIEW software to be installed and properly licensed. Ensure all hardware connections and configurations are correct before using the API endpoints.