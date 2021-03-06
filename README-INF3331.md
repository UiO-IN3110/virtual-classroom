Virtual classroom for INF3331/INF4331
=====================================

Start of semester
-----------------

1. Ask students to fill out the Google Form https://docs.google.com/a/simula.no/forms/d/1JGSMC-9sRcuCanLF7MavHlGWVxuOjX-bwcIoyoM4yPE/edit
2. Make sure the response Google Spreadsheet has the ordering: *Timestamp, UiO-Username, Username on Github, Email Address, Course, Full name*
3. Download the student list with `cd virtual-classroom/src/scripts && ./get-info-google-spreadsheet.py`
4. Mark all participating students with an `x` in `Attendance/INF3331-students_base.txt`
4. Create a github repository and team for each student with 

   `cd virtual-classroom/src && ./start_group.py --i True --no-email --f Attendance/INF3331-students_base.txt`

   (If you choose `--email`, make sure to update the file `message_new_student.rst` beforehand).
   
   *Note*: This command will *not* overwrite existing repositories. This means that you can execute this command again if new students join the course.

Assignments
-----------
1. Each student has a repository with the name INF3331-*XYZ* where *XYZ* is the UiO-username. The solutions should be pushed into this repository.
2. If the assignment is a peer-reviewed assignment, see next section. Otherwise, proceed with the next step.
3. At the assignment deadline, all repositories can be downloaded with:

   `./start_group.py --get_repos True --get_repos_filepath assignment2_solutions --f Attendance/INF3331-students_base.txt`
   

Performing a peer-review
------------------------
1. Run `scripts/copy-attendance-file.py` and mark the students that take part of the group with `x` (this is usefull if some of the students hand in late).
2. Run `./start_group.py --m 3 --f Attendance/INF3331-2015-12-01_group1.txt`. This creates github teams of size 3 with access to 3 other student's repositories. Each group should review the student's solutions and push the reports to their repositories.

After review, delete all teams (and with it the access to their peers repositories) with:

3. `./start_group.py --e True`

End of semester
---------------

1. Backup all repositories. For example:

```bash
./start_group.py --university=UiO --course=INF3331 --get_repos=True --get_repos_filepath=../repos_2015
```

2. Delete all course repositories, teams and members (not owners) with:

```bash
./end_semester.py
```
