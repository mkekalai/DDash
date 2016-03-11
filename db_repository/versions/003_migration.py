from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
query_result = Table('query_result', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('httpStatus', VARCHAR(length=10)),
    Column('timestamp', DATETIME),
    Column('webresource_id', INTEGER),
)

web_resource = Table('web_resource', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('url', VARCHAR(length=255)),
)

resource = Table('resource', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=255)),
)

status = Table('status', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('httpStatus', String(length=10)),
    Column('timestamp', DateTime),
    Column('resource_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['query_result'].drop()
    pre_meta.tables['web_resource'].drop()
    post_meta.tables['resource'].create()
    post_meta.tables['status'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['query_result'].create()
    pre_meta.tables['web_resource'].create()
    post_meta.tables['resource'].drop()
    post_meta.tables['status'].drop()
