#!/usr/bin/env python3
"""
Simple Qryma SDK test
"""

from qryma import QrymaClient


def test_search():
    """Test basic search functionality"""
    print("=== Testing Qryma SDK Search ===")

    # Replace this with your actual API Key
    api_key = "ak-********************"

    if api_key == "ak-********************":
        print("⚠️  Please replace the api_key with your actual API Key")
        print("   Modify the api_key variable in tests/test_search.py")
        return

    try:
        # Initialize the client
        client = QrymaClient(api_key)

        # Perform search
        query = "test"
        print(f"\nSearching for: '{query}'")
        response = client.search(query=query, safe=True)  # Enable safe search

        # Display results
        print(f"\n✓ Search successful!")

        if "organic" in response:
            results = response["organic"]
            print(f"Total {len(results)} results")

            # Show first 3 results
            for i, result in enumerate(results[:3], 1):
                print(f"\n{i}. {result.get('title', 'N/A')}")
                print(f"   Link: {result.get('link', 'N/A')}")
                snippet = result.get('snippet', '')
                if len(snippet) > 80:
                    snippet = snippet[:80] + "..."
                print(f"   Snippet: {snippet}")
        else:
            print("Response format:")
            print(response)

    except Exception as e:
        print(f"\n✗ Search failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_search()
