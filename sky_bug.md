# SKY Bug Tracking Software::

#### Testing Goals:
1. Our testing will primarily be “black-box” with focus on correctly delivered functionality.
2. We will also conduct testing on 
  * security 
  * structure
  * usability
  * navigation
  * compatibility with multiple host configurations
3. And some technical testing we will learn in Unit 4 (data flows and anomalies)


#### Software Features:
1. Bughound is a secure (authorized users and login required) web-based bug recording and tracking software products.
2. Key Features:
  * Using web browser, create, edit and update “bug” reports on multiple products
  * Store error report content in relational tables
  * Access error report content via SQL
  * Search for bugs on multiple fields 
  * Facilities to add, delete or update information on program, releases, functional areas, employees, more


#### Web Pages:
1. SignUp
2. LogIn
3. Dashboard
4. Bug Report -> Create, Read, Update
5. Program -> Create, Read, Update (Program means the product in which we are reporting a bug)
6. User -> Create, Read, Update (Types: Admin, User)
7. Functional Area -> Create, Read, Update ()



#### Bug Report fields:
1. Report ID (Non editable Text field) -> Unique ID created by the backend and is not editable
2. Program & version (Drop down) -> Refers to any of the existing products in which a bug needs to be reported
3. Report Type (Drop down) -> Hardcoding on Front-end
  * Values - [Coding Error, Design Issue, Suggestion, Documentation, Hardware, Query]
4. Severity (Drop down) -> Hardcoding on Front-end
  * Values - [Minor, Serious, Fatal]
5. Attachments (Button = File explorer) -> (Just store a field in database) to store S3 link or something (Can be discussed later. Not a priority at the moment)
6. Problem Summary (Text Area) -> Will be entered by the user in the front-end
7. Is reproducible? (Checkbox) -> Boolean
8. Problem & how to reproduce it (Text Area) -> Will be entered by the user in the front-end    
9. Suggested Fix (Text Area) -> Will be entered by the user in the front-end
10. Reported By (Drop down) -> Show list of all users names in drop down
11. Date (Editable Text Field) -> text. (YYYY/MM/DD)

-------------------------Mandatory Fields end here-------------------------------

12. Functional Area (Drop down) -> 
13. Assigned to (Drop down) -> 
14. Comments (Text Area) -> 
15. Status (Drop Down) -> Values[Open, Closed, Resolved]
16. Priority (Assigned by Manager) -> Values[Fix immediately, Fix as soon as possible, Fix before next milestone, Fix before release, Fix if possible, Optional]
17. Resolution & version (Drop Down) -> Values[]
18. Resolved By (Drop down) -> Users
19. Resolved Date ()
18. Tested By (Drop down) -> User
21. Tested Date ()



BugReport(
    id,
    program_id (refers to ID in Program Table),
    report_type,
    severity,
    attachment,
    problem_summary,
    is_reproducible,
    description,
    suggested_fix,
    reported_by (refers to ID in User Table),
    reported_date,
    functional_area_id (refers to ID in Functional Area Table),
    assigned_to (refers to ID in User Table),
    comment,
    status,
    priority,
    resolution,
    resolved_by (refers to ID in User Table),
    resolved_date,
    tested_by (refers to ID in User Table),
    tested_date
)














#### Tables

1. User (ID, )



























