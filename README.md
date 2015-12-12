Command Line Interface for the Copado Webhook API
-------------
With this simple program, you will be able to start a Copado job and wait for its completion. The process will exit gracefully if the job was successfull or fail exit(1) otherwise.


## Installing
1. Download copado.py or clone this repo.
2. That's it.

## Prerequisites
* **Webhook URL** - review Webhook API  ```http://docs.copado.apiary.io```
* **API Key** - in order for the plugin to start the Job and check on the status (via the Copado Webhook API), it requires an API key. To create an api key, login to your Copado account and navigate to the Account Summary tab, and finally on the API Key sub-tab.
 
## Usage
1. Open your console.
2. Type: ```$>python copado.py -url URL```
3. In the ```URL``` parameter, paste the Webhook URL and make sure that Salesforce Ids and API Key parameter are set.

## Change Log
2015-Dec-10: First release
