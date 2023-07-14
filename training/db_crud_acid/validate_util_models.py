from django.db.models.query_utils import Q

class validate_fields_model_util:

    @staticmethod
    def validate_if_field_exists_in_model(request, model, field_required, field_name, error_message):
        field_value = request.data.get(field_name, None)
        
        if not field_required and not field_value:
            return None
        
        if field_required and not field_value:
            message = f"The {field_name} field is required."
            return message
        
        criteria = Q(**{f"{field_name}__iexact": field_value})

        field_exists = model.objects.filter(criteria).exists()

        if field_exists:
            return error_message
        
        return None