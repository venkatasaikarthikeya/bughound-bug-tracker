# SKY Bug Tracking Software::

### Testing Goals:
1. Our testing will primarily be “black-box” with focus on correctly delivered functionality.
2. We will also conduct testing on 
  * security 
  * structure
  * usability
  * navigation
  * compatibility with multiple host configurations
3. And some technical testing we will learn in Unit 4 (data flows and anomalies)
---
### Software Features:
1. Bughound is a secure (authorized users and login required) web-based bug recording and tracking software products.
2. Key Features:
  * Using web browser, create, edit and update “bug” reports on multiple products
  * Store error report content in relational tables
  * Access error report content via SQL
  * Search for bugs on multiple fields 
  * Facilities to add, delete or update information on program, releases, functional areas, employees, more
---
### Web Pages:
1. SignUp
2. LogIn
3. Dashboard
4. Bug Report -> Create, Read, Update
5. Program -> Create, Read, Update (Program means the product in which we are reporting a bug)
6. User -> Create, Read, Update (Types: Admin, User)
7. Functional Area -> Create, Read, Update ()
---
### Bug Report fields:
1. id (Non Editable) -> Unique ID created by the backend and is not editable
2. Program with version (Drop down) -> Populated by `program` table. Product in which a bug needs to be reported
3. Report Type (Drop down) -> Populated on `Frontend` => [Coding Error, Design Issue, Suggestion, Documentation, Hardware, Query]
4. Severity (Drop down) -> Populated on `Frontend` => [Minor, Serious, Fatal]
5. Attachments (Button => File explorer) -> 
6. Problem Summary (Text Area) -> Populated on `Frontend`
7. Is reproducible? (Checkbox) -> Populated on `Frontend`
8. Problem & how to reproduce it (Text Area) -> Populated on `Frontend` 
9. Suggested Fix (Text Area) -> Populated on `Frontend`
10. Reported By (Drop down) -> Populated by `user` table. User who reported the bug.
11. Reported Date (Editable Text Field) -> Populated on `Frontend`

-------------------------Mandatory Fields end here-------------------------------

12. Functional Area (Drop down) -> Populated by `functional_area` table. Functional Area to which the bug belongs to.
13. Assigned to (Drop down) -> Populated by `user` table. User who is assigned with this bug.
14. Comments (Text Area) -> Populated on `Frontend`
15. Status (Drop down) -> Populated on `Frontend` => [Open, Resolved, Closed]
16. Priority (Drop down) -> Populated on `Frontend` => [Fix immediately, Fix as soon as possible, Fix before next milestone, Fix before release, Fix if possible, Optional]
17. Resolution & version (Drop Down) -> Populated on `Frontend` => [Pending, Fixed, Cannot be reproduced, Deferred, As designed, Withdrawn by reporter, Need more info, Disagree with suggestion, Duplicate]
18. Resolved By (Drop down) -> Populated by `user` table. User who resolved the bug.
19. Resolved Date (Editable Text Field) -> Populated on `Frontend`
18. Tested By (Drop down) -> Populated by `user` table. User who tested the resolution.
21. Tested Date (Editable Text Field) -> Populated on `Frontend`
22. Is deferred? (Checkbox) -> Populated on `Frontend`
---
### Schema:
#### User
```
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    user_role VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    UNIQUE (username)
);
```

#### Program
```
CREATE TABLE IF NOT EXISTS program(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    UNIQUE (name)
);
```

#### Functional Area
```
CREATE TABLE IF NOT EXISTS functional_area(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    UNIQUE (name)
);
```

#### Authorization 
```
CREATE TABLE IF NOT EXISTS authorization(
    user_id INTEGER primary key,
    jwt VARCHAR(512) NOT NULL,
    UNIQUE (jwt)
);
```

#### Bug Report
```
CREATE TABLE IF NOT EXISTS bug_report(
    id INTEGER PRIMARY KEY,
    pgm_id INTEGER NOT NULL,
    type VARCHAR(255) NOT NULL,
    severity VARCHAR(255) NOT NULL,
    summary VARCHAR(255) NOT NULL,
    is_reproducible BOOLEAN NOT NULL,
    description TEXT,
    suggested_fix TEXT,
    reported_by INTEGER NOT NULL,
    reported_on DATE,
    fa_id INTEGER,
    assigned_to INTEGER,
    comment TEXT,
    status VARCHAR(255),
    priority VARCHAR(255),
    resolution VARCHAR(255),
    resolved_by INTEGER,
    resolved_on DATE,
    tested_by INTEGER,
    tested_on DATE,
    is_deferred BOOLEAN
);
```