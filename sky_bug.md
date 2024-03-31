# SKY Bug Tracking Software:

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


