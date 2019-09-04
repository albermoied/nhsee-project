from django import forms

class JudgeAssignmentForm(forms.Form):
    project_id = forms.CharField(max_length=255, required=True)
    judge_id = forms.CharField(max_length=255, required=True)
    goal_score = forms.DecimalField(max_digits=10, required=True)
    plan_score = forms.DecimalField(max_digits=10, required=True, decimal_places=6)
    action_score = forms.DecimalField(max_digits=10, required=True, decimal_places=6)
    result_analysis_score = forms.DecimalField(max_digits=10, required=True, decimal_places=6)
    communication_score = forms.DecimalField(max_digits=10, required=True, decimal_places=6)
    raw_total = forms.DecimalField(max_digits=10, required=True, decimal_places=6)
