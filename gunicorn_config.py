import multiprocessing

bind = "127.0.0.1:5005"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 120
keepalive = 5

accesslog = "-"
errorlog = "-"
loglevel = "info"

proc_name = "kalenderia-web"
