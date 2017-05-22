import datetime

from skf.database import db
from skf.database.project_sprints import project_sprints 
from skf.database.groupmembers import groupmembers
from skf.api.security import val_num, val_alpha, val_alpha_num

def update_sprint(project_id, user_id, data):
    sprint = project_sprints.query.filter(project_sprints.projectID == project_id).one()
    sprint.sprintName = data.get('name')
    sprint.sprintDesc = data.get('description')
    db.session.add(sprint) 
    db.session.commit()


def new_sprint(user_id, data):
    sprintName = data.get('name')
    sprintDesc = data.get('description')
    projectID = data.get('projectID')
    val_alpha_num(sprintName)
    val_alpha_num(sprintDesc)
    userID = user_id
    groupmember = groupmembers.query.filter(groupmembers.userID == userID).one()
    ownerID = groupmember.ownerID
    groupID = groupmember.groupID
    sprint = project_sprints(sprintName, sprintDesc, groupID, projectID)
    db.session.add(sprint)
    db.session.commit()


def delete_sprint(sprint_id, user_id):
    sprint = (project_sprints.query.filter(project_sprints.sprintID == sprint_id).one())
    db.session.delete(sprint)
    db.session.commit()
