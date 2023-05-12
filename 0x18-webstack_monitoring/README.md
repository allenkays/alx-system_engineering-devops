# 0x18. Webstack monitoring
## Tasks
### 0. Sign up for Datadog and install datadog-agent 
For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent. 
    - Sign up for Datadog - use the US website of Datagog (.com)
    - Install datadog-agent on web-01
    - Create an application key
    - Copy-paste in Intranet user profile (here) the DataDog API key and the DataDog application key.
    - The server web-01 should be visible in Datadog under the host name XX-web-01
###  1. Monitor some metrics

    - Monitor that checks the number of read requests issued to the device per second.
    - Monitor that checks the number of write requests issued to the device per second.
### 2. Create a dashboard 
Dashboard with different metrics displayed in order to get a few different visualizations.

    - Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
    - 2-setup_datadog has the dashboard_id on the first line. 
Note: in order to get the id of your dashboard, you may need to use Datadog’s API

