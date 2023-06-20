# Best network provider Dec 2021 Data Analysis  

In this project, I performed Data Analysis and get some finding from it, and come up with the particular conclusion. 

## Language and IDE Software Used 

- Language:- Python
- IDE:- Jupyter notebook

## Steps, I follow 
- ### Quetion
  Who is the best netwrok provider in Dec 2021, India
  ( Parameters:- Networks with speed more than average, Strong signal strength, More use of 4G technology )
 
- ### Data gathering 

  - Dataset which I used is from https://indiaai.gov.in/ , All India Crowdsourced Mobile Data Speed Measurement for December 2021 https://data.gov.in/resource/all-india-crowdsourced-mobile-data-speed-measurement-december-2021.

  - Initialling Dataset was in csv format

- ### Data Cleaning and Modification 

  - Remove null values from speed, signal strength columns
  - Change signal strength data type from object to float, so that arithmetic operations can be performed.  
  
- ### Removing the outliers 

  -   Remove outliers from speed columns
      Remove all the values in speed column which was outside the range of 144 kbps and 100000 kbps. (with the refference of Airtel experts 
      and wikipedia)

- ### Data Analysis and Findings
  
<img width="609" alt="Screenshot 2023-06-20 at 11 26 53 PM" src="https://github.com/himanshu1199/Best_network_provider_Dec_2021_Data_analysis/assets/130036773/c91ac0a4-a039-41e1-9ba5-370d8c54c505">
<img width="624" alt="Screenshot 2023-06-20 at 11 24 16 PM" src="https://github.com/himanshu1199/Best_network_provider_Dec_2021_Data_analysis/assets/130036773/6b6d0fdf-abcb-4a03-bbd0-23b943ee1fe0">
<img width="626" alt="Screenshot 2023-06-20 at 11 24 55 PM" src="https://github.com/himanshu1199/Best_network_provider_Dec_2021_Data_analysis/assets/130036773/8620208a-d6bb-4e72-8a17-0c839502f674">
<img width="629" alt="Screenshot 2023-06-20 at 11 25 21 PM" src="https://github.com/himanshu1199/Best_network_provider_Dec_2021_Data_analysis/assets/130036773/4c3100d7-74f1-4765-b29d-986719063e7d">
