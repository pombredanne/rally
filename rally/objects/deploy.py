# Copyright 2013: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally import db


class Deployment(object):
    """Represents a deployment object."""

    def __init__(self, deployment=None, **attributes):
        if deployment:
            self.deployment = deployment
        else:
            self.deployment = db.deployment_create(attributes)

    def __getitem__(self, key):
        return self.deployment[key]

    @staticmethod
    def get(uuid):
        return Deployment(db.deployment_get(uuid))

    @staticmethod
    def delete_by_uuid(uuid):
        db.deployment_delete(uuid)

    def _update(self, values):
        self.deployment = db.deployment_update(self.deployment['uuid'], values)

    def update_status(self, status):
        self._update({'status': status})

    def update_name(self, name):
        self._update({'name': name})

    def update_config(self, config):
        self._update({'config': config})

    def update_endpoint(self, endpoint):
        self._update({'endpoint': endpoint})

    def delete(self):
        db.deployment_delete(self.deployment['uuid'])
