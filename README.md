# AI-Generated GitHub Pages

This repository demonstrates automated content generation and deployment to GitHub Pages using AI APIs (Anthropic Claude or OpenAI GPT).

## Features

- 🤖 Automated HTML content generation using Claude or GPT-4 APIs
- 🚀 Automatic deployment to GitHub Pages
- 📅 Scheduled weekly updates (configurable)
- 🎨 Professional, responsive HTML template
- 🔧 Manual trigger with custom prompts and AI provider selection
- 🔄 Support for both Anthropic Claude and OpenAI GPT models

## Setup

### 1. Enable GitHub Pages

1. Go to Settings → Pages
2. Under "Source", select "GitHub Actions"

### 2. Add API Keys

1. Go to Settings → Secrets and variables → Actions
2. Add one or both of the following secrets:
   - `ANTHROPIC_API_KEY` - Your Anthropic API key (for Claude)
   - `OPENAI_API_KEY` - Your OpenAI API key (for GPT-4)
3. You only need to add the key for the provider you plan to use

### 3. Trigger the Workflow

The workflow can be triggered in three ways:

1. **Push to main branch** - Automatically triggers on push
2. **Manual trigger** - Go to Actions → "Generate and Deploy AI Content to GitHub Pages" → Run workflow
3. **Scheduled** - Runs automatically every Monday at midnight UTC

## Manual Trigger Options

When manually triggering the workflow, you can customize:

- **AI Provider**: Choose between `anthropic` (Claude) or `openai` (GPT-4)
- **Custom prompt**: The prompt for content generation
- **Page title**: The title of the generated page

## Workflow Structure

```yaml
generate-content:
  - Checkout repository
  - Setup Python environment
  - Install dependencies
  - Generate HTML with selected AI API (Claude or GPT-4)
  - Upload as Pages artifact

deploy:
  - Deploy artifact to GitHub Pages
```

## Local Testing

To test the content generation locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export AI_PROVIDER="anthropic"  # or "openai"
export ANTHROPIC_API_KEY="your-anthropic-key"  # if using Anthropic
export OPENAI_API_KEY="your-openai-key"  # if using OpenAI
export PROMPT="Your custom prompt"
export PAGE_TITLE="Your Page Title"

# Run the script
python scripts/generate_content.py
```

The generated HTML will be saved to `public/index.html`.

## Customization

### Modify the HTML Template

Edit the `create_html_template()` function in `scripts/generate_content.py` to customize the design.

### Change Generation Schedule

Edit the cron expression in `.github/workflows/ai-generated-pages.yaml`:

```yaml
schedule:
  - cron: '0 0 * * 1'  # Weekly on Monday
```

### Adjust Claude Model Settings

Modify the model parameters in `generate_content_with_claude()`:

```python
model="claude-3-5-sonnet-20241022"
max_tokens=4000
temperature=0.7
```

## Security Notes

- Never commit your API key directly to the repository
- Use GitHub Secrets for sensitive information
- The workflow has minimal permissions (read contents, write pages)

## License

MIT