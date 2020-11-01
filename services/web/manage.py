from flask.cli import FlaskGroup
from app import create_app
from redistimeseries.client import Client
import random
import time

app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)

    client.create('temperature')
    client.create('radiation')

    client.create('temp_avg_min')
    client.create('rad_avg_min')

    client.createrule('temperature', 'temp_avg_min', 'avg', 60)
    client.createrule('radiation', 'rad_avg_min', 'avg', 60)

    t = int(time.time())

    for i in range(1000):
        client.add('temperature', t, random.randint(1,100))
        client.add('radiation', t, random.randint(1,100))
        t += 1


if __name__ == "__main__":
    cli()