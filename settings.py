#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# 共通設定
# BUILDINGS_BASE_DIR: 読み込み元の建造物定義のディレクトリパス
# OUTPUT_DIR: 出力先ディレクトリパス
###############################################################################
BUILDINGS_BASE_DIR = 'C:/Program Files (x86)/Steam/steamapps/common/Stellaris/common/buildings'
OUTPUT_DIR = '.\output'

###############################################################################
# 布告解析用の正規表現のpattern
###############################################################################
BUILDINGS_START_PATTARN = r'^[a-zA-Z0-9]+.*{.*\n'
BUILDINGS_END_PATTARN = r'^}\n'
BUILDINGS_POSITION_PATTARN = r'^.*position_priority.*\n'
BUILDINGS_POSITION_PATTARN2 = r'^.*position_priority[ ]*=[ ]*100.*\n'
BUILDINGS_CATEGORY_PATTARN = r'^.*category.*\n'

###############################################################################
# 出力文字列
###############################################################################
ADD_PARAM = '	position_priority = {position}\n'
