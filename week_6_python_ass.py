# Import required libraries
import requests  # For sending HTTP requests
import os        # For creating folders and managing file paths
from urllib.parse import urlparse  # For extracting filename from URL

# Define the main function
def main():
    # Welcome message
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask the user to enter an image URL
    url = input("Please enter the image URL: ")

    try:
        # Create the folder 'Fetched_Images' if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Send a GET request to the URL
        response = requests.get(url, timeout=10)

        # Raise an error if the response status is not OK
        response.raise_for_status()

        # Extract the filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename is found, use a default name
        if not filename:
            filename = "downloaded_image.jpg"

        # Create the full path to save the image
        filepath = os.path.join("Fetched_Images", filename)

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        # Print success messages
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    # Handle network-related errors
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")

    # Handle other unexpected errors
    except Exception as e:
        print(f"✗ An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()