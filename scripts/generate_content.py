#!/usr/bin/env python3
"""
Generate HTML content using AI APIs (Anthropic Claude or OpenAI GPT) and save it to GitHub Pages directory
"""

import os
import json
import sys
from datetime import datetime
from pathlib import Path
import markdown2
from jinja2 import Template

def create_html_template():
    """Create a professional HTML template"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }
        
        header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            animation: fadeInDown 1s ease;
        }
        
        .meta {
            font-size: 0.9rem;
            opacity: 0.9;
            animation: fadeInUp 1s ease 0.3s both;
        }
        
        main {
            padding: 3rem 2rem;
        }
        
        .content {
            animation: fadeIn 1s ease 0.5s both;
        }
        
        .content h2 {
            color: #667eea;
            margin: 2rem 0 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #667eea;
        }
        
        .content h3 {
            color: #764ba2;
            margin: 1.5rem 0 0.75rem;
        }
        
        .content p {
            margin-bottom: 1rem;
            text-align: justify;
        }
        
        .content ul, .content ol {
            margin: 1rem 0 1rem 2rem;
        }
        
        .content li {
            margin-bottom: 0.5rem;
        }
        
        .content code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        
        .content pre {
            background: #f4f4f4;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1rem 0;
        }
        
        .content blockquote {
            border-left: 4px solid #667eea;
            padding-left: 1rem;
            margin: 1rem 0;
            font-style: italic;
            color: #666;
        }
        
        footer {
            background: #f8f9fa;
            padding: 2rem;
            text-align: center;
            color: #666;
            border-top: 1px solid #dee2e6;
        }
        
        .badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 20px;
            font-size: 0.85rem;
            margin: 0.5rem 0.25rem;
        }
        
        .badge.openai {
            background: linear-gradient(135deg, #10a37f 0%, #1a7f64 100%);
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @media (max-width: 768px) {
            header h1 {
                font-size: 1.75rem;
            }
            
            main {
                padding: 2rem 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ title }}</h1>
            <div class="meta">
                <span class="badge">AI Generated</span>
                <span class="badge">{{ date }}</span>
                <span class="badge {{ 'openai' if provider == 'openai' else '' }}">Powered by {{ provider_name }}</span>
            </div>
        </header>
        
        <main>
            <div class="content">
                {{ content }}
            </div>
        </main>
        
        <footer>
            <p>This content was automatically generated using {{ provider_name }}</p>
            <p>Last updated: {{ timestamp }}</p>
        </footer>
    </div>
</body>
</html>"""

def generate_content_with_claude(prompt, api_key):
    """Generate content using Claude API"""
    import anthropic
    
    client = anthropic.Anthropic(api_key=api_key)
    
    enhanced_prompt = f"""
    {prompt}
    
    Please generate rich, engaging HTML content. Use a variety of HTML elements including:
    - Headings (h2, h3)
    - Paragraphs
    - Lists (ordered and unordered)
    - Code blocks where appropriate
    - Blockquotes for important points
    
    Make the content informative, well-structured, and visually appealing.
    Return only the HTML content without the outer HTML structure.
    """
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": enhanced_prompt
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error generating content with Claude: {e}", file=sys.stderr)
        raise

def generate_content_with_openai(prompt, api_key):
    """Generate content using OpenAI API"""
    from openai import OpenAI
    
    client = OpenAI(api_key=api_key)
    
    enhanced_prompt = f"""
    {prompt}
    
    Please generate rich, engaging HTML content. Use a variety of HTML elements including:
    - Headings (h2, h3)
    - Paragraphs
    - Lists (ordered and unordered)
    - Code blocks where appropriate
    - Blockquotes for important points
    
    Make the content informative, well-structured, and visually appealing.
    Return only the HTML content without the outer HTML structure.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that generates high-quality HTML content."
                },
                {
                    "role": "user",
                    "content": enhanced_prompt
                }
            ],
            max_tokens=4000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content with OpenAI: {e}", file=sys.stderr)
        raise

def main():
    # Get environment variables
    ai_provider = os.environ.get('AI_PROVIDER', 'anthropic').lower()
    prompt = os.environ.get('PROMPT', 'Generate an engaging HTML page about the latest in technology')
    page_title = os.environ.get('PAGE_TITLE', 'AI Generated Content')
    
    # Determine which API to use and get the appropriate key
    if ai_provider == 'openai':
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            print("Error: OPENAI_API_KEY not set", file=sys.stderr)
            sys.exit(1)
        provider_name = "OpenAI GPT-4"
        print(f"Using OpenAI API for content generation")
    else:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
            sys.exit(1)
        provider_name = "Claude"
        print(f"Using Anthropic Claude API for content generation")
    
    # Create output directory
    output_dir = Path('public')
    output_dir.mkdir(exist_ok=True)
    
    # Generate content based on provider
    print(f"Generating content with prompt: {prompt}")
    
    try:
        if ai_provider == 'openai':
            # Lazy import OpenAI only when needed
            from openai import OpenAI
            content = generate_content_with_openai(prompt, api_key)
        else:
            # Lazy import Anthropic only when needed
            import anthropic
            content = generate_content_with_claude(prompt, api_key)
    except ImportError as e:
        print(f"Error: Required package not installed for {ai_provider}. Please install it first.", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error generating content: {e}", file=sys.stderr)
        # Fallback content
        content = f"""
        <h2>Welcome to AI Generated Content</h2>
        <p>An error occurred while generating content. This is fallback content.</p>
        <p>Error details: {str(e)}</p>
        <h3>About This Page</h3>
        <p>This page is automatically generated using GitHub Actions and AI APIs.</p>
        """
    
    # Create HTML from template
    template = Template(create_html_template())
    html = template.render(
        title=page_title,
        content=content,
        date=datetime.now().strftime('%B %d, %Y'),
        timestamp=datetime.now().isoformat(),
        provider=ai_provider,
        provider_name=provider_name
    )
    
    # Save HTML file
    output_file = output_dir / 'index.html'
    output_file.write_text(html)
    print(f"Generated HTML saved to {output_file}")
    
    # Create a simple 404 page
    error_html = template.render(
        title="404 - Page Not Found",
        content="<h2>Page Not Found</h2><p>The page you're looking for doesn't exist.</p><p><a href='/'>Return to Home</a></p>",
        date=datetime.now().strftime('%B %d, %Y'),
        timestamp=datetime.now().isoformat(),
        provider=ai_provider,
        provider_name=provider_name
    )
    (output_dir / '404.html').write_text(error_html)
    
    # Create metadata file for tracking
    metadata = {
        'generated_at': datetime.now().isoformat(),
        'prompt': prompt,
        'title': page_title,
        'provider': ai_provider,
        'model': 'gpt-4o' if ai_provider == 'openai' else 'claude-3-5-sonnet-20241022'
    }
    (output_dir / 'metadata.json').write_text(json.dumps(metadata, indent=2))
    
    print("Content generation complete!")

if __name__ == '__main__':
    main()