# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import core_functions as core
import gameplay_modules as gameplay

class Ui_Luupycards(object):
    def setupUi(self, Luupycards):
        if not Luupycards.objectName():
            Luupycards.setObjectName(u"Luupycards")
        Luupycards.resize(582, 574)
        font = QFont()
        font.setPointSize(12)
        Luupycards.setFont(font)
        icon = QIcon()
        icon.addFile(u"../v1/luupycards.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Luupycards.setWindowIcon(icon)
        Luupycards.setWindowOpacity(0.000000000000000)
        self.actionCSV = QAction(Luupycards)
        self.actionCSV.setObjectName(u"actionCSV")
        self.actionJSON = QAction(Luupycards)
        self.actionJSON.setObjectName(u"actionJSON")
        self.actionRead_the_docs = QAction(Luupycards)
        self.actionRead_the_docs.setObjectName(u"actionRead_the_docs")
        self.actionRead_the_docs.setFont(font)
        self.actionSave = QAction(Luupycards)
        self.actionSave.setObjectName(u"actionSave")
        self.actionNew = QAction(Luupycards)
        self.actionNew.setObjectName(u"actionNew")
        self.actionQuit = QAction(Luupycards)
        self.actionQuit.setObjectName(u"actionQuit")
        self.action_tabs_main_menu = QAction(Luupycards)
        self.action_tabs_main_menu.setObjectName(u"action_tabs_main_menu")
        self.action_tabs_main_menu.setCheckable(True)
        self.action_tabs_main_menu.setChecked(True)
        font1 = QFont()
        font1.setPointSize(9)
        self.action_tabs_main_menu.setFont(font1)
        self.action_tabls_play = QAction(Luupycards)
        self.action_tabls_play.setObjectName(u"action_tabls_play")
        self.action_tabls_play.setCheckable(True)
        self.action_tabls_play.setChecked(True)
        self.action_tabls_play.setFont(font1)
        self.action_tabs_settings = QAction(Luupycards)
        self.action_tabs_settings.setObjectName(u"action_tabs_settings")
        self.action_tabs_settings.setCheckable(True)
        self.action_tabs_settings.setChecked(True)
        self.action_tabs_settings.setFont(font1)
        self.action_tabs_inspector = QAction(Luupycards)
        self.action_tabs_inspector.setObjectName(u"action_tabs_inspector")
        self.action_tabs_inspector.setCheckable(True)
        self.action_tabs_inspector.setChecked(True)
        self.action_tabs_inspector.setFont(font1)
        self.centralwidget = QWidget(Luupycards)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 566, 497))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tab_main = QTabWidget(self.scrollAreaWidgetContents_2)
        self.tab_main.setObjectName(u"tab_main")
        self.tab_main.setEnabled(True)
        self.tab_main.setFont(font)
        self.tab_main.setLayoutDirection(Qt.LeftToRight)
        self.tab_main.setAutoFillBackground(False)
        self.tab_main.setDocumentMode(False)
        self.tab_main.setTabsClosable(False)
        self.tab_main.setMovable(True)
        self.tab_main_menu = QWidget()
        self.tab_main_menu.setObjectName(u"tab_main_menu")
        self.gridLayout_5 = QGridLayout(self.tab_main_menu)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.button_play = QPushButton(self.tab_main_menu)
        self.button_play.setObjectName(u"button_play")

        self.gridLayout_5.addWidget(self.button_play, 2, 1, 1, 1)

        self.layout_main_question_order = QVBoxLayout()
        self.layout_main_question_order.setObjectName(u"layout_main_question_order")
        self.label_question_order = QLabel(self.tab_main_menu)
        self.label_question_order.setObjectName(u"label_question_order")
        font2 = QFont()
        font2.setPointSize(16)
        self.label_question_order.setFont(font2)

        self.layout_main_question_order.addWidget(self.label_question_order, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.comboBox_question_order = QComboBox(self.tab_main_menu)
        self.comboBox_question_order.addItem("")
        self.comboBox_question_order.addItem("")
        self.comboBox_question_order.addItem("")
        self.comboBox_question_order.setObjectName(u"comboBox_question_order")

        self.layout_main_question_order.addWidget(self.comboBox_question_order)


        self.gridLayout_5.addLayout(self.layout_main_question_order, 0, 1, 1, 1)

        self.layout_main_mode = QVBoxLayout()
        self.layout_main_mode.setObjectName(u"layout_main_mode")
        self.label_mode = QLabel(self.tab_main_menu)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setFont(font2)

        self.layout_main_mode.addWidget(self.label_mode, 0, Qt.AlignHCenter)

        self.comboBox_modes = QComboBox(self.tab_main_menu)
        self.comboBox_modes.addItem("")
        self.comboBox_modes.addItem("")
        self.comboBox_modes.addItem("")
        self.comboBox_modes.addItem("")
        self.comboBox_modes.setObjectName(u"comboBox_modes")

        self.layout_main_mode.addWidget(self.comboBox_modes)


        self.gridLayout_5.addLayout(self.layout_main_mode, 0, 0, 1, 1)

        self.button_quit = QPushButton(self.tab_main_menu)
        self.button_quit.setObjectName(u"button_quit")

        self.gridLayout_5.addWidget(self.button_quit, 2, 0, 1, 1)

        self.verticalSpacer_main_menu = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_main_menu, 1, 0, 1, 1)

        self.tab_main.addTab(self.tab_main_menu, "")
        self.play = QWidget()
        self.play.setObjectName(u"play")
        self.gridLayout_13 = QGridLayout(self.play)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.button_check = QPushButton(self.play)
        self.button_check.setObjectName(u"button_check")

        self.gridLayout_13.addWidget(self.button_check, 6, 2, 1, 1)

        self.horizontalSpacer_play_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_play_right, 1, 2, 1, 1)

        self.label_question = QLabel(self.play)
        self.label_question.setObjectName(u"label_question")
        font3 = QFont()
        font3.setPointSize(20)
        self.label_question.setFont(font3)

        self.gridLayout_13.addWidget(self.label_question, 1, 1, 1, 1)

        self.horizontalSpacer_play_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_play_left, 1, 0, 1, 1)

        self.verticalSpacer_play_middle = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_play_middle, 2, 1, 1, 1)

        self.verticalSpacer_play_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_play_top, 0, 1, 1, 1)

        self.verticalSpacer_play_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_play_bottom, 4, 1, 1, 1)

        self.lineEdit_answer = QLineEdit(self.play)
        self.lineEdit_answer.setObjectName(u"lineEdit_answer")
        self.lineEdit_answer.setFont(font2)
        self.lineEdit_answer.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lineEdit_answer, 3, 0, 1, 3)

        self.tab_main.addTab(self.play, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.gridLayout_8 = QGridLayout(self.tab_settings)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_settings_settings = QScrollArea(self.tab_settings)
        self.scrollArea_settings_settings.setObjectName(u"scrollArea_settings_settings")
        self.scrollArea_settings_settings.setWidgetResizable(True)
        self.scrollAreaWidgetContents_settings = QWidget()
        self.scrollAreaWidgetContents_settings.setObjectName(u"scrollAreaWidgetContents_settings")
        self.scrollAreaWidgetContents_settings.setGeometry(QRect(0, -49, 516, 423))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_settings)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_settings = QGridLayout()
        self.gridLayout_settings.setObjectName(u"gridLayout_settings")
        self.label_all_time_survival_streak_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_all_time_survival_streak_2.setObjectName(u"label_all_time_survival_streak_2")
        self.label_all_time_survival_streak_2.setFont(font)

        self.gridLayout_settings.addWidget(self.label_all_time_survival_streak_2, 1, 0, 1, 1)

        self.label_fuzzy_select_precent_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_fuzzy_select_precent_2.setObjectName(u"label_fuzzy_select_precent_2")

        self.gridLayout_settings.addWidget(self.label_fuzzy_select_precent_2, 9, 0, 1, 1)

        self.label_all_time_streak_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_all_time_streak_2.setObjectName(u"label_all_time_streak_2")
        self.label_all_time_streak_2.setFont(font)

        self.gridLayout_settings.addWidget(self.label_all_time_streak_2, 0, 0, 1, 1)

        self.reset_all_time_survival_streak_value_2 = QCheckBox(self.scrollAreaWidgetContents_settings)
        self.reset_all_time_survival_streak_value_2.setObjectName(u"reset_all_time_survival_streak_value_2")
        self.reset_all_time_survival_streak_value_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_settings.addWidget(self.reset_all_time_survival_streak_value_2, 3, 1, 1, 1)

        self.label_reset_all_time_streak_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_reset_all_time_streak_2.setObjectName(u"label_reset_all_time_streak_2")

        self.gridLayout_settings.addWidget(self.label_reset_all_time_streak_2, 2, 0, 1, 1)

        self.label_min_question_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_min_question_2.setObjectName(u"label_min_question_2")

        self.gridLayout_settings.addWidget(self.label_min_question_2, 4, 0, 1, 1)

        self.label_multiple_choice_max_options_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_multiple_choice_max_options_2.setObjectName(u"label_multiple_choice_max_options_2")

        self.gridLayout_settings.addWidget(self.label_multiple_choice_max_options_2, 7, 0, 1, 1)

        self.multiple_choice_max_options_value_2 = QSpinBox(self.scrollAreaWidgetContents_settings)
        self.multiple_choice_max_options_value_2.setObjectName(u"multiple_choice_max_options_value_2")
        self.multiple_choice_max_options_value_2.setMinimum(2)
        self.multiple_choice_max_options_value_2.setMaximum(26)
        self.multiple_choice_max_options_value_2.setValue(5)

        self.gridLayout_settings.addWidget(self.multiple_choice_max_options_value_2, 7, 1, 1, 1)

        self.fuzzy_select_precent_value_2 = QSpinBox(self.scrollAreaWidgetContents_settings)
        self.fuzzy_select_precent_value_2.setObjectName(u"fuzzy_select_precent_value_2")
        self.fuzzy_select_precent_value_2.setMinimum(1)
        self.fuzzy_select_precent_value_2.setMaximum(100)
        self.fuzzy_select_precent_value_2.setValue(90)

        self.gridLayout_settings.addWidget(self.fuzzy_select_precent_value_2, 9, 1, 1, 1)

        self.min_question_value_2 = QSpinBox(self.scrollAreaWidgetContents_settings)
        self.min_question_value_2.setObjectName(u"min_question_value_2")
        self.min_question_value_2.setMinimum(1)
        self.min_question_value_2.setMaximum(1000000)

        self.gridLayout_settings.addWidget(self.min_question_value_2, 4, 1, 1, 1)

        self.label_lives_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_lives_2.setObjectName(u"label_lives_2")

        self.gridLayout_settings.addWidget(self.label_lives_2, 8, 0, 1, 1)

        self.max_question_value_2 = QSpinBox(self.scrollAreaWidgetContents_settings)
        self.max_question_value_2.setObjectName(u"max_question_value_2")
        self.max_question_value_2.setMinimum(1)
        self.max_question_value_2.setMaximum(1000000)

        self.gridLayout_settings.addWidget(self.max_question_value_2, 5, 1, 1, 1)

        self.label_show_current_question_number_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_show_current_question_number_2.setObjectName(u"label_show_current_question_number_2")

        self.gridLayout_settings.addWidget(self.label_show_current_question_number_2, 6, 0, 1, 1)

        self.show_current_question_number_value_2 = QCheckBox(self.scrollAreaWidgetContents_settings)
        self.show_current_question_number_value_2.setObjectName(u"show_current_question_number_value_2")
        self.show_current_question_number_value_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_current_question_number_value_2.setChecked(True)

        self.gridLayout_settings.addWidget(self.show_current_question_number_value_2, 6, 1, 1, 1)

        self.lives_value_2 = QSpinBox(self.scrollAreaWidgetContents_settings)
        self.lives_value_2.setObjectName(u"lives_value_2")
        self.lives_value_2.setMinimum(1)
        self.lives_value_2.setValue(5)

        self.gridLayout_settings.addWidget(self.lives_value_2, 8, 1, 1, 1)

        self.label_max_question_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_max_question_2.setObjectName(u"label_max_question_2")

        self.gridLayout_settings.addWidget(self.label_max_question_2, 5, 0, 1, 1)

        self.all_time_streak_value_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.all_time_streak_value_2.setObjectName(u"all_time_streak_value_2")
        self.all_time_streak_value_2.setFont(font)
        self.all_time_streak_value_2.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

        self.gridLayout_settings.addWidget(self.all_time_streak_value_2, 0, 1, 1, 1)

        self.label_reset_all_time_survival_streak_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.label_reset_all_time_survival_streak_2.setObjectName(u"label_reset_all_time_survival_streak_2")

        self.gridLayout_settings.addWidget(self.label_reset_all_time_survival_streak_2, 3, 0, 1, 1)

        self.reset_all_time_streak_value_2 = QCheckBox(self.scrollAreaWidgetContents_settings)
        self.reset_all_time_streak_value_2.setObjectName(u"reset_all_time_streak_value_2")
        font4 = QFont()
        font4.setKerning(True)
        self.reset_all_time_streak_value_2.setFont(font4)
        self.reset_all_time_streak_value_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_settings.addWidget(self.reset_all_time_streak_value_2, 2, 1, 1, 1)

        self.all_time_survival_streak_value_2 = QLabel(self.scrollAreaWidgetContents_settings)
        self.all_time_survival_streak_value_2.setObjectName(u"all_time_survival_streak_value_2")
        self.all_time_survival_streak_value_2.setFont(font)
        self.all_time_survival_streak_value_2.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

        self.gridLayout_settings.addWidget(self.all_time_survival_streak_value_2, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_settings, 0, 0, 1, 1)

        self.scrollArea_settings_settings.setWidget(self.scrollAreaWidgetContents_settings)

        self.gridLayout_8.addWidget(self.scrollArea_settings_settings, 9, 1, 1, 1)

        self.horizontalLayout_settings_buttons = QHBoxLayout()
        self.horizontalLayout_settings_buttons.setObjectName(u"horizontalLayout_settings_buttons")
        self.button_settings_reset_2 = QPushButton(self.tab_settings)
        self.button_settings_reset_2.setObjectName(u"button_settings_reset_2")

        self.horizontalLayout_settings_buttons.addWidget(self.button_settings_reset_2)

        self.button_settings_save_2 = QPushButton(self.tab_settings)
        self.button_settings_save_2.setObjectName(u"button_settings_save_2")

        self.horizontalLayout_settings_buttons.addWidget(self.button_settings_save_2)


        self.gridLayout_8.addLayout(self.horizontalLayout_settings_buttons, 12, 1, 1, 1)

        self.tab_main.addTab(self.tab_settings, "")
        self.tab_inspector = QWidget()
        self.tab_inspector.setObjectName(u"tab_inspector")
        self.verticalLayout = QVBoxLayout(self.tab_inspector)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.tab_inspector)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_inspector_buttons = QHBoxLayout()
        self.horizontalLayout_inspector_buttons.setObjectName(u"horizontalLayout_inspector_buttons")
        self.button_save_file = QPushButton(self.tab_inspector)
        self.button_save_file.setObjectName(u"button_save_file")

        self.horizontalLayout_inspector_buttons.addWidget(self.button_save_file)

        self.button_save_memory = QPushButton(self.tab_inspector)
        self.button_save_memory.setObjectName(u"button_save_memory")

        self.horizontalLayout_inspector_buttons.addWidget(self.button_save_memory)


        self.verticalLayout.addLayout(self.horizontalLayout_inspector_buttons)

        self.tab_main.addTab(self.tab_inspector, "")

        self.gridLayout_11.addWidget(self.tab_main, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)

        Luupycards.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Luupycards)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 582, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpen = QMenu(self.menuFile)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuOpen.setFont(font1)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTabs = QMenu(self.menubar)
        self.menuTabs.setObjectName(u"menuTabs")
        Luupycards.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Luupycards)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        Luupycards.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTabs.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuOpen.addAction(self.actionCSV)
        self.menuOpen.addAction(self.actionJSON)
        self.menuHelp.addAction(self.actionRead_the_docs)
        self.menuTabs.addAction(self.action_tabs_main_menu)
        self.menuTabs.addAction(self.action_tabls_play)
        self.menuTabs.addAction(self.action_tabs_settings)
        self.menuTabs.addAction(self.action_tabs_inspector)

        self.retranslateUi(Luupycards)
        self.lineEdit_answer.returnPressed.connect(self.button_check.click)

        self.tab_main.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Luupycards)

        # from under this these are self set.

        ## setting up

        # options
        self.reload_settings()

        # I'll set some default states of the tabs
        self.tabs_event_play()
        self.tabs_event_inspector()
        self.action_tabls_play.setChecked(False)
        self.action_tabs_inspector.setChecked(False)

        ## Buttons
        # Quit buttons
        self.button_quit.clicked.connect(self.quit_action)
        self.actionQuit.triggered.connect(self.quit_action)

        # tab toggle buttons
        self.action_tabs_main_menu.triggered.connect(self.tabs_event_main_menu)  # main menu
        self.action_tabls_play.triggered.connect(self.tabs_event_play)  # play
        self.action_tabs_settings.triggered.connect(self.tabs_event_settings)  # settings
        self.action_tabs_inspector.triggered.connect(self.tabs_event_inspector)  # inspector

        # file buttons
        self.menuOpen.triggered.connect(self.open_dir_dialog)

        # Start playing
        self.button_play.clicked.connect(self.gameplay_setup)

    def open_dir_dialog(self):
        pass

    def quit_action(self):
        exit()

    def gameplay_setup(self):
        # determine mode
        current_mode = self.comboBox_modes.currentText()
        current_order = self.comboBox_question_order.currentText()

        # set tab to play
        self.tab_main.setCurrentWidget(self.play)
        self.action_tabls_play.setEnabled(True)
        self.play.setEnabled(True)

        print(current_mode, current_order)  # then pass to backend

    def tabs_event_main_menu(self):
        # simple toggle
        if self.tab_main_menu.isEnabled():
            self.tab_main_menu.setEnabled(False)
        else:
            self.tab_main_menu.setEnabled(True)

    def tabs_event_play(self):
        # simple toggle
        if self.play.isEnabled():
            self.play.setEnabled(False)
        else:
            self.play.setEnabled(True)

    def tabs_event_settings(self):
        # simple toggle
        if self.tab_settings.isEnabled():
            self.tab_settings.setEnabled(False)
        else:
            self.tab_settings.setEnabled(True)

    def tabs_event_inspector(self):
        # simple toggle
        if self.tab_inspector.isEnabled():
            self.tab_inspector.setEnabled(False)
        else:
            self.tab_inspector.setEnabled(True)

    def reload_settings(self):
        options = core.get_options("load")

        self.all_time_streak_value_2.setText(str(options["all time streak"]))
        self.all_time_survival_streak_value_2.setText(str(options["all time survival streak"]))
        self.reset_all_time_streak_value_2.setCheckState(options["reset all time streak"])  # this is broken
        self.reset_all_time_survival_streak_value_2.setCheckState(options["reset all time survival streak"])
        self.min_question_value_2.setValue(options["min question"])
        self.max_question_value_2.setValue(options["max question"])
        self.show_current_question_number_value_2.setCheckState(options["show current question number"])
        self.multiple_choice_max_options_value_2.setValue(options["multiple choice max options"])
        self.lives_value_2.setValue(options["lives"])
        self.fuzzy_select_precent_value_2.setValue(options["fuzzy select percent"])

    def save_settings(self):
        pass



    # setupUi

    def retranslateUi(self, Luupycards):
        Luupycards.setWindowTitle(QCoreApplication.translate("Luupycards", u"Luupycards", None))
