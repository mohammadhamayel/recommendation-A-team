# recommendation-A-team
recommendation system based on data science

#Installation Steps

install php version 8.1 *** you can install xampp with mentioned php version ***
install composer latest version and make sure to add php path during its installation

copy .env.example and rename it to .env in the same location
add database information (database name, user-name and passwork) you can use xampp to open the phpmyadmin to show and make your database
add vairable named (TMDB_TOKEN="") at the end of .env file
go to the TMDB website and craete an account for you then take create a token for you and add it in the quots of the added vairable (TMDB_TOKEN)

#run the following commands in the root directory of the laravel project
composer install
php artisan config:cache
php artisan migrate
php artisan db:seed

#then to run the project every time you open the app run 
php artisan serve