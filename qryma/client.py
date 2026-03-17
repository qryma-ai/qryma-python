"""Qryma API Client implementation."""

import requests
from typing import Optional, Dict, Any
from .version import __version__


class QrymaClient:
    """
    Client for interacting with the Qryma Search API.

    Args:
        api_key: Qryma API key for authentication
        base_url: Base URL for the Qryma API (default: https://search.qryma.com)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://search.qryma.com",
        timeout: int = 30
    ):
        if not api_key or not api_key.strip():
            raise ValueError("API key must be provided")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = {
            "X-Api-Key": api_key,
            "Content-Type": "application/json",
            "User-Agent": f"qryma-python/{__version__}"
        }

    def search(
        self,
        query: str = "",
        lang: str = "",
        start: int = 0,
        safe: bool = False,
        detail: bool = False
    ) -> Dict[str, Any]:
        """
        Perform a search using the Qryma API.

        Args:
            query: The search query string (optional)
            lang: Language code for search results (e.g., 'am' for Amharic, 'en' for English) (optional)
            start: Starting position of results (default: 0)
            safe: Safe search mode: True , False (default: False)
            detail: Whether to include detailed results (default: False)

        Returns:
            Raw API response dictionary containing the search results

        Raises:
            requests.exceptions.RequestException: If there's an error with the request
            ValueError: If the API response is invalid
        """
        url = f"{self.base_url}/api/web"
        payload = {
            "query": query,
            "lang": lang,
            "start": start,
            "safe": safe,
            "detail": detail
        }

        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            data = response.json()
            return data

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing search: {str(e)}")
