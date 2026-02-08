# CSV Server API — Windows Server Data Infrastructure

---
**File**: `csv_server_api.md`  
**Tag**: `eMemory.systems.infrastructure.csv_server`  
**Category**: 02_Systems  
**Agent**: CLERK  
**Created**: 2025-11-20  
**Last Updated**: 2025-11-20  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `techContext.md`, `mpts_systems.md`  
---

## 🎯 Purpose

The **CSV Server API** is Unity Energy's Windows-based data infrastructure for serving Unity meter CSV files to Mac development workstations. This Flask API enables remote access to meter data stored on Windows server, supporting the eestream analysis pipeline.

---

## 🏗️ Architecture

### **System Components**

```
Mac Development Environment (eVision)
    ↓ HTTP Request
Windows Server (99.177.88.145:5000)
    ↓ Flask API (csv_server.py)
D:\server_storage\{mac_address}\*.csv
    ↓ Process & Resample
Composite CSV Response
```

### **File Location**
- **Server Script**: `eVision/server/csv_server.py`
- **Management Script**: `eVision/server/manage_csv_server.sh`
- **Server Storage Path**: `D:\server_storage\` (Windows)
- **Server User**: `cster@99.177.88.145`

---

## 📡 API Endpoints

### **1. Health Check**
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "server": "csv_server",
  "version": "1.0"
}
```

---

### **2. List Meters**
```http
GET /list_meters
```

**Response:**
```json
{
  "meters": ["ecc38a20c2b8", "ecc38a211029", "ecc38a217ccc", ...],
  "count": 6
}
```

**Purpose**: Returns all available meter MAC addresses with data on server.

---

### **3. Meter Information**
```http
GET /meter_info/<mac_address>
```

**Example:**
```bash
curl http://99.177.88.145:5000/meter_info/ecc38a217ccc
```

**Response:**
```json
{
  "mac_address": "ecc38a217ccc",
  "file_count": 1523,
  "earliest_datetime": "2025-01-01T00:00:00-05:00",
  "latest_datetime": "2025-03-31T23:59:00-05:00"
}
```

**Purpose**: Get date range and file count for specific meter.

---

### **4. Generate Composite CSV**
```http
POST /generate_csv
```

**Request Body:**
```json
{
  "mac_address": "ecc38a217ccc",
  "start_datetime": "2025-01-01T00:00:00",
  "end_datetime": "2025-01-31T23:59:59",
  "resolution": "1min",
  "base_filename": "AN53111387-E-"
}
```

**Parameters:**
- `mac_address` (required): Meter MAC address
- `start_datetime` (required): Start of date range (ISO 8601 format)
- `end_datetime` (required): End of date range (ISO 8601 format)
- `resolution` (optional): Resampling resolution
  - Options: `1sec`, `1min`, `5min`, `15min`, `1hr`, `1day`
  - Default: `1min`
- `base_filename` (optional): Base meter serial number for output filename
  - Default: Uses MAC_TO_METERSN mapping

**Response:** CSV file download
- **Filename format**: `{base}{resolution}RES_{rows}CLP_{start}-{end}.csv`
- **Example**: `AN53111387-E-1minRES_44640CLP_250101.0000-250131.2359.csv`

**Processing:**
1. Find all CSV files in date range
2. Read and concatenate files
3. Filter by exact datetime range
4. Resample to specified resolution (mean aggregation)
5. Return composite CSV file

---

## 🗺️ MAC Address to Meter Mapping

### **Foster Farms Cherry Ave Site**

| MAC Address    | Meter Serial   | Transformer | Description        |
|----------------|----------------|-------------|--------------------|
| ecc38a217ccc   | AN53111387-E-  | T10         | Air Chiller        |
| 307a57001e28   | AN54021613-C-  | T12         | Main               |
| ecc38a2175a6   | AN53110845-F-  | T15         | Fillet             |
| 307a57007b50   | AN54022983-G-  | T16         | Compressor         |

### **Other Sites**

| MAC Address    | Meter Serial   | Site                     |
|----------------|----------------|--------------------------|
| ecc38a20c2b8   | AN21061800-H-  | HAD2500, Scranton, AR    |
| ecc38a211029   | AN21113351-A-  | ARMI Site, Fayetteville  |

---

## 🛠️ Server Management

### **Management Script**

The `manage_csv_server.sh` script provides SSH-based server control:

```bash
# Start server
./manage_csv_server.sh start

# Stop server
./manage_csv_server.sh stop

# Restart server
./manage_csv_server.sh restart

# Check status
./manage_csv_server.sh status

# View logs
./manage_csv_server.sh logs

# Test health endpoint
./manage_csv_server.sh test

# List meters
./manage_csv_server.sh meters
```

### **Manual Server Operations**

**SSH into server:**
```bash
ssh cster@99.177.88.145
```

**Start server manually:**
```cmd
D:
cd eSYSTEM
python csv_server.py
```

**Check if running:**
```cmd
netstat -ano | findstr :5000
```

**Stop server (Windows):**
```cmd
# Find PID
netstat -ano | findstr :5000
# Kill process
taskkill /F /PID {pid}
```

---

## 🔧 Technical Implementation

### **Key Features**

1. **CORS Enabled**: Accepts cross-origin requests from Mac development environment
2. **Timezone Handling**: All datetimes in `America/New_York` timezone
3. **Multiple Filename Patterns**: Supports various CSV filename formats
4. **Efficient Date Range Detection**: Reads first/last files to determine data availability
5. **Resampling**: Pandas-based resampling with mean aggregation
6. **In-Memory Processing**: CSV generated in memory (no disk writes)

### **Datetime Parsing Patterns**

