from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
status = Table('status', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('httpStatus', VARCHAR(length=10)),
    Column('timestamp', DATETIME),
    Column('resource_id', INTEGER),
)

status = Table('status', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('httpstatus', String(length=10)),
    Column('timestamp', DateTime),
    Column('resource_id', Integer),
)

resource = Table('resource', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('url', VARCHAR(length=255)),
    Column('status', VARCHAR(length=15)),
)

resource = Table('resource', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=255)),
    Column('httpstatus', String(length=15)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['status'].columns['httpStatus'].drop()
    post_meta.tables['status'].columns['httpstatus'].create()
    pre_meta.tables['resource'].columns['status'].drop()
    post_meta.tables['resource'].columns['httpstatus'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['status'].columns['httpStatus'].create()
    post_meta.tables['status'].columns['httpstatus'].drop()
    pre_meta.tables['resource'].columns['status'].create()
    post_meta.tables['resource'].columns['httpstatus'].drop()
