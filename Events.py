from custom_exceptions import *
from PyQt5.QtWidgets import *
import re

from time import sleep


# region Base Classes

class EventListenerManager:
    def __init__(self, gui, db):
        
        self.gui = gui
        self.db = db

    def _add_event_listeners(self):
        raise UnimplementedMethodException("Method must be implemented in inheriting classes")


class MainWindowListener(EventListenerManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_event_listeners()

    def _add_event_listeners(self):
        # Bind all database methods into frontend elements
        self._add_crud_buttons_listeners()
        self._add_function_buttons_listeners()
        self._add_edit_db_and_collection_buttons_listeners()

    def _add_crud_buttons_listeners(self):
        create_button = self.gui.widget_objects['createButton']
        filter_button = self.gui.widget_objects['filterButton']
        modify_button = self.gui.widget_objects['modifyButton']
        delete_button = self.gui.widget_objects['deleteButton']

        #####

        # NOTE: query_data will be assigned from the popup windows created later
        query_data = ""

        ######

        def create_query(query_data=query_data):
            self.db.create_query(query_data)

        def filter_query(query_data=query_data):
            self.db.filter_query(query_data)

        def modify_query(query_data=query_data):
            self.db.modify_query(query_data)

        def delete_query(query_data=query_data):
            self.db.delete_query(query_data)

        #####

        create_button.clicked.connect(self.gui.show_create_window)
        filter_button.clicked.connect(self.gui.show_filter_window)
        modify_button.clicked.connect(self.gui.show_modify_window)
        delete_button.clicked.connect(self.gui.show_delete_window)

    def _add_function_buttons_listeners(self):

        for button_id, button  in self.gui.widget_objects.items():
            # this RegEx catches all objects with id ~= "functionNumberButton"
            if re.match("^function.*Button$", button_id):
                self._add_button_listener(button, button_id)

    def _add_button_listener(self, button, button_name: str):
        button.clicked.connect(lambda: self.gui.show_function_window(button_name, button))

    def _add_edit_db_and_collection_buttons_listeners(self):

        edit_database_button = self.gui.widget_objects['editDatabaseButton']
        edit_collection_button = self.gui.widget_objects['editCollectionButton']

        edit_database_button.clicked.connect(self.gui.view_edit_db_window)
        edit_collection_button.clicked.connect(self.gui.view_edit_collection_window)


class DynamicPopupWindowListener(EventListenerManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_field_listeners()

    def _add_field_listeners(self):
        for widget in self.gui.fields_widget.children():
            
            expected_type = type(QLineEdit())
            
            if type(widget) == expected_type:
                widget.setText("This is development code, so I can put anything I want here")


# endregion Base Classes


class WelcomeWindowListener(EventListenerManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._host_field, self._port_field = self._get_fields()

        self._add_event_listeners()


    def _get_fields(self):
        _host_field: QLineEdit = self.gui.widget_objects['hostLineEdit']
        _port_field: QLineEdit = self.gui.widget_objects['portLineEdit']

        return _host_field, _port_field

    def _add_event_listeners(self):
        self._add_run_button_listener()

    def _add_run_button_listener(self):
        self.gui.widget_objects['runButton'].clicked.connect(self._run_button_on_click)

    def _check_field_values(self):
        
        self._host_field.setDisabled(True)
        self._port_field.setDisabled(True)

        return True


    def _run_button_on_click(self):

        # Check fields
        if not self._check_field_values():
            raise BadFieldValueException("Invalid value entered in host field")

        # Attempt Connection

        # ???

        # Profit

        print("//{}:{}".format(self._host_field.text(), self._port_field.text()))

        self.gui.close()


# region Edit DB / Collection Window Listeners

class EditDatabaseWindowListener(EventListenerManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_event_listeners()

    def _add_event_listeners(self):
        self._add_buttons()
        self._add_line_edits()
        self._add_labels()

    def _add_buttons(self):
        pass

    def _add_line_edits(self):
        pass

    def _add_labels(self):
        pass


class EditCollectionWindowListener(EventListenerManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_event_listeners()

    def _add_event_listeners(self):
        self._add_buttons()
        self._add_line_edits()
        self._add_labels()

    def _add_buttons(self):
        pass

    def _add_line_edits(self):
        pass

    def _add_labels(self):
        pass


# endregion Edit DB / Collection Window Listeners


# region CRUD Window Listeners

class CreateWindowListener(DynamicPopupWindowListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_button_listener()

    def _add_button_listener(self):
        self.gui.widget_objects['createButton'].clicked.connect(lambda: print("Created Item (fake)"))
        self.gui.widget_objects['createButton'].clicked.connect(self._list_all_field_data)

    def _list_all_field_data(self):
        for widget in self.gui.fields_widget.children():

            if type(widget) == type(QLabel):
                print(field.text(), end="")

            if type(widget) == type(QLineEdit()):
                print(widget.text())


class FilterWindowListener(DynamicPopupWindowListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_button_listener()

    def _add_button_listener(self):
        self.gui.widget_objects['filterButton'].clicked.connect(lambda: print("Filtered Item (fake)"))
        self.gui.widget_objects['filterButton'].clicked.connect(self._list_all_field_data)

    def _list_all_field_data(self):
        for widget in self.gui.fields_widget.children():

            if type(widget) == type(QLabel):
                print(field.text(), end="")

            if type(widget) == type(QLineEdit()):
                print(widget.text())


class ModifyWindowListener(DynamicPopupWindowListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_button_listener()

    def _add_button_listener(self):
        self.gui.widget_objects['updateButton'].clicked.connect(lambda: print("Updated Item (fake)"))
        self.gui.widget_objects['updateButton'].clicked.connect(self._list_all_field_data)

    def _list_all_field_data(self):
        for widget in self.gui.fields_widget.children():

            if type(widget) == type(QLabel):
                print(field.text(), end="")

            if type(widget) == type(QLineEdit()):
                print(widget.text())


class DeleteWindowListener(DynamicPopupWindowListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._add_button_listener()

    def _add_button_listener(self):
        self.gui.widget_objects['deleteButton'].clicked.connect(lambda: print("Deleted Item (fake)"))
        self.gui.widget_objects['deleteButton'].clicked.connect(self._list_all_field_data)

    def _list_all_field_data(self):
        for widget in self.gui.fields_widget.children():

            if type(widget) == type(QLabel):
                print(field.text(), end="")

            if type(widget) == type(QLineEdit()):
                print(widget.text())

# endregion CRUD Window Listeners
