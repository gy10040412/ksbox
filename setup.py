from setuptools import setup, find_packages
 
setup(
    # 배포할 패키지의 이름을 적어줍니다. setup.py파일을 가지는 폴더 이름과 동일하게 합니다.
    name                = 'ksbox',
    # 배포할 패키지의 버전을 적어줍니다. 첫 등록이므로 0.1 또는 0.0.1을 사용합니다.
    version             = '0.4',
    # 배포할 패키지에 대한 설명을 작성합니다.
    description         = '3,4,5,8-sbox module ddt,lat,1-1, 1-2, 2-1 ddt & lat',
    # 배포하는 사람의 이름을 작성합니다.
    author              = 'KG',
    # 배포하는 사람의 메일주소를 작성합니다.
    author_email        = 'gi0412@kookmin.ac.kr',
    # 배포하는 패키지의 url을 적어줍니다. 보통 github 링크를 적습니다.
    url                 = 'https://github.com/gy10040412/ksbox',
    # 배포하는 패키지의 다운로드 url을 적어줍니다.
    download_url        = 'https://github.com/gy10040412/ksbox/archive/master.zip',
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적어줍니다. ex. install_requires= ['numpy', 'django']
    # 여기에 적어준 패키지는 현재 패키지를 install할때 함께 install됩니다.
    install_requires    =  ['colorama','numpy'],

    # 등록하고자 하는 패키지를 적는 곳입니다.
    # 우리는 find_packages 라이브러리를 이용하기 때문에 아래와 같이 적어줍니다.
    # 만약 제외하고자 하는 파일이 있다면 exclude에 적어줍니다.
    packages            = find_packages(exclude = []),
    # 패키지의 키워드를 적습니다.
    keywords            = ['pypi ksbox'],
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적습니다.
    python_requires     = '>=3',
    # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함시켜야 합니다.
    package_data        = {},
    # 위의 package_data에 대한 설정을 하였다면 zip_safe설정도 해주어야 합니다.
    zip_safe            = False,
    # PyPI에 등록될 메타 데이터를 설정합니다.
    # 이는 단순히 PyPI에 등록되는 메타 데이터일 뿐이고, 실제 빌드에는 영향을 주지 않습니다.
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
