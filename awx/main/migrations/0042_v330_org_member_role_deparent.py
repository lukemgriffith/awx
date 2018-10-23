# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-02 13:47
from __future__ import unicode_literals

import awx.main.fields
from django.db import migrations
import django.db.models.deletion
from awx.main.migrations._rbac import rebuild_role_hierarchy


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_v330_update_oauth_refreshtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='member_role',
            field=awx.main.fields.ImplicitRoleField(editable=False, null=b'True', on_delete=django.db.models.deletion.CASCADE, parent_role=[b'admin_role'], related_name='+', to='main.Role'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='read_role',
            field=awx.main.fields.ImplicitRoleField(editable=False, null=b'True', on_delete=django.db.models.deletion.CASCADE, parent_role=[b'member_role', b'auditor_role', b'execute_role', b'project_admin_role', b'inventory_admin_role', b'workflow_admin_role', b'notification_admin_role', b'credential_admin_role', b'job_template_admin_role'], related_name='+', to='main.Role'),
        ),
        migrations.RunPython(rebuild_role_hierarchy),
    ]
