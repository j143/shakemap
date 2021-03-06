from distutils.core import setup
import os.path
import versioneer


setup(name='shakemap',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='USGS Near-Real-Time Ground Motion Mapping',
      author='Bruce Worden, Mike Hearne, Eric Thompson',
      author_email='cbworden@usgs.gov,mhearne@usgs.gov,emthompson@usgs.gov',
      url='http://github.com/usgs/shakemap',
      packages=['shakemap',
                'shakemap.mapping',
                'shakemap.utils'],
      package_data={'shakemap': [os.path.join('tests', 'data', '*'),
                                 os.path.join('data', '*'),
                                 ]},
      scripts=['bin/sm_assemble', 'bin/sm_augment', 'bin/sm_contour',
               'bin/sm_model', 'bin/sm_profile'],
      )
