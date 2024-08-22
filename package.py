name = 'qumulo_fs_walk'

version = '1.0.0.hh.1.0.1'

authors = [
    'Qumulo',
]

description = '''Qumulo file system walk and actions'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']

requires = [
    "qumulo_api",
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_QUMULO_FS_WALK_ROOT = '{root}'
    env.PYTHONPATH.append('{root}/src/python')


build_command = 'rez python {root}/rez_build.py'
uuid = 'repository.qumulo-filesystem-walk'
