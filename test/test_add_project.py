# -*- coding: utf-8 -*-
from model.project import Project
import pytest


def test_add_project(app, json_project, db):
    #app.session.login("administrator", "root")
    project = json_project
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
