# import os
#
# class Config(object):
#
#
#     # 데이터베이스 설정
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:It12345!@aurora-db.cluster-cmg5rcfhykpl.ap-northeast-2.rds.amazonaws.com/sports'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False






import os

class Config(object):


    # 데이터베이스 설정
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1111@localhost/sports'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 추가적인 설정이 필요할 경우 이곳에 추가


