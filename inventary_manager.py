from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from os import path
import sys

from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(path.join(path.dirname('__file__'),"main.ui"))

import sqlite3

x=0
idx = 2

class Main(QMainWindow,FORM_CLASS):
	"""docstring for """
	def __init__(self, parent=None):

		super(Main, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.Handle_Buttons()
	  
	def Handle_Buttons(self):
		self.refresh_btn.clicked.connect(self.GET_DATA)
		self.search_btn.clicked.connect(self.SEARCH)
		self.check_btn.clicked.connect(self.LEVEL)
		self.update_btn.clicked.connect(self.UPDATE)
		self.delete_btn.clicked.connect(self.DELETE)
		self.add_btn.clicked.connect(self.ADD)
		self.first_btn.clicked.connect(self.FIRST_STAGE)

		self.next_btn.clicked.connect(self.NEXT_STAGE)
		self.prev_btn.clicked.connect(self.PREVIOUS_STAGE)
		self.last_btn.clicked.connect(self.LAST_STAGE)
		

	def GET_DATA(self):
		
		db=sqlite3.connect("part.db")
		cursor=db.cursor()


		command= ''' SELECT * from use_data '''

		result=cursor.execute(command)

		self.table.setRowCount(0)

		for  row_number,row_data in enumerate(result):
			self.table.insertRow(row_number)
			for column_number,data in enumerate(row_data):
				self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))

		#Displaying refrences
		cursor2=db.cursor()
		cursor3=db.cursor()

		parts_nbr='''SELECT COUNT (DISTINCT Parts_Name) from use_data '''
		ref_nbr='''SELECT COUNT (DISTINCT Refrences ) from use_data '''
		
		result_ref_nbr=cursor2.execute(ref_nbr)
		result_parts_nbr=cursor3.execute(parts_nbr)

		self.lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
		self.lbl_parts_nbr.setText(str(result_parts_nbr.fetchone()[0]))

		cursor4=db.cursor()
		cursor5=db.cursor()

		min_hole='''SELECT MIN(NumberOfHoles) ,Refrences from use_data '''
		max_hole='''SELECT MAX(NumberOfHoles) ,Refrences from use_data '''

		result_min_hole=cursor4.execute(min_hole)
		result_max_hole=cursor5.execute(max_hole)

		r1=result_min_hole.fetchone()
		r2=result_max_hole.fetchone()

		self.lbl_min_hole.setText(str(r1[0]))
		self.lbl_max_hole.setText(str(r2[0]))

		self.lbl_min_hole_2.setText(str(r1[1]))
		self.lbl_max_hole_2.setText(str(r2[1]))


		self.FIRST_STAGE()
		self.NAVIGATE()

		#if int(self.lbl_ref_nbr.text())<15:

	#here is the code
	def SEARCH(self):
			
		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		nbr=int(self.count_filter_txt.text())

		command= ''' SELECT * from use_data WHERE count<=?'''

		result=cursor.execute(command,[nbr])

		self.table.setRowCount(0)

		for  row_number,row_data in enumerate(result):
			self.table.insertRow(row_number)
			for column_number,data in enumerate(row_data):
				self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))




	def LEVEL(self):
		db=sqlite3.connect("part.db")
		cursor=db.cursor()
 
		command= ''' SELECT Refrences,Parts_Name,Count from use_data order by Count asc LIMIT 3 '''

		result=cursor.execute(command)

		self.table2.setRowCount(0)

		for  row_number,row_data in enumerate(result):
			self.table2.insertRow(row_number)
			for column_number,data in enumerate(row_data):
				self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))

		

	def NAVIGATE(self):
		
		global idx
		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		command=''' SELECT * FROM use_data WHERE ID=?  '''

		result= cursor.execute(command,[idx])
		val=result.fetchone()
		
		self.id.setText(str(val[0]))
		self.refrence.setText(str(val[1]))
		self.part_name.setText(str(val[2]))
		self.min_area.setText(str(val[3]))
		self.max_area.setText(str(val[4]))
		self.num_of_holes.setText(str(val[5]))
		self.min_dia.setText(str(val[6]))
		self.max_dia.setText(str(val[7]))
		self.count.setValue(val[8])


	def NEXT_STAGE(self):
			
		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		command=''' SELECT ID FROM use_data'''
		result=cursor.execute(command)
		
		val=result.fetchall()
		tot=len(val)
		
		global x
		global idx

		x=x+1

		if x<tot:
		   idx=val[x][0]
		   self.NAVIGATE()
		else:
		   x=tot-1
		   print("END OF FILE")

	

	def PREVIOUS_STAGE(self):
		
		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		command=''' SELECT ID FROM use_data'''
		result=cursor.execute(command)
		
		val=result.fetchall()
				
		global x
		global idx

		x=x-1

		if x>-1:
			idx=val[x][0]
			self.NAVIGATE()
		else:
			x=0
			print("BEGIN OF FILE")


	
	def LAST_STAGE(self):
		
		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		command=''' SELECT ID FROM use_data'''
		result=cursor.execute(command)
		
		val=result.fetchall()
		tot=len(val)
		
		global x
		global idx

		x=tot-1
		if x<tot:
			idx=val[x][0]
			self.NAVIGATE()
		else:
			x=tot-1
			print("END OF FILE")


	
	def FIRST_STAGE(self):
	
		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		command=''' SELECT ID FROM use_data'''
		result=cursor.execute(command)
		
		val=result.fetchall()
				
		global x
		global idx

		x=0
		if x>-1:
		   idx=val[x][0]
		   self.NAVIGATE()
		else:
			x=0
			print("END OF FILE")

	



	def UPDATE(self):

		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		id_=int(self.id.text())
		refrence_=self.refrence.text()
		part_name_=self.part_name.text()
		min_area_=self.min_area.text()
		max_area_=self.max_area.text()
		num_of_hole_=self.num_of_holes.text()
		min_dia_=self.min_dia.text()
		max_dia=self.max_dia.text()
		count_=str(self.count.value())

		rows=(refrence_, part_name_, min_area_, max_area_, num_of_hole_, min_dia_, max_dia,count_, id_ )

		command= (""" UPDATE use_data SET Refrences=?, Parts_Name=?, MinArea=?, MaxArea=?, NumberOfHoles=?, MinDiameter=?, MaxDiameter=?, Count=? WHERE Id=? """)


		cursor.execute(command,rows)

		db.commit()


	def DELETE(self):

		db=sqlite3.connect("part.db")
		cursor=db.cursor()
		
		d=self.id.text()

		command='''DELETE FROM use_data WHERE ID=? '''

		cursor.execute(command,d)
		
		db.commit()
	


	def ADD(self):

		db=sqlite3.connect("part.db")
		cursor=db.cursor()

		refrence_=self.refrence.text()
		part_name_=self.part_name.text()
		min_area_=self.min_area.text()
		max_area_=self.max_area.text()
		num_of_hole_=self.num_of_holes.text()
		min_dia_=self.min_dia.text()
		max_dia=self.max_dia.text()
		count_=str(self.count.value())

		rows=(refrence_, part_name_, min_area_, max_area_, num_of_hole_, min_dia_, max_dia,count_ )

		command= (""" INSERT INTO use_data (Refrences, Parts_Name, MinArea, MaxArea, NumberOfHoles, MinDiameter, MaxDiameter, Count) VALUES(?,?,?,?,?,?,?,?) """)


		cursor.execute(command,rows)

		db.commit()
   
	

def main():
	app=QApplication(sys.argv)
	window=Main()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()


