{
    'name': 'Farmer Management',
    'version': '1.1',
    'author':'Akello Olga',
    'summary':'Farmer managemt software',
    'sequence':'10',
    'category': 'Productivity',
    'description': """A module to enable capturing of farmer details including the produce they have delivered.""",
    'depends':['base'],
    'data':[
        'security/security.xml',
        'security/ir.model.access.scv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
