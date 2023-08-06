import psutil
from teska_monitor import db
import datetime
import time


def get_cpu_percent():
    pct = psutil.cpu_percent(interval=1)
    return pct


def get_cpu_temp():
    temp = psutil.sensors_temperatures()["coretemp"][0]
    return (temp.current)


def get_virtual_memory(option = "percent"):
    mem = psutil.virtual_memory()
    value = getattr(mem, option)
    return value


def get_disk_usage(option = "percent"):
    disk = psutil.disk_usage("/")
    value = getattr(disk, option)
    return value   



def get_boot_time():
    time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return time


def get_all(save=False, **kwargs):
    """Returns the current telemetry data
    :param save: If True, the telemetry data will be written into the database 
    :param kwargs: Additional params sent to db
    """
    
    output = {
       "cpu_usage": get_cpu_percent(),
       "cpu_temperature": get_cpu_temp(),
       "total_memory": get_virtual_memory(option= "total"),
       "virtual_memory": get_virtual_memory(),
       "disk_usage": get_disk_usage(),
       #"boot_time": get_boot_time()
    }

    # save if needed
    if save:
        db.save(**kwargs, **output)

    return output    


def interval(seconds=900, verbose=True, **kwargs):
    """Run the telemetry script at an interval.
    Calls get_all with save flag auto-activated at a given interval.
    This can be used to collect telemetry data on a client, as an 
    alternative to a Cron-Job.
    Usually, you want set the provider flag as well
    :param seconds: Interval length in seconds
    :param provider: Unique name of the client
    :param kwargs: Additional params sent to db
    """
    while True:
        # generate and save data
        data = get_all(save=True, **kwargs)
        if verbose:
            print(data)
        
        # wait specified interval
        time.sleep(seconds)


if __name__=="__main__":
    import fire
    fire.Fire({
        "all": get_all,
        "interval": interval,
        "cpu": get_cpu_percent,
        "mem": get_virtual_memory
    })


