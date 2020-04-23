# get the config object
c = get_config()
c.NotebookApp.password = 'sha1:6f9cf44b5eec3c0e4b645a6fb4044ebf00c86842'
c.Spawner.notebook_dir = '~/'
c.NotebookApp.certfile = '/root/fullchain.pem'
c.NotebookApp.keyfile = '/root/privkey.pem'
c.NotebookApp.ip = '0.0.0.0'
