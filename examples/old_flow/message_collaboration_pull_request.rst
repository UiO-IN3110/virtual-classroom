Dear {name}!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are receiving this e-mail because you are taking the course INF3331/INF4331
course and the next peer-review has now started. This peer-review is different to the previous one! You improve the code directly and
create a pull request (i.e. no Latex report). Please make sure that you read the instructions below.

You have been assigned to work with {{ group_names }} as part of
{{ group.team_name }}. Start by contacting your collaborators to organize
yourself. The email addresses of your collaborators are:

|    {{ filtered_group|map(attribute="email")|join("\n|    ") }}

You now have pull and fork access to three (or two) other students repositories.
Please create pull-requests for all these repositories.

The repositories to be reviewed are listed here: https://github.com/orgs/{{ classroom.org }}/teams/{{ group.team_name }}/repositories.

Instructions
~~~~~~~~~~~~
The instructions for this review can be downloaded here:

https://www.overleaf.com/read/schgbqcwnyng
