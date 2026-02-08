# Tech Context - Unity Energy eestream System

---
**File**: `techContext.md`  
**Tag**: `eMemory.context.technical.stack`  
**Category**: 01_Context  
**Agent**: COLLABORATIVE  
**Created**: 2025-10-16  
**Last Updated**: 2025-10-16  
**Status**: ACTIVE  
**Importance**: HIGH  
**Related**: `productContext.md`, `systemPatterns.md`, `quickref.md`  
---

## Technologies Used

### Core Python Stack
- **Python 3.10+** - Primary development language with modern features
- **Streamlit** - Interactive web interface for eVision module
- **Pandas** - Data manipulation and analysis for CSV processing
- **NumPy** - Numerical computations for energy calculations
- **Matplotlib/Plotly** - Data visualization and charting

### AI & Machine Learning Integration
- **OpenAI GPT-4o** - AI analysis, text generation, and TTS capabilities
- **OpenAI API** - Structured analysis and intelligent interpretation
- **ElevenLabs** - High-quality voice synthesis for audio output
- **PyAudio** - Real-time audio streaming and playback

### Data Processing & Storage
- **CSV Processing** - Primary data format for energy measurements
- **SQL Integration** - Database queries and data selection interfaces
- **JSON** - Configuration and data exchange format between modules
- **Markdown** - Report generation and documentation format

### Web Technologies
- **HTML5** - Dashboard templates with modern features
- **CSS3** - Advanced styling with gradients, animations, and responsive design
- **JavaScript** - Interactive dashboard functionality and data integration
- **SVG** - Vector graphics for gauges and technical diagrams

### Development Infrastructure
- **Git** - Version control with GitHub integration
- **Conda/Miniconda** - Environment management and package installation
- **pip** - Python package management
- **VS Code** - Primary development environment

## Development Setup

### Environment Requirements
```bash
# Python Environment
Python 3.10+
Conda/Miniconda (recommended)
pip package manager

# System Requirements
8GB RAM minimum (16GB recommended)
2GB free disk space
Internet connection for API services
Modern web browser
```

### Installation Process
```bash
# 1. Repository Setup
git clone https://github.com/helirush/eestream.git
cd eestream

# 2. Environment Creation
conda create -n eestream python=3.10
conda activate eestream

# 3. Dependencies
pip install -r requirements.txt

# 4. Configuration
cp eConfig/.env.example eConfig/.env
# Edit .env with API keys
```

### Required API Keys
- **OpenAI API Key** - Core AI analysis and TTS functionality
- **Notion API Key** (optional) - Automated report management
- **ElevenLabs API Key** (optional) - Premium voice synthesis

## Technical Constraints

### Performance Constraints
- **Memory Usage**: Large CSV files (>100MB) require significant RAM
- **Processing Time**: Complex analysis can take 5-15 minutes for large datasets
- **API Rate Limits**: OpenAI and ElevenLabs APIs have usage quotas
- **File I/O**: Heavy disk usage during report generation and dashboard creation

### Data Constraints
- **CSV Format Requirements**: Specific column names and data types expected
- **Date Range Limitations**: Analysis optimized for 30-365 day periods
- **Transformer Data**: Requires industrial 480V electrical system data
- **Weather Data**: Optional but enhances analysis accuracy

### Integration Constraints
- **Local Processing**: Core analysis runs locally for data security
- **API Dependencies**: Some features require internet connectivity
- **Browser Compatibility**: Dashboards optimized for modern browsers
- **File Path Limitations**: Long transformer names may cause path issues on some systems

## Dependencies

### Core Python Packages
```python
# Data Processing
pandas >= 1.5.0
numpy >= 1.24.0
matplotlib >= 3.6.0
plotly >= 5.0.0

# AI Integration
openai >= 1.0.0
elevenlabs >= 0.2.0

# Web Interface
streamlit >= 1.25.0
jinja2 >= 3.1.0

# Audio Processing
pyaudio >= 0.2.11
pygame >= 2.1.0

# Utilities
python-dotenv >= 1.0.0
requests >= 2.28.0
pathlib >= 1.0.0
```

### System Dependencies
- **Audio System**: Required for PyAudio and voice playback
- **Web Browser**: For viewing generated dashboards
- **File System**: Write permissions for report generation
- **Network Access**: For API calls and data downloads

### Optional Dependencies
- **Notion API**: For automated report publishing
- **Database Drivers**: For SQL data integration
- **Additional Audio Codecs**: For enhanced audio format support

## Tool Usage Patterns

### Primary Development Workflow
1. **Environment Activation**: `conda activate eestream`
2. **Code Development**: VS Code with Python extension
3. **Local Testing**: Direct script execution and debugging
4. **Data Testing**: Sample CSV files in `eSlices/` directory
5. **Version Control**: Git commits with descriptive messages

### Analysis Workflow
```bash
# Standard Analysis Process
cd eBehavior
python eeBEHAVIOR.py

# Visual Interface
cd eVision  
streamlit run eeVISION.py

# Audio Processing
cd eAudio
python process_audio_script.py
```

### Configuration Management
- **Centralized Config**: All settings in `eConfig/.env`
- **Environment Variables**: Override defaults for different deployments
- **Security**: API keys never committed to version control
- **Validation**: Automatic configuration validation on startup

### Testing Patterns
- **Sample Data**: `eSlices/` directory contains test CSV files
- **Unit Testing**: Individual module testing capabilities
- **Integration Testing**: Full workflow testing with sample data
- **Output Validation**: Automated checking of generated files

### Deployment Patterns
- **Local Deployment**: Standard development environment
- **Portable Deployment**: Conda environment packaging
- **Cloud Deployment**: AWS/Azure compatible architecture
- **Container Deployment**: Docker-ready configuration

## Development Best Practices

### Code Organization
- **Module Separation**: Clear boundaries between eBehavior, eVision, eAudio, eMarket
- **Configuration Centralization**: Single source for all settings
- **Template System**: Reusable HTML templates with parameter replacement
- **Error Handling**: Comprehensive error catching and user-friendly messages

### Data Management
- **Consistent Naming**: Standardized file and variable naming conventions
- **Data Validation**: Input validation at multiple stages
- **Backup Strategy**: Automatic backup of important analysis results
- **Version Tracking**: Analysis metadata for reproducibility

### Security Practices
- **API Key Management**: Environment-based key storage
- **Data Privacy**: Local processing to protect sensitive energy data
- **Input Sanitization**: Validation of user inputs and file uploads
- **Output Validation**: Verification of generated files and reports

### Performance Optimization
- **Memory Management**: Efficient handling of large datasets
- **Caching Strategy**: Reuse of processed data where appropriate
- **Parallel Processing**: Multi-threading for independent analysis tasks
- **Resource Monitoring**: Tracking of system resource usage

This technical foundation enables the eestream system to process complex industrial energy data efficiently while maintaining reliability, security, and extensibility for future enhancements.
