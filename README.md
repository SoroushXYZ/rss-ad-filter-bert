# RSS Advertisement Detection with BERT

A BERT-based classifier for detecting advertisements in RSS news feeds.

## Project Structure

```
rss-ad-filter-bert/
├── src/
│   ├── data_collection/    # RSS feed collection and processing
│   ├── models/            # BERT model training and inference
│   └── utils/             # Utility functions
├── data/                  # Raw and processed datasets
├── tests/                 # Test files
├── requirements.txt       # Python dependencies
└── README.md
```

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies (as needed during development):
```bash
pip install -r requirements.txt
```

## Current Status

- ✅ Virtual environment setup
- ✅ Basic project structure
- ✅ RSS data collection
- ✅ Article labeling interface
- ⏳ BERT model development
- ⏳ GitHub/Hugging Face integration

## Usage

### 1. Data Collection
Run the Jupyter notebook to collect RSS articles:
```bash
jupyter notebook notebooks/01_rss_data_collection.ipynb
```

### 2. Article Labeling
Start the web interface for labeling articles:
```bash
python run_labeling.py
```
Then open http://localhost:5001 in your browser.

**Keyboard shortcuts:**
- `1` or `A` = Mark as Advertisement
- `2` or `N` = Mark as News  
- `S` = Skip article
- `←` = Go to previous article
- `→` = Go to next article

**⚡ Super fast labeling:** Just press any key to label instantly - no clicking needed!

### 3. Model Training
*Coming next: BERT model training notebook*

## Development Plan

1. **Data Collection**: ✅ Gather RSS feeds and create labeled dataset
2. **Article Labeling**: ✅ Web interface for manual labeling
3. **Model Development**: Fine-tune BERT for advertisement classification
4. **Integration**: Set up GitHub and Hugging Face repositories
5. **Deployment**: Create inference pipeline and API