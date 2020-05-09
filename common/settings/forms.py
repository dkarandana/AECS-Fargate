from django import forms


class BaseSettingForm(forms.Form):

    '''
        VIEW ABSTRACT SETTING CLASS FOR MORE DETAILS
        MODEL - SETTING MODEL
    '''

    MODEL = None

    def get_all_data_in_db(self):

        queryset = self.MODEL.objects.all()
        queryset = queryset.values("key", 'value_type', 'value')
        return queryset

    def get_setting_by_key(self, db_data=None, structure_data=None,key= None):

        '''
            db_data = queryset.values()
            structure_data = [{}] # look model structure
            key = string
        '''

        returnData = {
            'status': False,
            'key': '',
            'value': '',
            'value_type': ''
        }
        
        # if pass db data queryset.values()
        if db_data:

            for data in db_data:

                db_key = data['key']
                db_value = data['value']
                db_value_type = data['value_type']

                if db_key == key:

                    returnData['status'] = True
                    returnData['key'] = db_key
                    returnData['value'] = db_value
                    returnData['value_type'] = db_value_type
                    break
            
            return returnData
        
        # if pass model structure data
        elif structure_data:
        
            for setting in  self.MODEL.STRUCTURE:

                setting_key = setting['FIELD_NAME']
                setting_value_type = setting['VALUE_TYPE']

                if setting_key == key:
                    
                    returnData['status'] = True
                    returnData['key'] = setting_key
                    returnData['value_type'] = setting_value_type
                    break
            
            return returnData
        
        # if not pass anything
        else:
            return returnData

    def __init__(self, *args, **kwargs):

        # check config model
        if not self.MODEL:
            raise AttributeError("Base Class of Setting Form must include MODEL Attribute")

        super().__init__(*args, **kwargs)
        request_method = 'POST' if self.data else 'GET'

        # check db_data
        if request_method == 'GET':
            db_data = self.get_all_data_in_db()
        else:
            db_data = []

        # read all field structure and create each field
        for fieldSetting in self.MODEL.STRUCTURE:
            
            try:

                field_name = fieldSetting.get('FIELD_NAME')
                field_type = fieldSetting.get('FIELD_TYPE')
                field_widget = fieldSetting.get('FIELD_WIDGET')
                is_required = fieldSetting.get('IS_REQUIRED')
                is_disabled = fieldSetting.get('IS_DISABLED')
                help_text = fieldSetting.get("HELP_TEXT")

                self.fields[field_name] =  field_type(
                    required=is_required, widget=field_widget, 
                    disabled=is_disabled, help_text=help_text
                )

                # SET inital value only get method
                if request_method == "GET":
                    setting_db_data = self.get_setting_by_key(db_data=db_data, key=field_name)
                    self.fields[field_name].initial = setting_db_data['value']

            except Exception:
                pass
                # add log

    def get_setting_objs_from_keys(self, keys):
        
        '''
            return tuple (object, is_new_object)
        '''
        queryset = self.MODEL.objects.filter(key__in=keys)
        return queryset
    
    def change_settings(self):
        '''
            this method called after is_valid method fire
        '''
        try:
            cleaned_data = self.cleaned_data
            all_keys = cleaned_data.keys()

            settingObjects = self.get_setting_objs_from_keys(all_keys)

            # iterate each settings
            for eachSetting in settingObjects:
                
                db_setting_key = eachSetting.key
                post_setting_value = cleaned_data.get(db_setting_key)
                structure_value_response = self.get_setting_by_key(
                    structure_data=self.MODEL.STRUCTURE,
                    key=db_setting_key
                )
                structure_value_type = structure_value_response['value_type']

                if post_setting_value:            
                    eachSetting.value = post_setting_value
                    eachSetting.value_type = structure_value_type
                    eachSetting.full_clean()
                    eachSetting.save()
        
        except Exception as err:
            # add logs
            return None
        else:
            return True


            


        
