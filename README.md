# Facebook Group Crawler with LINE Notify Integration

This project provides a simple yet effective solution for monitoring specific Facebook groups for posts containing user-defined keywords and sending instant notifications through LINE Notify. Stay updated with the latest posts about housing or any other topics of interest without manually checking the group.
## Setup Instructions

### Step 1: ChromeDriver Installation

* Download `ChromeDriver` from [ChromeDriver - WebDriver for Chrome](https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-tw). Make sure to select the version that matches your Chrome browser's version.

### Step 2: Configuration

* Open the script and set your Facebook credentials and the target group URL:
   ```python
   username = 'your account'
   password = 'your password'
   spec_url = 'specific facebook group url'
   
### Step 3: Define Keywords

* In the `keywords = []` array, add the keywords you're interested in. For housing, you might use:
   ```python
   keywords = ["租屋", "租房", "套房", "雅房", "室友", "分租", "台電", "獨立電表", "出租", "租客"]
* Optionally, add any keywords you want to exclude in the specified section of the script.

### Step 4: LINE Notify Setup

* Set up LINE Notify by following the instructions [here](https://www.cc.ntu.edu.tw/chinese/epaper/0031/20220920_006204.html) to obtain your token.
* * Insert your token in the script:
   ```python
   headers = {
       "Authorization": "Bearer" + "your token",
       "Content-Type": "application/x-www-form-urlencoded"
   }


### Usage
After completing the setup, run the script. You will receive notifications via LINE Notify when a new post in your specified Facebook group matches any of your defined keywords.

