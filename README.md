LunchUp - WAD2 Team Project

Live demo: http://lunchup12.pythonanywhere.com

Instructions:
<ol>
    <li>python manage.py syncdb (make sure super user does not clash with users in pop. script)</li>
    <li>python manage.py makemigrations</li>
    <li>python manage.py migrate</li>
    <li>python populate_lunchup.py</li>
</ol>
Matchmaking function can be executed by going to /magic/

Additional info:
<ul>
    <li>Users must register with a university email</li>
    <li>All UK uni email domains are supported</li>
    <li>Support for all uni email domains can be added by modifying populate_lunchup.py to populate more data</li>
    <li>We got the database from https://github.com/Hipo/university-domains-list/</li>
</ul>

Team members:
Omar Tufail
Justinas Bikulcius
Rajeevan Vijayakumar
Blair William Aitcheson