#if QT_CONFIG(tooltip)
        Luupycards.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.actionCSV.setText(QCoreApplication.translate("Luupycards", u"CSV", None))
#if QT_CONFIG(tooltip)
        self.actionCSV.setToolTip(QCoreApplication.translate("Luupycards", u"Open a CSV file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCSV.setShortcut(QCoreApplication.translate("Luupycards", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionJSON.setText(QCoreApplication.translate("Luupycards", u"JSON", None))
#if QT_CONFIG(tooltip)
        self.actionJSON.setToolTip(QCoreApplication.translate("Luupycards", u"Open a JSON file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionJSON.setShortcut(QCoreApplication.translate("Luupycards", u"Ctrl+J", None))
#endif // QT_CONFIG(shortcut)
        self.actionRead_the_docs.setText(QCoreApplication.translate("Luupycards", u"Just test stuff", None))
        self.actionSave.setText(QCoreApplication.translate("Luupycards", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("Luupycards", u"Saves the current file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("Luupycards", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("Luupycards", u"New", None))
#if QT_CONFIG(tooltip)
        self.actionNew.setToolTip(QCoreApplication.translate("Luupycards", u"Create a new pair file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("Luupycards", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("Luupycards", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("Luupycards", u"Quits this app", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("Luupycards", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_tabs_main_menu.setText(QCoreApplication.translate("Luupycards", u"Main Menu", None))
        self.action_tabls_play.setText(QCoreApplication.translate("Luupycards", u"Play", None))
        self.action_tabs_settings.setText(QCoreApplication.translate("Luupycards", u"Settings", None))
        self.action_tabs_inspector.setText(QCoreApplication.translate("Luupycards", u"Inspector", None))
#if QT_CONFIG(tooltip)
        self.tab_main.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tab_main.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.button_play.setToolTip(QCoreApplication.translate("Luupycards", u"Start the game", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_play.setStatusTip(QCoreApplication.translate("Luupycards", u"Start the game", None))
#endif // QT_CONFIG(statustip)
        self.button_play.setText(QCoreApplication.translate("Luupycards", u"Play", None))
        self.label_question_order.setText(QCoreApplication.translate("Luupycards", u"Question order", None))
        self.comboBox_question_order.setItemText(0, QCoreApplication.translate("Luupycards", u"Forward", None))
        self.comboBox_question_order.setItemText(1, QCoreApplication.translate("Luupycards", u"Reverse", None))
        self.comboBox_question_order.setItemText(2, QCoreApplication.translate("Luupycards", u"Random", None))

#if QT_CONFIG(tooltip)
        self.comboBox_question_order.setToolTip(QCoreApplication.translate("Luupycards", u"Choose the question order", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBox_question_order.setStatusTip(QCoreApplication.translate("Luupycards", u"Choose the question order", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.label_mode.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_mode.setText(QCoreApplication.translate("Luupycards", u"Mode", None))
        self.comboBox_modes.setItemText(0, QCoreApplication.translate("Luupycards", u"Normal", None))
        self.comboBox_modes.setItemText(1, QCoreApplication.translate("Luupycards", u"Reverse", None))
        self.comboBox_modes.setItemText(2, QCoreApplication.translate("Luupycards", u"Multiple Choice", None))
        self.comboBox_modes.setItemText(3, QCoreApplication.translate("Luupycards", u"Survive!", None))

#if QT_CONFIG(tooltip)
        self.comboBox_modes.setToolTip(QCoreApplication.translate("Luupycards", u"Choose the mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBox_modes.setStatusTip(QCoreApplication.translate("Luupycards", u"Choose the mode", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.button_quit.setToolTip(QCoreApplication.translate("Luupycards", u"Close this app", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_quit.setStatusTip(QCoreApplication.translate("Luupycards", u"Close this app", None))
#endif // QT_CONFIG(statustip)
        self.button_quit.setText(QCoreApplication.translate("Luupycards", u"Quit", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_main_menu), QCoreApplication.translate("Luupycards", u"Main Menu", None))
#if QT_CONFIG(tooltip)
        self.button_check.setToolTip(QCoreApplication.translate("Luupycards", u"Check that did you answer correctly", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_check.setStatusTip(QCoreApplication.translate("Luupycards", u"Check that did you answer correctly", None))
#endif // QT_CONFIG(statustip)
        self.button_check.setText(QCoreApplication.translate("Luupycards", u"Check", None))
#if QT_CONFIG(tooltip)
        self.label_question.setToolTip(QCoreApplication.translate("Luupycards", u"The question", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_question.setStatusTip(QCoreApplication.translate("Luupycards", u"The question", None))
#endif // QT_CONFIG(statustip)
        self.label_question.setText(QCoreApplication.translate("Luupycards", u"Question", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_answer.setToolTip(QCoreApplication.translate("Luupycards", u"Input your answer", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_answer.setStatusTip(QCoreApplication.translate("Luupycards", u"Input your answer", None))
#endif // QT_CONFIG(statustip)
        self.lineEdit_answer.setText("")
        self.tab_main.setTabText(self.tab_main.indexOf(self.play), QCoreApplication.translate("Luupycards", u"Play", None))
#if QT_CONFIG(tooltip)
        self.label_all_time_survival_streak_2.setToolTip(QCoreApplication.translate("Luupycards", u"Your all time survival streak", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_all_time_survival_streak_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Your all time survival streak", None))
#endif // QT_CONFIG(statustip)
        self.label_all_time_survival_streak_2.setText(QCoreApplication.translate("Luupycards", u"All time survival streak", None))
#if QT_CONFIG(tooltip)
        self.label_fuzzy_select_precent_2.setToolTip(QCoreApplication.translate("Luupycards", u"How wrong can the answer be for it to be count correct. 100 is disabled.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_fuzzy_select_precent_2.setStatusTip(QCoreApplication.translate("Luupycards", u"How wrong can the answer be for it to be count correct. 100 is disabled.", None))
#endif // QT_CONFIG(statustip)
        self.label_fuzzy_select_precent_2.setText(QCoreApplication.translate("Luupycards", u"Fuzzy select percent", None))
#if QT_CONFIG(tooltip)
        self.label_all_time_streak_2.setToolTip(QCoreApplication.translate("Luupycards", u"Your all time streak", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_all_time_streak_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Your all time streak", None))
#endif // QT_CONFIG(statustip)
        self.label_all_time_streak_2.setText(QCoreApplication.translate("Luupycards", u"All time streak", None))
        self.reset_all_time_survival_streak_value_2.setText("")
#if QT_CONFIG(tooltip)
        self.label_reset_all_time_streak_2.setToolTip(QCoreApplication.translate("Luupycards", u"Reset your all time streak", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_reset_all_time_streak_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Reset your all time streak", None))
#endif // QT_CONFIG(statustip)
        self.label_reset_all_time_streak_2.setText(QCoreApplication.translate("Luupycards", u"Reset all time streak", None))
#if QT_CONFIG(tooltip)
        self.label_min_question_2.setToolTip(QCoreApplication.translate("Luupycards", u"Minimum question number it will ask you", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_min_question_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Minimum question number it will ask you", None))
#endif // QT_CONFIG(statustip)
        self.label_min_question_2.setText(QCoreApplication.translate("Luupycards", u"Min question", None))
#if QT_CONFIG(tooltip)
        self.label_multiple_choice_max_options_2.setToolTip(QCoreApplication.translate("Luupycards", u"The ammount of answer candidates in multiple choice", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_multiple_choice_max_options_2.setStatusTip(QCoreApplication.translate("Luupycards", u"The ammount of answer candidates in multiple choice", None))
#endif // QT_CONFIG(statustip)
        self.label_multiple_choice_max_options_2.setText(QCoreApplication.translate("Luupycards", u"Multiple choice max options", None))
#if QT_CONFIG(tooltip)
        self.label_lives_2.setToolTip(QCoreApplication.translate("Luupycards", u"The ammount of lives in Survive!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_lives_2.setStatusTip(QCoreApplication.translate("Luupycards", u"The ammount of lives in Survive!", None))
#endif // QT_CONFIG(statustip)
        self.label_lives_2.setText(QCoreApplication.translate("Luupycards", u"Lives", None))
#if QT_CONFIG(tooltip)
        self.label_show_current_question_number_2.setToolTip(QCoreApplication.translate("Luupycards", u"Whether to show the current question number", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_show_current_question_number_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Whether to show the current question number", None))
#endif // QT_CONFIG(statustip)
        self.label_show_current_question_number_2.setText(QCoreApplication.translate("Luupycards", u"Show current question number", None))
        self.show_current_question_number_value_2.setText("")
#if QT_CONFIG(tooltip)
        self.label_max_question_2.setToolTip(QCoreApplication.translate("Luupycards", u"Maximum question number it will ask you", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_max_question_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Maximum question number it will ask you", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_max_question_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_max_question_2.setText(QCoreApplication.translate("Luupycards", u"Max question", None))
        self.all_time_streak_value_2.setText(QCoreApplication.translate("Luupycards", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_reset_all_time_survival_streak_2.setToolTip(QCoreApplication.translate("Luupycards", u"Reset your all time survival streak", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_reset_all_time_survival_streak_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Reset your all time survival streak", None))
#endif // QT_CONFIG(statustip)
        self.label_reset_all_time_survival_streak_2.setText(QCoreApplication.translate("Luupycards", u"Reset all time survival streak", None))
        self.reset_all_time_streak_value_2.setText("")
        self.all_time_survival_streak_value_2.setText(QCoreApplication.translate("Luupycards", u"0", None))
#if QT_CONFIG(tooltip)
        self.button_settings_reset_2.setToolTip(QCoreApplication.translate("Luupycards", u"Reset to default values", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_settings_reset_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Reset to default values", None))
#endif // QT_CONFIG(statustip)
        self.button_settings_reset_2.setText(QCoreApplication.translate("Luupycards", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.button_settings_save_2.setToolTip(QCoreApplication.translate("Luupycards", u"Save these settings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_settings_save_2.setStatusTip(QCoreApplication.translate("Luupycards", u"Save these settings", None))
#endif // QT_CONFIG(statustip)
        self.button_settings_save_2.setText(QCoreApplication.translate("Luupycards", u"Save", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_settings), QCoreApplication.translate("Luupycards", u"Settings", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Luupycards", u"Questions", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Luupycards", u"Answers", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Luupycards", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Luupycards", u"2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Luupycards", u"3", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Luupycards", u"4", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Luupycards", u"5", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Luupycards", u"[\"question1\"]", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Luupycards", u"[\"answer1a\", \"answer1b\"]", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Luupycards", u"[\"question2\"]", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Luupycards", u"[\"answer2a\"]", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Luupycards", u"[\"question3\"]", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Luupycards", u"[\"answer3a\", \"answer3b\", \"answer3c\"]", None));
        ___qtablewidgetitem13 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Luupycards", u"[\"question4\"]", None));
        ___qtablewidgetitem14 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Luupycards", u"[\"answer4a\", \"answer4b\"]", None));
        ___qtablewidgetitem15 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Luupycards", u"[\"question5\"]", None));
        ___qtablewidgetitem16 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Luupycards", u"[\"answer5a\"]", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("Luupycards", u"Your pairs nicely in raw Python", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip(QCoreApplication.translate("Luupycards", u"You can edit them, but be careful!", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.button_save_file.setToolTip(QCoreApplication.translate("Luupycards", u"Save to a CSV file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_save_file.setStatusTip(QCoreApplication.translate("Luupycards", u"Save to a CSV file", None))
#endif // QT_CONFIG(statustip)
        self.button_save_file.setText(QCoreApplication.translate("Luupycards", u"Save to file", None))
#if QT_CONFIG(tooltip)
        self.button_save_memory.setToolTip(QCoreApplication.translate("Luupycards", u"Saves changes to the program memory", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_save_memory.setStatusTip(QCoreApplication.translate("Luupycards", u"Saves changes to the program memory", None))
#endif // QT_CONFIG(statustip)
        self.button_save_memory.setText(QCoreApplication.translate("Luupycards", u"Save to memory", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_inspector), QCoreApplication.translate("Luupycards", u"Inspector", None))
        self.menuFile.setTitle(QCoreApplication.translate("Luupycards", u"File", None))
#if QT_CONFIG(tooltip)
        self.menuOpen.setToolTip(QCoreApplication.translate("Luupycards", u"Open a file", None))
#endif // QT_CONFIG(tooltip)
        self.menuOpen.setTitle(QCoreApplication.translate("Luupycards", u"Open", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Luupycards", u"Help", None))
#if QT_CONFIG(tooltip)
        self.menuTabs.setToolTip(QCoreApplication.translate("Luupycards", u"Toggle different tabs on or off", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.menuTabs.setStatusTip(QCoreApplication.translate("Luupycards", u"Toggle different tabs on or off", None))
#endif // QT_CONFIG(statustip)
        self.menuTabs.setTitle(QCoreApplication.translate("Luupycards", u"Tabs", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Luupycards = QMainWindow()
    ui = Ui_Luupycards()
    ui.setupUi(Luupycards)
    Luupycards.show()
    sys.exit(app.exec())