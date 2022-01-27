
from jinja2 import Environment, FileSystemLoader
import os
import sys

with open("main.html.j2", "r") as f:
    dashboardHtmlString = f.read()
with open("email-schedule.html.j2", "r") as f:
    emailScheduleHtmlString = f.read()
with open("email-calendar.html.j2", "r") as f:
    emailCalendarHtmlString = f.read()
with open("analytics-email.html.j2", "r") as f:
    analyticsEmailHtmlString = f.read()
with open("permissions-add-user.html.j2", "r") as f:
    permissionsAddUserHtmlString = f.read()
with open("permissions-view-edit-users.html.j2", "r") as f:
    permissionsViewEditUsersHtmlString = f.read()

data = {
    "name": "Jake Boes"
}

load = FileSystemLoader(".")
dashboardTemplate = Environment(loader=load).from_string(dashboardHtmlString)
dashboardHtmlOutput = dashboardTemplate.render(**data)

schedulerTemplate = Environment(loader=load).from_string(emailScheduleHtmlString)
emailSchedulerHtmlOutput = schedulerTemplate.render(**data)

calendarTemplate = Environment(loader=load).from_string(emailCalendarHtmlString)
emailCalendarHtmlOutput = calendarTemplate.render(**data)

analyticsEmailTemplate = Environment(loader=load).from_string(analyticsEmailHtmlString)
analyticsEmailHtmlOutput = analyticsEmailTemplate.render(**data)

permissionsAddUserTemplate = Environment(loader=load).from_string(permissionsAddUserHtmlString)
permissionsAddUserHtmlOutput = permissionsAddUserTemplate.render(**data)

permissionsViewEditUsersTemplate = Environment(loader=load).from_string(permissionsViewEditUsersHtmlString)
permissionsViewEditUsersHtmlOutput = permissionsViewEditUsersTemplate.render(**data)

with open("renderedExample.html", "w") as f:
    f.write(dashboardHtmlOutput)
with open("renderedExample2.html", "w") as f:
    f.write(emailSchedulerHtmlOutput)
with open("renderedExample3.html", "w") as f:
    f.write(emailCalendarHtmlOutput)
with open("renderedExample4.html", "w") as f:
    f.write(analyticsEmailHtmlOutput)
with open("renderedExample5.html", "w") as f:
    f.write(permissionsAddUserHtmlOutput)
with open("renderedExample6.html", "w") as f:
    f.write(permissionsViewEditUsersHtmlOutput)
