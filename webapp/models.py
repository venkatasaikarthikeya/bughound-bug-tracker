from django.db import models


# [1(low), 2(medium), 3(high)]
levels = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
]

# [Coding Error, Design Issue, Suggestion, Documentation, Hardware, Query]
report_types = [
    ('Select', 'Select'),
    ('Coding Error', 'Coding Error'),
    ('Design Issue', 'Design Issue'),
    ('Suggestion', 'Suggestion'),
    ('Documentation', 'Documentation'),
    ('Hardware', 'Hardware'),
    ('Query', 'Query')
]

# [Minor, Serious, Fatal]
severities = [
    ('Select', 'Select'),
    ('Minor', 'Minor'),
    ('Serious', 'Serious'),
    ('Fatal', 'Fatal')
]

# [Pending, Fixed, Cannot be reproduced, Deferred, As designed, Withdrawn by reporter, Need more info, Disagree with suggestion, Duplicate]
resolutions = [
    ('Select', 'Select'),
    ('Pending', 'Pending'),
    ('Fixed', 'Fixed'),
    ('Cannot be reproduced', 'Cannot be reproduced'),
    ('Deferred', 'Deferred'),
    ('As designed', 'As designed'),
    ('Withdrawn by reporter', 'Withdrawn by reporter'),
    ('Need more info', 'Need more info'),
    ('Disagree with suggestion', 'Disagree with suggestion'),
    ('Duplicate', 'Duplicate')
]

# [Open, Resolved, Closed]
statuses = [
    ('Select', 'Select'),
    ('Open', 'Open'),
    ('Resolved', 'Resolved'),
    ('Closed', 'Closed')
]

# [Fix immediately, Fix as soon as possible, Fix before next milestone, Fix before release, Fix if possible, Optional]
priorities = [
    ('Select', 'Select'),
    ('Fix immediately', 'Fix immediately'),
    ('Fix as soon as possible', 'Fix as soon as possible'),
    ('Fix before next milestone', 'Fix before next milestone'),
    ('Fix before release', 'Fix before release'),
    ('Fix if possible', 'Fix if possible'),
    ('Optional', 'Optional')
]


# Entity: Login
class Login(models.Model):
    name = models.CharField(max_length=200, default='', null=False, blank=False)

    def __str__(self):
        return self.name


# Entity: Program
class Program(models.Model):
    
    name = models.CharField(max_length=100)

    version = models.CharField(max_length=100)

    release = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '-' + self.version + '-' + self.release
    
# Entity: FunctionalArea
class FunctionalArea(models.Model):
    
    name = models.CharField(max_length=100)

    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.program.name + '-' + self.program.version + '-' + self.program.release + '-' + self.name
    
# Entity: Employee
class Employee(models.Model):

    name = models.CharField(max_length=100, default='')

    loginID = models.CharField(max_length=100, default='')

    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Entity: Report
class BugReport(models.Model):

    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    reportType = models.CharField(max_length=100, choices=report_types)

    severity = models.CharField(max_length=100, choices=severities)

    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)

    problemSummary = models.TextField()

    isReproducible = models.BooleanField()

    problem = models.TextField()

    suggestedFix = models.TextField()

    reportedBy = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reported')

    reportedOn = models.DateTimeField()

    # Optional Fields

    functionalArea = models.ForeignKey(FunctionalArea, on_delete=models.CASCADE, blank=True, null=True)

    assignedTo = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='assigned')

    comments = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=100, choices=statuses, default='Open')

    priority = models.CharField(max_length=100, choices=priorities, default='Optional')

    resolution = models.CharField(max_length=100, choices=resolutions, default='Pending')

    resolvedBy = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='resolved')

    resolvedOn = models.DateTimeField(blank=True, null=True)

    testedBy = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='tested')

    testedOn = models.DateTimeField(blank=True, null=True)

    isDeferred = models.BooleanField(default=False)

    def __str__(self):
        return self.program.name + '-' + self.reportType + '-' + self.problemSummary
    
    def fetch_attachment_name(self):
        return self.attachment.path.split('/')[-1]