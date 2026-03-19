# Qryma Python SDK

A Python SDK for the Qryma Search API, providing a simple and intuitive interface for accessing Qryma's powerful search capabilities.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install the Qryma Python SDK using pip:

```bash
pip install qryma-python
```

## Quick Start

```python
# To install: pip install qryma-python
from qryma import QrymaClient
client = QrymaClient("ak-********************")
response = client.search(
    query="artificial intelligence",
    start=0,
    safe=False,
    detail=False
)
print(response)
```

## Usage Examples

### Basic Search

```python
from qryma import QrymaClient
client = QrymaClient("ak-********************")
response = client.search("python programming")
print(response)
```

### Search with All Parameters

```python
from qryma import QrymaClient
client = QrymaClient("ak-********************")
response = client.search(query="machine learning tutorials", lang="en", start=0, safe=False, detail=False)
print(response)
```

### Custom Configuration

You can specify additional configuration options:

```python
from qryma import QrymaClient

client = QrymaClient(
    "ak-********************",
    base_url="https://custom.qryma.com",
    timeout=60
)

response = client.search("test query")
print(response)
```

### API Response Format

The `search()` method returns the raw API response in the following format:

```python
{
  "organic": [
    {
      "title": "Result Title",
      "date": "",
      "link": "https://example.com",
      "position": 1,
      "site_name": "Example.com",
      "snippet": "Description text..."
    }
  ]
}
```

**Field descriptions:**
- `title`: Search result title
- `date`: Publication date (if available)
- `link`: URL of the search result
- `position`: Position in the results list
- `site_name`: Name of the website
- `snippet`: Brief description or excerpt from the page

## API Reference

### QrymaClient

The main client class for interacting with the Qryma API.

#### Constructor

```python
QrymaClient(api_key: str, base_url: str = "https://search.qryma.com", timeout: int = 30)
```

- `api_key`: Your Qryma API key (required)
- `base_url`: Base URL for the API (default: `https://search.qryma.com`)
- `timeout`: Request timeout in seconds (default: 30)

#### Methods

##### search(query: str = "", lang: str = "", start: int = 0, safe: bool = False, detail: bool = False) -> Dict[str, Any]

Perform a search with the given query and return the raw API response.

**Parameters:**
- `query`: Search query string (optional)
- `lang`: Language code for search results (e.g., 'am' for Amharic, 'en' for English) (optional)
- `start`: Starting position of results (optional, default: 0)
- `safe`: Safe search mode: True or False (optional, default: False)
- `detail`: Include detailed results (optional, default: False)

**Returns:**
- Raw API response dictionary containing the search results

## Configuration

### Environment Variables

You can configure the API key using environment variables:

```bash
export QRYMA_API_KEY="your-api-key"
```

Then in your code:

```python
import os
from qryma import QrymaClient

client = QrymaClient(os.environ.get("QRYMA_API_KEY"))
```

## Error Handling

The SDK raises exceptions for API errors:

```python
from qryma import QrymaClient

try:
    client = QrymaClient("ak-********************")
    response = client.search("test query")
    results = response.get("organic", [])
    # Process results...

except Exception as e:
    if "timed out" in str(e):
        print("Network timeout error")
    elif "API request failed" in str(e):
        print("API error")
    else:
        print(f"Error: {e}")
```

Common error conditions:
- Invalid API key
- Rate limiting
- Network timeouts
- Invalid parameters

## Testing

The SDK includes a simple test file. To run the test:

1. First, replace the placeholder API key in `tests/test_search.py` with your actual API key
2. Then run the test:

```bash
python tests/test_search.py
```

## Contributing

Contributions are welcome! Please see our contributing guide for more information.

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please:

1. Check the [documentation](https://qryma.com/documentation.html)
2. Open an issue on GitHub
3. Contact support at support@qryma.com

## Changelog

### 0.1.0
- Basic search functionality
- Advanced search with SearchRequest
- Result extraction methods
- API status check
- Error handling
- Comprehensive data models
