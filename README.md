# Player-Manager
> This project is an attempt to help manage and monitor the transition and growthof players in different academies nationally. The aim is to have a central management system for all football academies and their players. This is essential to help investors in planning and financing our local academies which will improve the general footballing in the country. Future implementations for the system include facial recognition, and player capabilities and market values throughout their journey.


![acakoro](ss/Screenshot%20(110).png)


[Visit site on render](https://fkf-mtaani.onrender.com/)


> The admiinstrator levels are divided into three and each is a member of the senior level. A senior level can view profiles of levels below by clicking the visit link
    >> Counties-registrar -> Academies-registrar -> Academy-manager

## Requirements
- python 3.7 +
- docker (optional)
## Installation
 - Clone this repository to your local machine and change into the directory
     ```
     git clone https://github.com/hawkinswinja/player-manager.git && cd player-manager
     ```
- Create and activate a virtual environment
    ```
    python -m venv virt && source virt/bin/activate

    # windows
    python -m venv virt && source virt\Scripts\activate
    ```
- Install dependencies listed in requirements.txt then cd into the project folder
    ```
    python -m pip install -r requirements.txt && cd fkf
    ```
- Run the migrations and create the superuser
    ```
    python manage.py makemigrations && python manage.py migrate && \
    python manage.py createsuperuser --name test --role test
    ```
- launch the server using gunicorn (ubuntu)
    ```
    gunicorn manager.wsgi:application
    ```
    - use waitress for windows 
    ```
    waitress-serve --listen=*:8000 manager.wsgi:application
    ```
>> alternatively if using docker, run the following command to build the image
```
docker build -t image-name:tag .
docker run -p 8000:8000 image-name:tag
```
- access the url at `127.0.0.1:8000`

## Areas to improve and contribute
This project could really use contributions. Feel free to fork the repo and make pull requests for improvements
- Limit registration to only the profile user i.e county admin can view players in academy but cannot register anew player
- Facial recognition to identify player basedd on their images
- Asynchronous database actions

&copy;hawkinswinja2023
