#!/bin/bash

# Test script for local validation of the content generation

echo "Testing AI content generation locally..."

# Check which provider to use
if [ -z "$AI_PROVIDER" ]; then
    export AI_PROVIDER="anthropic"
fi

# Check if appropriate API key is set
if [ "$AI_PROVIDER" = "openai" ]; then
    if [ -z "$OPENAI_API_KEY" ]; then
        echo "Warning: OPENAI_API_KEY not set. Using mock mode."
        export OPENAI_API_KEY="test-key-for-validation"
    fi
else
    if [ -z "$ANTHROPIC_API_KEY" ]; then
        echo "Warning: ANTHROPIC_API_KEY not set. Using mock mode."
        export ANTHROPIC_API_KEY="test-key-for-validation"
    fi
fi

# Set test environment variables
export PROMPT="Generate a sample technology article about cloud computing"
export PAGE_TITLE="Cloud Computing Insights"
echo "Using AI Provider: $AI_PROVIDER"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the generation script
echo "Running content generation..."
python scripts/generate_content.py

# Check if output was created
if [ -f "public/index.html" ]; then
    echo "✅ Success! HTML file generated at public/index.html"
    echo "File size: $(wc -c < public/index.html) bytes"
    
    # Open in browser if on macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Opening in browser..."
        open public/index.html
    fi
else
    echo "❌ Error: HTML file not generated"
    exit 1
fi

# Cleanup
deactivate
echo "Test complete!"