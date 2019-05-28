#!/usr/bin/python
# -*- coding: utf-8 -*-
import responses
import unittest

from slacker import Users
from slacker.utilities import get_api_url


class TestUsers(unittest.TestCase):
    @responses.activate
    def test_user_list_supports_pagination(self):
        response = {
            "ok": True,
            "members": [{
                    "id": "id1",
                    "team_id": "team_id1",
                    "name": "vasya",
                    "deleted": False,
                    "real_name": "Vasya Pupkin",
                    "profile": {
                        "display_name": "vasya",
                        "email": "v.pupkin@email.com",
                        "team": "team_id1"
                    },
                    "is_admin": True
                },
                {
                    "id": "id2",
                    "team_id": "team_id2",
                    "name": "petya",
                    "deleted": False,
                    "real_name": "Petya Pupkin",
                    "profile": {
                        "real_name": "Petya Pupkin",
                        "email": "p.pupkin@email.com",
                        "team": "team_id2"
                    },
                    "response_metadata": {
                        "next_cursor": ""
                    }
                }]
        }

        responses.add(
            responses.GET,
            get_api_url('users.list?presence=0&cursor=next_cursor1'),
            json=response,
            status=200
        )
        users = Users()
        users_list = users.list(cursor='next_cursor1')
        self.assertEqual(len(users_list.body['members']), 2)

    @responses.activate
    def test_user_list_supports_pagination(self):
        response = {
            "ok": True,
            "members": [{
                "id": "id1",
                "team_id": "team_id1",
                "name": "vasya",
                "deleted": False,
                "real_name": "Vasya Pupkin",
                "profile": {
                    "display_name": "vasya",
                    "email": "v.pupkin@email.com",
                    "team": "team_id1"
                },
                "is_admin": True
            },
                {
                    "id": "id2",
                    "team_id": "team_id2",
                    "name": "petya",
                    "deleted": False,
                    "real_name": "Petya Pupkin",
                    "profile": {
                        "real_name": "Petya Pupkin",
                        "email": "p.pupkin@email.com",
                        "team": "team_id2"
                    }
                }]
        }

        responses.add(
            responses.GET,
            get_api_url('users.list?presence=0'),
            json=response,
            status=200
        )
        users = Users()
        users_list = users.list()
        self.assertEqual(len(users_list.body['members']), 2)
