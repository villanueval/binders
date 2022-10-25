# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['/home/$HOME/.openrefine/openrefine-3.6.2/refine', '-p', '{port}','-d','/home/$HOME/openrefine', '-i', '0.0.0.0'],
        'port': 3333,
        'timeout': 120,
        'launcher_entry': {
            'title': 'OpenRefine'
        },
    },
}