The server supports multiple filename formats:

1. **Unity meter format**: `AN53111387-H-2025-11-06T15-00-00-0800-1min.csv`
2. **Standard format**: `20240115_103000.csv` or `20240115T103000.csv`
3. **Dash format**: `2024-01-15_10-30-00.csv`
4. **Short format**: `240115.1030.csv` (YYMMDD.HHMM)

### **Resampling Logic**

```python
resample_map = {
    '1sec': '1s',
    '1min': '1min',
    '5min': '5min',
    '15min': '15min',
    '1hr': '1H',
    '1day': '1d'
}
```

All numeric columns resampled using **mean aggregation**.

---

## 📋 Usage Workflow

### **Typical Data Request Flow**

1. **Check meter availability**:
   ```bash
   curl http://99.177.88.145:5000/list_meters
   ```

2. **Get date range for meter**:
   ```bash
   curl http://99.177.88.145:5000/meter_info/ecc38a217ccc
   ```

3. **Generate composite CSV**:
   ```bash
   curl -X POST http://99.177.88.145:5000/generate_csv \
     -H "Content-Type: application/json" \
     -d '{
       "mac_address": "ecc38a217ccc",
       "start_datetime": "2025-01-01T00:00:00",
       "end_datetime": "2025-01-31T23:59:59",
       "resolution": "1min"
     }' \
     --output T10_Jan2025_1min.csv
   ```

---

## 🔐 Security & Access

### **Network Configuration**
- **Server IP**: 99.177.88.145
- **Port**: 5000
- **Protocol**: HTTP (not HTTPS - internal network only)
- **SSH Access**: Required for server management

### **Firewall Requirements**
- Port 5000 must be open for HTTP requests
- Port 22 must be open for SSH management

---

## 🚨 Known Issues & Limitations

### **Current Limitations**
1. **No Authentication**: API endpoints are open (internal network only)
2. **No HTTPS**: Data transmitted unencrypted
3. **Single-threaded**: Flask development server (not production-grade)
4. **No Rate Limiting**: Could be overwhelmed by rapid requests
5. **No Request Queuing**: Large requests block other requests

### **Future Enhancements**
- Add API key authentication
- Implement HTTPS with SSL certificates
- Deploy with production WSGI server (Gunicorn/uWSGI)
- Add request rate limiting
- Implement background task queue (Celery)
- Add request progress tracking
- Cache frequently requested date ranges

---

## 📊 Performance Considerations

### **File Processing**
- **Typical request**: 1-month 1min resolution = ~44,640 rows
- **Processing time**: 30-60 seconds (depends on file count)
- **Memory usage**: Pandas loads all files in memory

### **Recommendations**
- Request smaller date ranges for faster processing
- Use higher resolution (5min, 15min, 1hr) for large spans
- Server has limited RAM - avoid concurrent large requests

---

## 🔗 Integration with eestream

### **Data Flow**

```
Unity Meter → Windows Server Storage
                    ↓
            CSV Server API
                    ↓
        Mac Development Environment
                    ↓
            eVision File Upload
                    ↓
            eBehavior Analysis Pipeline
```

### **Client Integration Example**

```python
import requests

# Get meter info
response = requests.get('http://99.177.88.145:5000/meter_info/ecc38a217ccc')
meter_info = response.json()

# Generate CSV
payload = {
    'mac_address': 'ecc38a217ccc',
    'start_datetime': '2025-01-01T00:00:00',
    'end_datetime': '2025-01-31T23:59:59',
    'resolution': '1min'
}
response = requests.post('http://99.177.88.145:5000/generate_csv', json=payload)

# Save CSV
with open('T10_Jan2025.csv', 'wb') as f:
    f.write(response.content)
```

---

## 📝 Maintenance Notes

### **Log Files**
- **Location**: `D:\eSYSTEM\csv_server.log`
- **Access**: Via SSH or `manage_csv_server.sh logs`

### **Common Issues**

**Server won't start:**
- Check if port 5000 already in use: `netstat -ano | findstr :5000`
- Check server storage path exists: `D:\server_storage`
- Verify Python and dependencies installed

**No files found error:**
- Verify MAC address exists in storage
- Check date range matches available data
- Use `/meter_info` endpoint to verify date range

**Connection refused:**
- Verify server is running: `./manage_csv_server.sh status`
- Check firewall allows port 5000
- Verify server IP address (99.177.88.145)

---

## 🎓 Key Concepts

### **MAC Address as Meter ID**
Unity meters are identified by MAC address (e.g., `ecc38a217ccc`). This is the primary key for all API operations.

### **Resolution vs Resampling**
- **Native resolution**: Unity meters capture at 1-second intervals
- **Resampling**: Server aggregates (mean) to requested resolution
- **Trade-off**: Higher resolution = more data points but slower processing

### **Date Range Detection**
Server reads actual CSV file contents (not filenames) to determine exact data availability. This ensures accuracy but requires file I/O.

---

## 🔮 Future Vision

### **Planned Enhancements**
1. **Real-time streaming**: WebSocket support for live meter data
2. **Data caching**: Redis cache for frequently requested ranges
3. **Metadata database**: PostgreSQL for meter info and file index
4. **Multi-site support**: Federated server architecture
5. **Authentication**: OAuth2 or API key system
6. **Dashboard**: Web UI for server monitoring and data exploration

---

**This CSV Server API is critical infrastructure for Unity Energy's remote data access.** It enables seamless meter data retrieval from Windows server storage to Mac development workstations, supporting the entire eestream analysis pipeline.

---

*Last Updated: November 20, 2025*  
*Maintained by: Unity Energy Maxwellians*
