#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import settings
import os
import re
import pathlib
import filecmp

def main():
	if not os.path.exists(settings.OUTPUT_DIR):
		os.mkdir(settings.OUTPUT_DIR)

	# 全ての建造物定義のファイルに対して実施
	files = pathlib.Path(settings.BUILDINGS_BASE_DIR).glob('*.txt')

	index = 0
	for file in files:
		# ファイルパス設定
		input_file = os.path.join(settings.BUILDINGS_BASE_DIR, file.name)
		output_file = os.path.join(settings.OUTPUT_DIR, file.name)
		write_buildings(input_file, output_file, index)
		index += 1

		# 出力内容が読み込み元と全く変わらなかったファイルについては不要なので削除する
		if filecmp.cmp(input_file, output_file, shallow=True):
			os.remove(output_file)


def write_buildings(input_file, output_file, index):
	# ファイル出力開始
	with open(output_file, 'w', encoding='utf-8') as wf:
		convert_buildings(input_file, wf, index)


def convert_buildings(input_file, wf, index):
	with open(input_file) as rf:
		# 読み込み中のデータ行が、個別の布告のパラメータを見ているかどうか
		is_parameter_line = False
		exist_position_param = False
		number = 0

		for line in rf:
			# 内部パラメータの行に入るまでは、そのまま読み込んだ行を出力する
			if not is_parameter_line:
				if re.fullmatch(settings.BUILDINGS_START_PATTARN, line):
					is_parameter_line = True
				wf.writelines(line)
				continue

			# 内部パラメータの行から抜ける時に、特定のパラメータの有無を確認し
			# 条件に一致すれば「position_priority = 数値」を追加で付与する
			if re.fullmatch(settings.BUILDINGS_END_PATTARN, line):
				if not exist_position_param:
					position = str(index * 100 + number)
					wf.writelines(settings.ADD_PARAM.format(position=position.strip()))
				wf.writelines(line)

				# 変数は初期化しておく
				is_parameter_line = False
				exist_position_param = False
				number += 1
				continue

			# 内部パラメータの行に入ったら、特定のパラメータがあるかどうかを調査する
			if re.fullmatch(settings.BUILDINGS_POSITION_PATTARN, line):
				exist_position_param = True
			wf.writelines(line)


if __name__ == "__main__":
	main()