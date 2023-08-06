__author__ = "Rafael Ferreira da Silva"

import logging

from sqlalchemy.exc import *

from pegaflow.db.admin.admin_loader import DBAdminError
from pegaflow.db.admin.versions.base_version import BaseVersion
from pegaflow.db.schema import *

DB_VERSION = 14

log = logging.getLogger(__name__)


class Version(BaseVersion):
    def __init__(self, connection):
        super().__init__(connection)

    def update(self, force=False):
        """."""
        log.debug("Updating to version %s" % DB_VERSION)
        try:
            Trigger.__table__.create(self.db.get_bind(), checkfirst=True)
        except (OperationalError, ProgrammingError):
            pass
        except Exception as e:
            self.db.rollback()
            raise DBAdminError(e)

    def downgrade(self, force=False):
        """."""
        log.debug("Downgrading from version %s" % DB_VERSION)
        # no downgrade is necessary
