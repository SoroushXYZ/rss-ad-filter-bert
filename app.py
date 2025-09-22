from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime
import glob

app = Flask(__name__)

# Global variables to track labeling progress
current_index = 0
articles = []
labels = {}  # Store labels as {index: label}

def load_latest_articles():
    """Load the most recent RSS articles JSON file"""
    global articles
    data_dir = 'data'
    json_files = glob.glob(os.path.join(data_dir, 'rss_articles_*.json'))
    
    if not json_files:
        return False
    
    # Get the most recent file
    latest_file = max(json_files, key=os.path.getctime)
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    print(f"Loaded {len(articles)} articles from {latest_file}")
    return True

def load_latest_labels():
    """Load the most recent labels JSON file and return progress"""
    global labels, current_index
    data_dir = 'data'
    label_files = glob.glob(os.path.join(data_dir, 'labels_*.json'))
    
    if not label_files:
        return False
    
    # Get the most recent labels file
    latest_labels_file = max(label_files, key=os.path.getctime)
    
    with open(latest_labels_file, 'r', encoding='utf-8') as f:
        label_data = json.load(f)
    
    labels = label_data.get('labels', {})
    # Set current index to the next unlabeled article
    current_index = len(labels)
    
    print(f"Resumed labeling from {latest_labels_file}")
    print(f"Previously labeled: {len(labels)} articles")
    print(f"Resuming from article index: {current_index}")
    
    return True

def save_labels():
    """Save current labels to a JSON file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/labels_{timestamp}.json"
    
    label_data = {
        'timestamp': timestamp,
        'total_articles': len(articles),
        'labeled_count': len(labels),
        'labels': labels
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(label_data, f, ensure_ascii=False, indent=2)
    
    print(f"Labels saved to {filename}")
    return filename

@app.route('/')
def index():
    """Main labeling interface"""
    global current_index
    
    if not articles:
        if not load_latest_articles():
            return "No articles found. Please run the data collection notebook first."
    
    # Try to load existing labels to resume progress
    if not labels:
        load_latest_labels()
    
    if current_index >= len(articles):
        return redirect(url_for('completed'))
    
    article = articles[current_index]
    progress = (current_index / len(articles)) * 100
    
    # Show resume message if we loaded existing labels
    resume_message = ""
    if len(labels) > 0 and current_index > 0:
        resume_message = f"Resumed from article {current_index + 1} (previously labeled {len(labels)} articles)"
    
    return render_template('labeling.html', 
                         article=article, 
                         current_index=current_index + 1,
                         total_articles=len(articles),
                         progress=progress,
                         resume_message=resume_message)

@app.route('/label', methods=['POST'])
def label_article():
    """Handle article labeling"""
    global current_index, labels
    
    data = request.get_json()
    label = data.get('label')  # 'advertisement' or 'news'
    
    if label in ['advertisement', 'news']:
        labels[current_index] = label
        current_index += 1
        
        # Auto-save every 10 labels
        if len(labels) % 10 == 0:
            save_labels()
    
    return jsonify({'success': True, 'next_index': current_index})

@app.route('/skip', methods=['POST'])
def skip_article():
    """Skip current article"""
    global current_index
    current_index += 1
    return jsonify({'success': True, 'next_index': current_index})

@app.route('/completed')
def completed():
    """Show completion summary"""
    filename = save_labels()
    
    stats = {
        'total_articles': len(articles),
        'labeled_count': len(labels),
        'advertisements': sum(1 for label in labels.values() if label == 'advertisement'),
        'news': sum(1 for label in labels.values() if label == 'news'),
        'labels_file': filename
    }
    
    return render_template('completed.html', stats=stats)

@app.route('/stats')
def stats():
    """API endpoint for labeling statistics"""
    if not articles:
        return jsonify({'error': 'No articles loaded'})
    
    stats = {
        'total_articles': len(articles),
        'labeled_count': len(labels),
        'current_index': current_index,
        'advertisements': sum(1 for label in labels.values() if label == 'advertisement'),
        'news': sum(1 for label in labels.values() if label == 'news'),
        'progress_percent': (current_index / len(articles)) * 100
    }
    
    return jsonify(stats)

if __name__ == '__main__':
    # Load articles and existing labels on startup
    load_latest_articles()
    load_latest_labels()
    app.run(debug=True, host='0.0.0.0', port=5001)
