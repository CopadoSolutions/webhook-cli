Command Line Interface for the Copado Webhook API
-------------
With this simple program, you will be able to start a Copado job and wait for its completion. The process will exit gracefully if the job was successfull or fail exit(1) otherwise.


## Installing
Download copado.py or clone this repo.

```curl https://raw.githubusercontent.com/CopadoSolutions/webhook-cli/master/copado.py --out copado.py```

```chmod +x copado.py```

## Prerequisites
* **Webhook URL** - review Webhook API  ```http://docs.copado.apiary.io```
* **API Key** - in order for the plugin to start the Job and check on the status (via the Copado Webhook API), it requires an API key. To create an api key, login to your Copado account and navigate to the Account Summary tab, and finally on the API Key sub-tab use the button "create/reset".
 
## Usage
1. Open your console.
2. Type: ```$>./copado.py --url URL```
3. In the ```URL``` parameter, paste the Webhook URL and make sure that Salesforce Ids and API Key parameter are set.

## Example
```./copado.py --url https://copado-eu.herokuapp.com/json/v1/webhook/gitSnapshot/a10f2000006O84F?api_key=XXXXXXXXXX```

## Change Log
* 2017-Jan-21: Clean up log messages and command line parameter
* 2015-Dec-10: First release
