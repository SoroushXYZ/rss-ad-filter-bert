# RSS Advertisement Detection with DistilBERT

A machine learning project that uses DistilBERT to classify RSS article titles as advertisements or legitimate news content.

## 🎯 Project Overview

This project provides a complete pipeline for:
1. **Collecting RSS feeds** from 75+ tech news sources
2. **Labeling articles** using an intuitive web interface
3. **Training a DistilBERT model** for advertisement classification
4. **Publishing the model** to Hugging Face Hub

## 🚀 Features

### Data Collection
- **75+ RSS sources** including major tech outlets (TechCrunch, WIRED, The Verge, etc.)
- **AI/ML research sources** (OpenAI, Google AI, DeepMind, etc.)
- **Comprehensive coverage** of tech news, data science, and cloud computing

### Labeling Interface
- **Fast keyboard shortcuts**: `1`/`A` for ads, `2`/`N` for news, `S` to skip
- **Auto-resume functionality** - never lose your progress
- **Visual feedback** with instant key press confirmation
- **Progress tracking** with real-time statistics

### Model Training
- **DistilBERT-based** classifier (faster than BERT, 95% accuracy)
- **Binary classification**: Advertisement vs News
- **Comprehensive evaluation** with detailed metrics
- **Ready for Hugging Face** model publishing

## 📁 Project Structure

```
rss-ad-filter-bert/
├── notebooks/
│   ├── 01_rss_data_collection.ipynb    # Collect RSS articles
│   ├── 02_explore_labeled_data.ipynb   # Analyze labeled dataset
│   └── 03_train_distilbert.ipynb       # Train DistilBERT model
├── templates/
│   ├── labeling.html                   # Main labeling interface
│   └── completed.html                  # Completion summary
├── app.py                              # Flask labeling application
├── run_labeling.py                     # Easy startup script
├── requirements.txt                    # Python dependencies
└── README.md
```

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rss-ad-filter-bert.git
cd rss-ad-filter-bert
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 📊 Usage

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
Train the DistilBERT model:
```bash
jupyter notebook notebooks/03_train_distilbert.ipynb
```

## 🤗 Hugging Face Model

The trained model is available on Hugging Face Hub:

**Model Card**: [SoroushXYZ/distilbert-rss-ad-detection](https://huggingface.co/SoroushXYZ/distilbert-rss-ad-detection)

### Usage Example
```python
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", 
                     model="SoroushXYZ/distilbert-rss-ad-detection")

# Classify a title
result = classifier("50% OFF - Limited Time Offer on Premium Headphones!")
print(result)  # [{'label': 'advertisement', 'score': 0.95}]
```

## 📈 Model Performance

- **Accuracy**: ~95%
- **F1 Score**: ~94%
- **Precision**: ~93%
- **Recall**: ~94%

### Dataset Statistics
- **Total articles collected**: 1,600+
- **Labeled articles**: 1,000+
- **Sources**: 75+ tech news outlets
- **Class distribution**: Balanced dataset

## 🔧 Technical Details

### Model Architecture
- **Base Model**: DistilBERT-base-uncased
- **Task**: Binary text classification
- **Input**: RSS article titles (max 128 tokens)
- **Output**: Advertisement (1) or News (0)

### Training Configuration
- **Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 5e-5 (with warmup)
- **Optimizer**: AdamW with weight decay

## 📝 Data Sources

The model is trained on RSS feeds from:

### Major Tech News
- TechCrunch, WIRED, The Verge, Ars Technica
- Engadget, Gizmodo, CNET, TechRadar
- Digital Trends, VentureBeat, GeekWire

### AI/ML Research
- OpenAI Blog, Google AI Research, DeepMind
- Berkeley AI Research, Machine Learning Mastery
- Towards Data Science, KDnuggets

### Cloud & Enterprise
- AWS News Blog, Microsoft Azure, Google Cloud
- IBM Cloud, TechRepublic, InfoWorld

*...and 50+ more sources*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Transformers library
- [DistilBERT](https://huggingface.co/distilbert-base-uncased) for the base model
- All the RSS feed providers for their valuable content

## 📞 Contact

- **GitHub**: [@SoroushXYZ](https://github.com/SoroushXYZ)
- **Hugging Face**: [@SoroushXYZ](https://huggingface.co/SoroushXYZ)
- **Model**: [SoroushXYZ/distilbert-rss-ad-detection](https://huggingface.co/SoroushXYZ/distilbert-rss-ad-detection)

---

⭐ **Star this repository** if you found it helpful!