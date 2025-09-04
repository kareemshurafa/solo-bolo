from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def scrape_with_base_selenium(url):
    # Setup Chrome options
    options = Options()
    options.add_argument('--headless')  # Remove this to see the browser
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Create driver
    driver = webdriver.Chrome(options=options)
    
    try:
        # Navigate to the page
        driver.get(url)
        
        # Wait for page to load (simple approach)
        time.sleep(10)
        
        # Now you can extract data directly with Selenium
        title = driver.title
        print(f"Page title: {title}")
        
        # Find elements by various methods
        # By tag name
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Found {len(links)} links")
        
        # By class name
        try:
            job_cards = driver.find_elements(By.CLASS_NAME, "job-card")  # Example class
            print(f"Found {len(job_cards)} job cards")
        except:
            print("No job cards found with that class")
        
        # By CSS selector
        headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3")
        for heading in headings:  # First 5 headings
            print(f"Heading: {heading.text}")
        
        return driver  # Return driver if you want to do more operations
        
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return None

# Usage
driver = scrape_with_base_selenium("https://www.gradcracker.com/")
if driver:
    # Do more scraping if needed
    driver.quit()