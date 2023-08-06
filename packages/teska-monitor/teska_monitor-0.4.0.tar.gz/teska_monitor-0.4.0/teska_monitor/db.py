import os
from datetime import datetime as dt
from datetime import timedelta as td
from dateutil.parser import parse

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATAPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))


class TelemetryType(Base):
    __tablename__ = 'telemetry_type'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    alias = sa.Column(sa.String, nullable=True)

    data = relationship('Telemetry', back_populates='type', cascade='all, delete')


class Telemetry(Base):
    __tablename__ = 'telemetry'

    id = sa.Column(sa.Integer, primary_key=True)
    value = sa.Column(sa.Numeric, nullable=False)
    type_id = sa.Column(sa.Integer, sa.ForeignKey('telemetry_type.id'), nullable=False)

    type = relationship('TelemetryType', back_populates='data')
    set = relationship('TelemetrySet', secondary='telemetry_set_records', back_populates='data')


class TelemetrySet(Base):
    __tablename__ = 'telemetry_set'
    __table_args__ = (
        sa.UniqueConstraint('dtime', 'provider'),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    dtime = sa.Column(sa.DateTime, default=dt.now)
    provider = sa.Column(sa.String)

    data = relationship('Telemetry', secondary='telemetry_set_records', back_populates='set', cascade='all, delete')

    def as_dict(self, deep=True):
        out = {
            'dtime': self.dtime,
            'provider': self.provider
        }

        if deep:
            out.update({tel.type.name:float(tel.value) for tel in self.data})

        return out        


class TelemetrySetRecords(Base):
    __tablename__ = 'telemetry_set_records'

    set_id = sa.Column(sa.Integer, sa.ForeignKey('telemetry_set.id'), primary_key=True)
    tel_id = sa.Column(sa.BigInteger, sa.ForeignKey('telemetry.id'), primary_key=True)


def connect(connection='data.db', mode='engine'):
    """
    Establish a connection to the database holding telemetry information.
    The connection can be returned as a raw engine object or as a SQLAlchemy
    Session.
    """
    # check if sqlite or something else
    if connection.endswith('.db'):
        path = os.path.join(DATAPATH, connection)
        connection = f"sqlite:///{path}"
    
    # create the engine
    engine = create_engine(connection)

    # return engine or session
    if mode.lower() == 'engine':
        return engine
    elif mode.lower() == 'session':
        Session = sessionmaker(bind=engine)
        return Session()


def save(connection='data.db', provider='localhost', dtime=dt.now, commit=True, **kwargs):
    """Save a set of telementry values to the database.
    The kwargs will be parsed as a list of types:values that make up the 
    telemetry set to be stored. The save method will check each kwargs key 
    (telemetry type) for existance in the database and create a new type if it
    is missing. 
    :param connection: sqlite filename or database connection string
    :param provider: if more than one provider is active, use this name to
        differentiate them.
    :param dtime: the datetime of the telemetry entry, if saving is not
        performed in real-time. Dafaults to current time.
    :param commit: if commit is False, the Model is returned and not persisted to
        the database.
    :param kwargs: telemetry type - value paris 
    """
    # first get a connection
    session = connect(connection=connection, mode='session')

    # create the set
    telset = TelemetrySet(provider=provider, dtime=dtime())

    # append each telemetry value
    for type_name, value in kwargs.items():
        # check if type exists
        with session.no_autoflush:
            teltype = session.query(TelemetryType).filter(TelemetryType.name==type_name).first()

        # if it does not exist, create it
        if teltype is None:
            teltype = TelemetryType(name=type_name)
        
        # create the telemetry entry
        tel = Telemetry(value=value, type=teltype)

        # append
        telset.data.append(tel)

    if commit:
        try:
            session.add(telset)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
    else:
        return telset


def read(connection='data.db', provider=None, since=None, start=None, end=None, as_dict=True):
    """Read telemetry data from the database
    Read the connected database by specifieing several filter options.
    :param connection: sqlite filename or database connection string
    :param provider: if given, filter by the given provider
    :param since: if given, include only Telemetry newer than given seconds
    :param start: if given, do not include telemetry before this date
    :param end: if given, do not include telemetry after this date
    :param as_dict: if True, return dictionaries, else Model instances
    """
    # first get a session
    session = connect(connection=connection, mode='session')

    # build the base query
    query = session.query(TelemetrySet)

    # add the different filters
    
    # provider
    if provider is not None:
        if '*' in provider:
            provider = provider.replace('*', '%')
        if '%' in provider:
            query = query.filter(TelemetrySet.provider.like(provider))
        else:
            query = query.filter(TelemetrySet.provider == provider)
    
    # since
    if since is not None:
        start = dt.now() - td(seconds=since)
        end = None
    
    # start and end
    if start is not None:
        if isinstance(start, str):
            start = parse(start)
        query = query.filter(TelemetrySet.dtime >= start)
    if end is not None:
        if isinstance(end, str):
            end = parse(end)
        query = query.filter(TelemetrySet.dtime <= end)
    
    # return
    if as_dict:
        return [tel.as_dict(deep=True) for tel in query.all()]
    else:
        return query.all()


def install(connection='data.db', drop=False):
    """Install the tables into the database.
    If connection is a .db file, a local SQLite database will be used. Otherwise
    connection has to be a connection string to a database server.
    :param connection: sqlite filename or database connection string
    :param drop: if true, any existing table will be dropped first
    """
    # get an engine
    engine = connect(connection=connection, mode='engine')
    
    # drop first if needed
    if drop:
        Base.metadata.drop_all(bind=engine)

    # install tables
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    import fire
    fire.Fire({
        'save': save,
        'read': read,
        'get': read,
        'install': install
    })
