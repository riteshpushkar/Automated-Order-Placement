## Bulk Purchase Automation with Selenium 

This Python script automates the process of bulk purchasing vignettes using Selenium WebDriver. It reads data from a CSV file containing information about the purchase orders and interacts with a web application to place the orders accordingly.

### Prerequisites 
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (chromedriver)

### Installation 
1. Install Python 3.x from python.org.
2. Install Selenium WebDriver using pip:

    ```
    pip install selenium
    ```

### Usage 
1. Download the Chrome WebDriver (chromedriver) compatible with your Chrome browser version from [here](https://chromedriver.chromium.org/downloads).
2. Update the `executable_path` variable in the script to point to the location of the chromedriver on your system.
3. Prepare a CSV file (`sample.csv`) with the following columns:
    - Country
    - Validity Begins
    - License Plate
    - Powered by (optional)
    - Type of Vignette
4. Run the script:

    ```
    python bulk_purchase.py
    ```

### Script Description 
- `csv_reader`: Reads the data from the provided CSV file.
- `order_placing`: Opens the purchase link, accepts cookies, and iterates through each row in the CSV to fill the purchase form.
- `WebDriver`: Utilizes Selenium WebDriver to automate web interactions.
- `time`: Includes time for waits and delays.
- `Keys`: Utilizes Keys for special keyboard interactions.
- `CSV`: Reads CSV file using the csv module.

### Disclaimer 
This script is provided as-is, without warranty of any kind. Use it at your own risk and ensure compliance with the terms of service of any website being automated.

### Author 
This script was authored by ritesh pushkar





