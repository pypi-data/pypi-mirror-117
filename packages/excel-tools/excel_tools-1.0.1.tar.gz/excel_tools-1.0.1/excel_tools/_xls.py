# -*- coding: utf-8 -*-
import xlrd
from xlrd.sheet import Cell as XLCell

import os
from typing import Optional, Union, Generator, List, Any

from excel_tools.base_reader import ExcelBaseObject
from excel_tools.utils import get_column_letter, xls_float_correct, Cell


class XlsReader(ExcelBaseObject):
    def __init__(self, name: str, path: Optional[str] = '', sheet: Union[int, str, None] = 0):
        """
        xls读取类,仅可以读取 .xls格式的表格
        注意：所有对表的索引都从1,1开始。sheet:A1=(row=1,col=1)

        Args:
            name(str): 文件名
            path(str): 文件路径
            sheet(int,str): 需要读取的工作表(表名或表索引)
        """
        super(XlsReader, self).__init__(name, path)
        self._xl = xlrd.open_workbook(os.path.join(self._path, self._name), formatting_info=True)
        if isinstance(sheet, str):
            self._sheet = self._xl.sheet_by_name(sheet)
        elif isinstance(sheet, int):
            self._sheet = self._xl.sheet_by_index(sheet)
        else:
            self._sheet = self._xl.sheet_by_index(0)

    @property
    def sheet_name(self) -> str:
        """
        当前读取中的工作表名称

        Returns:
            工作表名称
        """
        return self._sheet.name

    def get_rows(self) -> Generator[List[XLCell], Any, None]:
        """ 获取所有列的单元格 """
        return self._sheet.get_rows()

    def get_row(self, rowx: int) -> List[XLCell]:
        """
        获取对应行的所有单元格

        Args:
            rowx: 行数

        Returns:
            返回这一行所有单元格
        """
        rowx = rowx - 1
        return [Cell(row=rowx, column=col + 1, worksheet=self._sheet, value=v.value, ctype=v.ctype)
                for col, v in enumerate(self._sheet.row(rowx))]

    def get_row_len(self, rowx: int) -> int:
        """
        获取对应行有效单元格的数量

        Args:
            rowx: 行数

        Returns:
            有效单元格数量
        """
        return len(self.get_row(rowx))

    def get_row_value(self, rowx: int, start_colx: Optional[int] = 0, end_colx: int = None) -> List[Any]:
        """
        获取表格内对应行中的所有单元格的数据

        Args:
            rowx: 行数
            start_colx: 左切片列数
            end_colx: 右切片列数

        Returns:
            返回这一行所有数据组成的列表
        """
        return [v.value for v in self.get_row(rowx)][start_colx:end_colx]

    def get_col(self, colx: int, start_rowx: Optional[int] = 0, end_rowx: Optional[int] = None) -> List[Cell]:
        """
        获取表格内对应列中的所有单元格

        Args:
            colx: 行数
            start_rowx: 左切片行数
            end_rowx: 右切片行数

        Returns:
            返回这一列所有数据组成的列表
        """
        return [Cell(worksheet=self._sheet, row=row + 1 + start_rowx, column=colx)
                for row, value in enumerate(self.get_col_value(colx, start_rowx, end_rowx))]

    def get_col_value(self, colx: int, start_rowx: Optional[int] = 0, end_rowx: Optional[int] = None) -> List[Any]:
        """
        获取表格内对应列中的所有单元格的数据

        Args:
            colx: 行数
            start_rowx: 左切片行数
            end_rowx: 右切片行数

        Returns:
            返回这一列所有数据组成的列表
        """
        return self._sheet.col_values(colx - 1, start_rowx, end_rowx)

    def get_cell(self, rowx, colx) -> Cell:
        """
        获取单元格

        Args:
            rowx: 列数
            colx: 行数

        Returns:
            行列对应单元格
        """
        cell = self._sheet.cell(rowx - 1, colx - 1)
        return Cell(worksheet=self._sheet, row=rowx, column=colx, value=cell.value, ctype=cell.ctype)

    def get_cell_value(self, rowx, colx) -> Any:
        """
        获取单元格内数据

        Args:
            rowx: 列数
            colx: 行数

        Returns:
            行列对应单元格中的数据
        """
        return self.get_cell(rowx, colx).value
