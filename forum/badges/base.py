import re
from string import lower

from django.core.exceptions import MultipleObjectsReturned
from django.db.models.signals import post_save

from forum.models import Badge, Node, Action
from forum.actions import AwardAction

import logging

installed = dict([(b.cls, b) for b in Badge.objects.all()])

class BadgesMeta(type):
    by_class = {}
    by_id = {}

    def __new__(mcs, name, bases, dic):
        badge = type.__new__(mcs, name, bases, dic)

        if not dic.get('abstract', False):
            if not name in installed:
                ondb = Badge(cls=name, type=dic.get('type', Badge.BRONZE))
                ondb.save()
            else:
                ondb = installed[name]

            badge.ondb = ondb.id

            inst = badge()

            def hook(action, new):
                user = inst.award_to(action)

                if user:
                    badge.award(user, action, badge.award_once)

            for action in badge.listen_to:
                action.hook(hook)

            BadgesMeta.by_class[name] = inst
            BadgesMeta.by_id[ondb.id] = inst

        return badge

class AbstractBadge(object):
    __metaclass__ = BadgesMeta

    abstract = True
    award_once = False

    @property
    def name(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @classmethod
    def award(cls, user, action, once=False):
        db_object = Badge.objects.get(id=cls.ondb)
        try:
            if once:
                node = None
                awarded = AwardAction.get_for(user, db_object)
            else:
                node = action.node
                awarded = AwardAction.get_for(user, db_object, node)

            trigger = isinstance(action, Action) and action or None

            if not awarded:
                AwardAction(user=user, node=node).save(data=dict(badge=db_object, trigger=trigger))
        except MultipleObjectsReturned:
            if node:
                logging.error('Found multiple %s badges awarded for user %s (%s)' % (cls.name, user.username, user.id))
            else:
                logging.error('Found multiple %s badges awarded for user %s (%s) and node %s' % (cls.name, user.username, user.id, node.id))